from django.test import TestCase, SimpleTestCase
from django.urls import reverse

# Create your tests here.
class TestBlogApp(TestCase):
    # Test for status code
    def test_homepage(self):
        response = self.client.get(reverse('blog-homepage'))
        self.assertEqual(response.status_code, 200)

    def test_aboutpage(self):
        response = self.client.get(reverse('blog-aboutpage'))
        self.assertEqual(response.status_code, 200)

    # Test for valid Template.
    def test_homepage_Template(self):
        response = self.client.get(reverse('blog-homepage'))
        self.assertTemplateUsed(response, 'home.html')

    def test_aboutpage_Template(self):
        response = self.client.get(reverse('blog-aboutpage'))
        self.assertTemplateUsed(response, 'about.html')
