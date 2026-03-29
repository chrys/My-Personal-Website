# Development Tasks: fasolaki.com Blog

This task list strictly adheres to the specifications outlined in `mar1-specs.md`. All unit tests are designated to be placed under `Tests/unit/`.

## Phase 1: Environment & Setup
- [x] **Task 1.1 - App Creation**: Run `python manage.py startapp blog` to create the new Django app.
- [x] **Task 1.2 - App Registration**: Add `'blog'` to the `INSTALLED_APPS` list in the main `settings.py`.
- [x] **Task 1.3 - Dependencies**: Install a WYSIWYG editor package (e.g., `django-ckeditor`) and update `requirements.txt`.
- [x] **Task 1.4 - Test Structure**: Create the testing directory structure `Tests/unit/blog/` and ensure it has an `__init__.py`.

## Phase 2: Data Models (with Unit Tests)
- [x] **Task 2.1 - Tag Model**: Implement the `Tag` model with `name` and `slug` fields.
- [x] **Task 2.2 - Post Model**: Implement the `Post` model including WYSIWYG support for `content`, and relations `author` (User) and `tags` (Tag).
- [x] **Task 2.3 - Comment Model**: Implement the `Comment` model, linking to `post` (Post), with `active` boolean for moderation.
- [x] **Task 2.4 - Migrations**: Create and apply database migrations (`makemigrations blog` and `migrate`).
- [x] **Task 2.5 - Model Tests**: Write unit tests in `Tests/unit/blog/test_models.py`

## Phase 3: Admin Interface & Configuration
- [x] **Task 3.1 - Register Models**: Register `Post`, `Comment`, and `Tag` inside `blog/admin.py`.
- [x] **Task 3.2 - Configure Editor**: Ensure the WYSIWYG editor loads correctly for the `content` field in the Post Admin panel.
- [x] **Task 3.3 - Admin Customization**: Add list displays, search fields, and filtering to make comment moderation easy (e.g., filtering `active=False`).
- [x] **Task 3.4 - Admin Tests**: Write unit tests in `Tests/unit/blog/test_admin.py`

## Phase 4: Views & Routing (with Unit Tests)
- [x] **Task 4.1 - URL Configuration**: Create `blog/urls.py` and map the three paths: `/blog/`, `/blog/<slug>/`, and `/blog/tag/<slug>/`. Include these in the main project `urls.py`.
- [x] **Task 4.2 - Index View**: Implement the view for the main Blog Index, fetching published posts and supporting pagination.
- [x] **Task 4.3 - Detail & Comment View**: Implement the view for Post Details. This should show the content, related tags, active comments, and handle POST requests for new comments.
- [x] **Task 4.4 - Tag Filter View**: Implement the view for listing posts filtered by a specific tag.
- [x] **Task 4.5 - View Tests**: Write unit tests in `Tests/unit/blog/test_views.py`

## Phase 5: Templates & UI
- [x] **Task 5.1 - Index Template**: Create `blog/post_list.html` to display the post feed.
- [x] **Task 5.2 - Detail Template**: Create `blog/post_detail.html`. Use the `|safe` flag (or appropriate tool) to properly render WYSIWYG `content` output.
- [x] **Task 5.3 - Tag Template**: Create `blog/post_by_tag.html`.
- [x] **Task 5.4 - Comment UI**: Add the comment submission form and display existing comments cleanly within `post_detail.html`.
- [x] **Task 5.5 - Template Tests**: Write unit tests in `Tests/unit/blog/test_templates.py`

## Phase 6: Server Configuration & Deployment
- [x] **Task 6.1 - Nginx Media Routes**: Inspect `config_files/fasolaki.com` to ensure Nginx serves `/media/` paths properly if WYSIWYG editors upload images locally.
- [x] **Task 6.2 - Static Files**: Run `python manage.py collectstatic` so the production environment correctly serves static assets for the WYSIWYG admin plugins.
- [x] **Task 6.3 - Validation**: Verify that `config_files/fasolaki.service` and `config_files/fasolaki.socket` configurations require no further modifications.
- [x] **Task 6.4 - Deployment**: Implement instructions for restarting Gunicorn/Nginx.
