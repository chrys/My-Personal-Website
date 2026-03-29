import os
import django
from django.utils.text import slugify

from anyascii import anyascii

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fasolaki2.settings.base')
django.setup()

from blog.models import Post

# First find any that have non-ascii characters (this might catch the Greek one)
for post in Post.objects.all():
    # Attempt to slugify normally with transliteration
    transl_title = anyascii(post.title)
    new_slug = slugify(transl_title)
    
    # If the slug was changed (e.g. from the Greek one), or was empty
    if not post.slug or post.slug != new_slug:
        if not new_slug or Post.objects.filter(slug=new_slug).exclude(id=post.id).exists():
           new_slug = f'{new_slug}-{post.id}' if new_slug else f'post-{post.id}'
        
        print(f"Updating: '{post.title}' -> '{new_slug}'")
        post.slug = new_slug
        post.save()
