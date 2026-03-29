import os
import glob
import django
from bs4 import BeautifulSoup
from django.utils.text import slugify
from django.utils import timezone
from datetime import datetime

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fasolaki2.settings.base')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post, Tag

def migrate_posts():
    # 1. Ensure user 'chrys' exists
    author, created = User.objects.get_or_create(
        username='chrys',
        defaults={'email': 'zampas@gmail.com', 'is_staff': True}
    )
    if created:
        author.set_password('temporary_password123')
        author.save()
        print(f"Created user: {author.username}")

    # 2. Ensure tag 'medium' exists
    medium_tag, created = Tag.objects.get_or_create(name='medium', slug='medium')
    if created:
        print("Created tag: medium")

    # 3. Path to old posts
    posts_path = 'logs/old-posts/*.html'
    files = glob.glob(posts_path)
    print(f"Found {len(files)} posts to migrate.")

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, 'html.parser')

            # Extract fields
            # - Title: <h1 class="p-name">
            title_tag = soup.find('h1', class_='p-name')
            if not title_tag:
                # Fallback to <title>
                title_tag = soup.find('title')
            
            title = title_tag.get_text().strip() if title_tag else "Untitled"
            
            # - Published date: <time class="dt-published" datetime="...">
            time_tag = soup.find('time', class_='dt-published')
            if time_tag and time_tag.has_attr('datetime'):
                # Format: 2020-05-15T19:18:01.919Z
                dt_str = time_tag['datetime'].replace('Z', '+00:00')
                published_date = datetime.fromisoformat(dt_str)
            else:
                published_date = timezone.now()

            # - Content: <section data-field="body" class="e-content">
            content_section = soup.find('section', {'data-field': 'body', 'class': 'e-content'})
            if content_section:
                # Get the HTML content within the section to keep formatting
                content = "".join([str(c) for c in content_section.contents]).strip()
            else:
                content = "Content not found."

            # - Slug: create it using title
            slug = slugify(title)
            
            # Check for slug duplicates and append suffix if needed
            original_slug = slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{original_slug}-{counter}"
                counter += 1

            # 4. Create Post
            post = Post.objects.create(
                title=title,
                slug=slug,
                author=author,
                content=content,
                published_date=published_date,
                status='published'
            )
            post.tags.add(medium_tag)
            print(f"Migrated: '{title}' [{slug}]")

if __name__ == "__main__":
    migrate_posts()
