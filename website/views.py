from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
import requests
import os
import logging

logger = logging.getLogger(__name__)

def get_latest_medium_article():
    """Fetch the latest article from Medium RSS feed"""
    try:
        medium_feed_url = 'https://medium.com/feed/@chrys0111'
        api_url = f'https://api.rss2json.com/v1/api.json?rss_url={medium_feed_url}'
        
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        if data.get('items') and len(data['items']) > 0:
            latest_item = data['items'][0]
            return {
                'title': latest_item.get('title'),
                'link': latest_item.get('link')
            }
    except Exception as e:
        logger.error(f'Error fetching Medium article: {str(e)}')
    
    return None

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
    latest_medium = get_latest_medium_article()
    github_contributions = get_github_contributions()
    
    return render(request, 'website/home.html', {
        'latest_medium': latest_medium,
        'github_contributions': github_contributions
    })

@require_http_methods(["GET", "HEAD"])
def projects(request):
    """Redirect to portfolio projects page"""
    from django.shortcuts import redirect
    return redirect('portfolio:projects_list')