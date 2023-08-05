from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    # create a user to run the tests
    def setUp(self):
        User.objects.create_user(username='terry', password='terrythetester')

    def test_can_list_posts(self):
        # creating a post as the user
        terry = User.objects.get(username='terry')
        Post.objects.create(owner=terry, title='terrys title')
        # get request the post
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # check its data and length
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        # must log in to test this works
        self.client.login(username='terry', password='terrythetester')
        # making a post request
        response = self.client.post('/posts/', {'title': 'a title'})
        # count the posts
        count = Post.objects.count()
        # check there is just one
        self.assertEqual(count, 1)
        # assert response code
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        # attempt to create post
        response = self.client.post('/posts/', {'title': 'a title'})
        # check it is a forbidden request
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
