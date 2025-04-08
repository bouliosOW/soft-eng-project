from django.test import TestCase
from django.urls import reverse

# Create your tests here.

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