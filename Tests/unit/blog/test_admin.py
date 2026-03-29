from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from blog.models import Post, Tag, Comment
from blog.admin import PostAdmin, TagAdmin, CommentAdmin

class MockRequest:
    pass

class BlogAdminTest(TestCase):
    def setUp(self):
        self.site = AdminSite()

    def test_tag_admin_registration(self):
        tag_admin = TagAdmin(Tag, self.site)
        self.assertEqual(tag_admin.list_display, ('name', 'slug'))
        self.assertEqual(tag_admin.prepopulated_fields, {'slug': ('name',)})

    def test_post_admin_registration(self):
        post_admin = PostAdmin(Post, self.site)
        self.assertIn('title', post_admin.list_display)
        self.assertIn('status', post_admin.list_display)
        self.assertEqual(post_admin.prepopulated_fields, {'slug': ('title',)})

    def test_comment_admin_registration(self):
        comment_admin = CommentAdmin(Comment, self.site)
        self.assertIn('name', comment_admin.list_display)
        self.assertIn('active', comment_admin.list_display)
