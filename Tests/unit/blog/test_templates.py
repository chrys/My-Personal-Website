from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from blog.models import Post, Tag

class BlogTemplateTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.tag = Tag.objects.create(name='Python', slug='python')
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Content here.',
            status='published'
        )
        self.post.tags.add(self.tag)

    def test_post_list_template_context(self):
        response = self.client.get(reverse('blog:post_list'))
        self.assertIn('posts', response.context)
        self.assertIn('tag_cloud', response.context)
        self.assertTemplateUsed(response, 'blog/post_list.html')
        self.assertContains(response, 'Tag Cloud')
        self.assertContains(response, 'data-tag-name="Python"')

    def test_post_detail_template_context(self):
        response = self.client.get(reverse('blog:post_detail', args=['test-post']))
        self.assertIn('post', response.context)
        self.assertIn('comments', response.context)
        self.assertIn('comment_form', response.context)
        self.assertTemplateUsed(response, 'blog/post_detail.html')
