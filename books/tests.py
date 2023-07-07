from django.test import TestCase
from .models import Book
from django.contrib.auth import get_user_model
from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
# from rest_framework.test import APIRequestFactory
# Create your tests here.

# factory = APIRequestFactory()

class TestBook(APITestCase):
    
    @classmethod
    def setUpTestData(cls):
        cls.testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        cls.testuser1.save()

        cls.test_book = Book.objects.create(title='title',auther_name='auther', release_date="1990-01-01",
                                        img_url='https://img',description='description',user=cls.testuser1)
        cls.test_book.save()

    def test_get_single_book(self):
        
        url = reverse('book_detail', kwargs={'pk': 1})  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'title')
        self.assertEqual(response.data['auther_name'], 'auther')
       
        
    def test_get_book(self):
        url = reverse('book_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
     
        
    # def test_create_book(self):
    #     url = reverse('book_list')
        
    #     data = {
    #         'title': 'Example Title',
    #         'author_name': 'Example Author',
    #         'release_date': '2023-06-19',
    #         'description': 'Example Description',
    #         'img_url': 'https://example.com/image.jpg',
    #         'user': self.testuser1.id
    #     }
        
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Book.objects.count(), 1)
    #     self.assertEqual(Book.objects.get().title, 'Example Title')   
    
        
    
    # def test_update_book(self):
    #     url = reverse('book_detail', args=[self.test_book.id])
        
    #     data = {
    #         'title': 'Updated Title',
    #         'author_name': 'Updated Author',
    #         'release_date': '2023-06-19',
    #         'img_url': 'https://example.com/updated_image.jpg',
    #         'description': 'Updated Description',
    #         'user': self.testuser1.id
    #     }
        
    #     response = self.client.put(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.test_book.refresh_from_db()
    #     self.assertEqual(self.test_book.title, 'Updated Title')
        
        
        
    def test_delete_book(self):
        obj = Book.objects.first()
        url = reverse('book_detail', kwargs={'pk': obj.pk})  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(pk=obj.pk).exists())