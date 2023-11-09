"""placehodler"""

'''
from django.test import TestCase
from ..models import Puppy


class PuppyTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')
        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_muffin = Puppy.objects.get(name='Muffin')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Bull Dog breed.")
        self.assertEqual(
            puppy_muffin.get_breed(), "Muffin belongs to Gradane breed.")
'''

# class GetAllPuppiesTest(TestCase):
#     """ Test module for GET all puppies API """
#
#     def setUp(self):
#         Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')
#         Puppy.objects.create(
#             name='Muffin', age=1, breed='Gradane', color='Brown')
#         Puppy.objects.create(
#             name='Rambo', age=2, breed='Labrador', color='Black')
#         Puppy.objects.create(
#             name='Ricky', age=6, breed='Labrador', color='Brown')
#
#     def test_get_all_puppies(self):
#         # get API response
#         response = client.get(reverse('get_post_puppies'))
#         # get data from db
#         puppies = Puppy.objects.all()
#         serializer = PuppySerializer(puppies, many=True)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

# class GetSinglePuppyTest(TestCase):
#     """ Test module for GET single puppy API """
#
#     def setUp(self):
#         self.casper = Puppy.objects.create(
#             name='Casper', age=3, breed='Bull Dog', color='Black')
#         self.muffin = Puppy.objects.create(
#             name='Muffin', age=1, breed='Gradane', color='Brown')
#         self.rambo = Puppy.objects.create(
#             name='Rambo', age=2, breed='Labrador', color='Black')
#         self.ricky = Puppy.objects.create(
#             name='Ricky', age=6, breed='Labrador', color='Brown')
#
#     def test_get_valid_single_puppy(self):
#         response = client.get(
#             reverse('get_delete_update_puppy', kwargs={'pk': self.rambo.pk}))
#         puppy = Puppy.objects.get(pk=self.rambo.pk)
#         serializer = PuppySerializer(puppy)
#         self.assertEqual(response.data, serializer.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#
#     def test_get_invalid_single_puppy(self):
#         response = client.get(
#             reverse('get_delete_update_puppy', kwargs={'pk': 30}))
#         self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


# import pytest
#
# from django.urls import reverse
#
# from articles.models import Article
# from articles.serializers import ArticleSerializer
#
#
# @pytest.mark.django_db
# def test_list_articles(client):
#     url = reverse('list-articles')
#     response = client.get(url)
#
#     articles = Article.objects.all()
#     expected_data = ArticleSerializer(articles, many=True).data
#
#     assert response.status_code == 200
#     assert response.data == expected_dat