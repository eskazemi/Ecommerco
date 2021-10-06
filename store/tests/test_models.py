from django.contrib.auth import get_user_model
from django.test import TestCase

from store.models import Category, Product

User = get_user_model()


class TestCategoriesModel(TestCase):

    def setUp(self) -> None:
        self.data1 = Category.objects.create(name='mobile', slug='mobile')

    def test_category_model_entry(self):
        """
        Test category model data insertion/types/filed attribute

        """

        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_str(self):
        """
        Test category model Category name

        """

        data = self.data1
        self.assertEqual(str(data), 'mobile')


class TestProductsModel(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='mobile', slug='mobile')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='Note11', created_by_id=1,
                                            slug='Note11', price='30.25', image='Note11')

    def test_product_model_entry(self):
        """
        Test product model data insertion/types/filed attribute

        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Note11')
