from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from .models import Account

# Create your tests here.

# TestCase is better for Database stuff and SimpleTestCase is better for urls or views without database access
# One test / test case is one function testing one functionality (see notes from class on CANVAS)
# Adding anything to the database is 

class AccountModelTests(TestCase):

    def test_Account_create(self):
        test_account = Account(username="testName", password="testPassword")
        self.assertEqual(test_account.username, "testName")
        self.assertEqual(test_account.password, "testPassword")

    
    def test_Account_add_delete(self):
        test_account = Account(username="testName", password="testPassword")
        test_account.save()
        self.assertTrue(Account.objects.filter(pk=test_account.pk).exists())
        test_account.delete()
        self.assertFalse(Account.objects.filter(pk=test_account.pk).exists())


class UserSitesTests(TestCase):

    def test_user_websites(self):

        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')
        self.assertContains(response, "Already Have an Account?")

        response = self.client.get(reverse('user.login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        self.assertContains(response, "Haven't Made an Account Yet?")

        response = self.client.get(reverse('user.userHome'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/userHome.html')
        self.assertContains(response, "Dashboard")

    def test_signup(self):

        response = self.client.post(reverse('user.get_new_user'), {
            'username': "username",
            'password': "password"
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        response = self.client.post(reverse('user.get_new_user'), {
            'username': "username",
            'password': "1234567890"
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {"success": False, "message": "This username is already taken."})
    
    def test_login(self):

        response = self.client.post(reverse('user.get_new_user'), {
            'username': "username",
            'password': "password"
        })

        response = self.client.post(reverse('user.user_enter'), {
            'username': "username",
            'password': "password"
        })
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        response = self.client.post(reverse('user.user_enter'), {
            'username': "wrongUsername",
            'password': "wrongPassword"
        })
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'success': False, 'message': "This account does not exist. Please try a different username or password."})

    def test_logout(self):

        response = self.client.post(reverse('user.get_new_user'), {
            'username': "username",
            'password': "password"
        })

        response = self.client.post(reverse('user.user_enter'), {
            'username': "username",
            'password': "password"
        })

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse('user.login'))

        follow_response = self.client.get(response.url)
        self.assertEqual(follow_response.status_code, 200)
        self.assertTemplateUsed(follow_response, 'user/login.html')
        self.assertContains(follow_response, "Haven't Made an Account Yet?")


class GameTests(TestCase):

    def test_game_pregame_pages(self):

        response = self.client.get(reverse('pregame'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pregame.html')
        self.assertContains(response, "Choose your preferred music category before starting the game:")

        response = self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'game.html')
        self.assertContains(response, "Guess that Groove!")