from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Tag, Comment

class BlogViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.tag = Tag.objects.create(name='Django', slug='django')
        self.published_post = Post.objects.create(
            title='Published Post',
            slug='published-post',
            author=self.user,
            content='Content here.',
            status='published'
        )
        self.published_post.tags.add(self.tag)
        self.draft_post = Post.objects.create(
            title='Draft Post',
            slug='draft-post',
            author=self.user,
            content='Draft content.',
            status='draft'
        )

    def test_post_list_view(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Post')
        self.assertNotContains(response, 'Draft Post')

    def test_post_list_by_tag_view(self):
        response = self.client.get(reverse('blog:post_list_by_tag', args=['django']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Post')

    def test_post_detail_view(self):
        # Test published post
        response = self.client.get(reverse('blog:post_detail', args=['published-post']))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Published Post')

        # Test draft post (should be 404)
        response = self.client.get(reverse('blog:post_detail', args=['draft-post']))
        self.assertEqual(response.status_code, 404)

    def test_comment_submission(self):
        response = self.client.post(reverse('blog:post_detail', args=['published-post']), {
            'name': 'Commenter',
            'email': 'commenter@example.com',
            'body': 'This is a test comment.'
        })
        # After success it redirects
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.filter(post=self.published_post).count(), 1)
