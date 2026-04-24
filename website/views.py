from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
import os
import logging
import requests

from .forms import ContactForm

logger = logging.getLogger(__name__)

CONTACT_RATE_LIMIT = 5
CONTACT_RATE_LIMIT_WINDOW_SECONDS = 3600


def get_client_ip(request):
    forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if forwarded_for:
        return forwarded_for.split(',')[0].strip()
    return request.META.get('REMOTE_ADDR', 'unknown')


def send_contact_email_via_mailjet(contact_data):
    """Send contact form submissions via Mailjet API."""
    api_key = os.environ.get('MAILJET_API_KEY')
    api_secret = os.environ.get('MAILJET_API_SECRET')
    sender_email = os.environ.get('MAILJET_SENDER_EMAIL')
    recipient_email = os.environ.get('MAILJET_RECIPIENT_EMAIL')

    if not api_key or not api_secret or not sender_email or not recipient_email:
        logger.warning('Mailjet environment variables are missing')
        return False

    sender_name = os.environ.get('MAILJET_SENDER_NAME', 'Website Contact Form')
    recipient_name = os.environ.get('MAILJET_RECIPIENT_NAME', 'Site Owner')

    payload = {
        'Messages': [
            {
                'From': {
                    'Email': sender_email,
                    'Name': sender_name,
                },
                'To': [
                    {
                        'Email': recipient_email,
                        'Name': recipient_name,
                    }
                ],
                'ReplyTo': {
                    'Email': contact_data['email'],
                    'Name': contact_data['name'],
                },
                'Subject': f"New contact form submission from {contact_data['name']}",
                'TextPart': contact_data['message'],
            }
        ]
    }

    try:
        auth_credentials = (api_key, api_secret)
        response = requests.post(
            'https://api.mailjet.com/v3.1/send',
            auth=auth_credentials,
            json=payload,
            timeout=10,
        )
        response.raise_for_status()
        logger.info('Mailjet accepted contact form submission for %s with status %s', recipient_email, response.status_code)
        return True
    except Exception as exc:
        response_text = ''
        if hasattr(exc, 'response') and exc.response is not None:
            response_text = exc.response.text
        logger.error('Error sending Mailjet email: %s %s', exc, response_text)
        return False

def get_github_contributions():
    """Fetch GitHub contributions using GraphQL API"""
    cache_key = 'github_contributions'
    cached_data = cache.get(cache_key)
    
    if cached_data:
        return cached_data
    
    try:
        github_token = os.environ.get('GITHUB_TOKEN')
        if not github_token:
            logger.warning('GITHUB_TOKEN not set in environment variables')
            return None
        
        # GraphQL query to get contributions and user info
        query = '''
        query {
            viewer {
                login
                contributionsCollection {
                    contributionCalendar {
                        totalContributions
                    }
                }
            }
        }
        '''
        
        headers = {
            'Authorization': f'Bearer {github_token}',
            'Content-Type': 'application/json',
        }
        
        response = requests.post(
            'https://api.github.com/graphql',
            json={'query': query},
            headers=headers,
            timeout=5
        )
        response.raise_for_status()
        
        data = response.json()
        
        if 'errors' in data:
            logger.error(f'GitHub GraphQL error: {data["errors"]}')
            return None
        
        viewer = data.get('data', {}).get('viewer', {})
        contributions = viewer.get('contributionsCollection', {})
        total_contributions = contributions.get('contributionCalendar', {}).get('totalContributions', 0)
        
        result = {
            'total_contributions': total_contributions,
            'username': viewer.get('login'),
            'profile_url': f'https://github.com/{viewer.get("login")}'
        }
        
        # Cache for 1 hour
        cache.set(cache_key, result, 3600)
        return result
        
    except Exception as e:
        logger.error(f'Error fetching GitHub contributions: {str(e)}')
        return None

def home(request):
    from blog.models import Post

    # Fetch the last three published blog posts
    latest_posts = Post.objects.filter(status='published').order_by('-published_date')[:3]

    github_contributions = get_github_contributions()

    return render(request, 'website/home.html', {
        'latest_posts': latest_posts,
        'github_contributions': github_contributions,
    })


def contact(request):
    contact_status = None
    if request.method == 'POST':
        client_ip = get_client_ip(request)
        rate_limit_key = f'contact_form_attempts:{client_ip}'
        current_attempts = cache.get(rate_limit_key, 0)

        if current_attempts >= CONTACT_RATE_LIMIT:
            contact_status = 'rate_limited'
            contact_form = ContactForm(request.POST)
        else:
            cache.set(rate_limit_key, current_attempts + 1, CONTACT_RATE_LIMIT_WINDOW_SECONDS)
            contact_form = ContactForm(request.POST)
            if contact_form.is_valid():
                # If honeypot is tripped, stop here and avoid claiming the message was sent.
                if contact_form.cleaned_data.get('website'):
                    logger.warning(
                        'Blocked contact form submission via honeypot from IP %s with user agent %s',
                        client_ip,
                        request.META.get('HTTP_USER_AGENT', 'unknown'),
                    )
                    contact_status = 'blocked'
                else:
                    email_sent = send_contact_email_via_mailjet(contact_form.cleaned_data)
                    if email_sent:
                        contact_status = 'success'
                        contact_form = ContactForm()
                    else:
                        contact_status = 'error'
    else:
        contact_form = ContactForm()

    return render(request, 'website/contact.html', {
        'contact_form': contact_form,
        'contact_status': contact_status,
    })

@require_http_methods(["GET", "HEAD"])
def projects(request):
    """Redirect to portfolio projects page"""
    from django.shortcuts import redirect
    return redirect('portfolio:projects_list')