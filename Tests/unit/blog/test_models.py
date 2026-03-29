from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Tag, Comment
from django.utils import timezone

class BlogModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.tag = Tag.objects.create(name='Django', slug='django')
        self.post = Post.objects.create(
            title='My First Post',
            slug='my-first-post',
            author=self.user,
            content='This is the content.',
            status='published'
        )
        self.post.tags.add(self.tag)

    def test_tag_creation(self):
        self.assertEqual(self.tag.name, 'Django')
        self.assertEqual(self.tag.slug, 'django')
        self.assertEqual(str(self.tag), 'Django')

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'My First Post')
        self.assertEqual(self.post.slug, 'my-first-post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.status, 'published')
        self.assertIn(self.tag, self.post.tags.all())
        self.assertEqual(str(self.post), 'My First Post')

    def test_comment_creation(self):
        comment = Comment.objects.create(
            post=self.post,
            name='John Doe',
            email='john@example.com',
            body='Nice post!',
            active=True
        )
        self.assertEqual(comment.post, self.post)
        self.assertEqual(comment.name, 'John Doe')
        self.assertTrue(comment.active)
        self.assertEqual(str(comment), 'Comment by John Doe on My First Post')
