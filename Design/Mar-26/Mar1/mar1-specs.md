# Product Requirements Document: Django Blog for fasolaki.com

## 1. Overview
The objective of this project is to implement a fully functional blog section for the personal website `www.fasolaki.com` using Django. The blog will allow the publication of posts, categorization via tags, and reader engagement through comments.

## 2. Scope
- Create a new Django app (e.g., `blog`) to handle blog functionality.
- Define data models for Posts, Comments, and Tags.
- Expose the blog at the `/blog/` URL trajectory.
- Ensure the web server (Nginx) and application server (Gunicorn) configurations support the new app (static files/media).
- Develop templates to display the blog index, individual posts, and comment forms.

## 3. Data Models (Entities & Fields)

### 3.1 Post
Represents an individual blog entry.
- `title` (CharField): The title of the blog post.
- `slug` (SlugField): URL-friendly string for the post, automatically generated from the title (e.g., `my-first-post`). Unique.
- `author` (ForeignKey to User): The author of the post.
- `content` (RichTextField or equivalent): The main body of the post, supporting WYSIWYG formatting (e.g. using TinyMCE, CKEditor, or a similar package).
- `published_date` (DateTimeField): The date and time when the post is published.
- `created_date` (DateTimeField): Auto-set when the post is created.
- `updated_date` (DateTimeField): Auto-set whenever the post is modified.
- `status` (CharField/IntegerChoices): Draft or Published state.
- `tags` (ManyToManyField): Relation to the Tag model.

### 3.2 Comment
Represents a reader's comment on a specific post.
- `post` (ForeignKey to Post): The post this comment belongs to (many-to-one relationship).
- `name` (CharField): The name of the commenter.
- `email` (EmailField): The email address of the commenter.
- `body` (TextField): The content of the comment.
- `created_date` (DateTimeField): Auto-set when the comment is submitted.
- `active` (BooleanField): A moderation flag. Set to `True` by default, but allows admins to hide inappropriate comments.

### 3.3 Tag
Used to categorize posts.
- `name` (CharField): The name of the tag (e.g., "Django", "Python", "Life").
- `slug` (SlugField): URL-friendly version of the tag name. Unique.

## 4. URLs & Routing
The blog will be nested under the `/blog/` path.
- **Blog Index**: `/blog/` - Displays a paginated list of published posts.
- **Post Detail**: `/blog/<slug>/` - Displays the full content of a specific post, its associated tags, and comments.
- **Tag Filter**: `/blog/tag/<slug>/` - Displays a list of posts associated with a specific tag.

## 5. Server Configuration & Deployment
Dependencies and configurations already exist for the main site:
- **Nginx Config**: `config_files/fasolaki.com`
- **Gunicorn Service**: `config_files/fasolaki.service`
- **Gunicorn Socket**: `config_files/fasolaki.socket`
*Action Items:* 
- Verify that Nginx is configured to serve any new static or media (e.g. upload images) directories required by the blog app.
- Apply database migrations and restart Gunicorn/Nginx upon deployment.

## 6. Future Enhancements (V2)
- Comment moderation dashboard.
- RSS Feeds.
