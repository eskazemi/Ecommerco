from django.contrib.auth import get_user_model
from django.http import HttpRequest
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

User = get_user_model()


# @skip("demonstarting skipping")
# class TestSkip(TestCase):
#     def test_skip_exmample(self):
#         pass

class TestViewResponse(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        Category.objects.create(name='mobile', slug='mobile')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Note11', created_by_id=1,
                                            slug='Note11', price='30.25', image='Note11')

    def test_url_allowed_hosts(self):
        """
        Test homepage response status
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        Test Product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['Note11']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        Test Category response status
        """
        response = self.c.get(reverse('store:category_list', args=['mobile']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>Home</title>', html)
