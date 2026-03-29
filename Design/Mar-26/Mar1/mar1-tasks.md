# Development Tasks: fasolaki.com Blog

This task list strictly adheres to the specifications outlined in `mar1-specs.md`. All unit tests are designated to be placed under `Tests/unit/`.

## Phase 1: Environment & Setup
- [ ] **Task 1.1 - App Creation**: Run `python manage.py startapp blog` to create the new Django app.
- [ ] **Task 1.2 - App Registration**: Add `'blog'` to the `INSTALLED_APPS` list in the main `settings.py`.
- [ ] **Task 1.3 - Dependencies**: Install a WYSIWYG editor package (e.g., `django-tinymce` or `django-ckeditor`) and update `requirements.txt`.
- [ ] **Task 1.4 - Test Structure**: Create the testing directory structure `Tests/unit/blog/` and ensure it has an `__init__.py`.

## Phase 2: Data Models (with Unit Tests)
- [ ] **Task 2.1 - Tag Model**: Implement the `Tag` model with `name` and `slug` fields.
- [ ] **Task 2.2 - Post Model**: Implement the `Post` model including WYSIWYG support for `content`, and relations `author` (User) and `tags` (Tag).
- [ ] **Task 2.3 - Comment Model**: Implement the `Comment` model, linking to `post` (Post), with `active` boolean for moderation.
- [ ] **Task 2.4 - Migrations**: Create and apply database migrations (`makemigrations blog` and `migrate`).
- [ ] **Task 2.5 - Model Tests**: Write unit tests in `Tests/unit/blog/test_models.py`
  - *Verify slug generation (if auto-generating).*
  - *Verify field validation and defaults (e.g., status defaults, timestamp auto-generation).*
  - *Verify relationships (ForeignKey and ManyToMany).*

## Phase 3: Admin Interface & Configuration
- [ ] **Task 3.1 - Register Models**: Register `Post`, `Comment`, and `Tag` inside `blog/admin.py`.
- [ ] **Task 3.2 - Configure Editor**: Ensure the WYSIWYG editor loads correctly for the `content` field in the Post Admin panel.
- [ ] **Task 3.3 - Admin Customization**: Add list displays, search fields, and filtering to make comment moderation easy (e.g., filtering `active=False`).
- [ ] **Task 3.4 - Admin Tests**: Write unit tests in `Tests/unit/blog/test_admin.py`
  - *Ensure Admin classes list the correct fields and load properly without errors.*

## Phase 4: Views & Routing (with Unit Tests)
- [ ] **Task 4.1 - URL Configuration**: Create `blog/urls.py` and map the three paths: `/blog/`, `/blog/<slug>/`, and `/blog/tag/<slug>/`. Include these in the main project `urls.py`.
- [ ] **Task 4.2 - Index View**: Implement the view for the main Blog Index, fetching published posts and supporting pagination.
- [ ] **Task 4.3 - Detail & Comment View**: Implement the view for Post Details. This should show the content, related tags, active comments, and handle POST requests for new comments.
- [ ] **Task 4.4 - Tag Filter View**: Implement the view for listing posts filtered by a specific tag.
- [ ] **Task 4.5 - View Tests**: Write unit tests in `Tests/unit/blog/test_views.py`
  - *Verify HTTP 200 responses on all routes for valid data.*
  - *Verify HTTP 404 responses for non-existent slugs/tags.*
  - *Ensure unpublished/draft posts are not returned in the views.*
  - *Validate successful and failing form submissions for comments.*

## Phase 5: Templates & UI
- [ ] **Task 5.1 - Index Template**: Create `blog/post_list.html` to display the post feed.
- [ ] **Task 5.2 - Detail Template**: Create `blog/post_detail.html`. Use the `|safe` flag (or appropriate tool) to properly render WYSIWYG `content` output.
- [ ] **Task 5.3 - Tag Template**: Create `blog/post_by_tag.html`.
- [ ] **Task 5.4 - Comment UI**: Add the comment submission form and display existing comments cleanly within `post_detail.html`.
- [ ] **Task 5.5 - Template Tests**: Write unit tests in `Tests/unit/blog/test_templates.py`
  - *Verify template contexts contain the required variables (posts, tags, comments, forms).*

## Phase 6: Server Configuration & Deployment
- [ ] **Task 6.1 - Nginx Media Routes**: Inspect `config_files/fasolaki.com` to ensure Nginx serves `/media/` paths properly if WYSIWYG editors upload images locally.
- [ ] **Task 6.2 - Static Files**: Run `python manage.py collectstatic` so the production environment correctly serves static assets for the WYSIWYG admin plugins.
- [ ] **Task 6.3 - Validation**: Verify that `config_files/fasolaki.service` and `config_files/fasolaki.socket` configurations require no further modifications.
- [ ] **Task 6.4 - Deployment**: Implement instructions for restarting Gunicorn/Nginx.
