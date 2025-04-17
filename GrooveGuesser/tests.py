from django.test import TestCase
from django.urls import reverse
from .models import Round, Song

# Create your tests here.

class MainSitesTests(TestCase):

    def test_main_pages(self):
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'GrooveGuesser.html')
        self.assertContains(response, "a randomly generated song guessing game!")

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
        self.assertContains(response, "GrooveGuesser is currently in development")

        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'leaderboard.html')
        self.assertContains(response, "Leaderboard")

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
    

    def test_Song_objects(self):
        
        testSong = Song(
            title="Test Song", 
            artist="Chris Haynes", 
            year=2025, 
            album="CSC 3400: Software Engineering", 
            path='/static/mp3s/LifeIsAHighwayTomCochrane.mp3', 
            category="Irish Jig"
        )

        self.assertEqual(testSong.title, "Test Song")
        self.assertEqual(testSong.artist, "Chris Haynes")
        self.assertEqual(testSong.year, 2025)
        self.assertEqual(testSong.album, "CSC 3400: Software Engineering")
        self.assertEqual(testSong.path, '/static/mp3s/LifeIsAHighwayTomCochrane.mp3')
        self.assertEqual(testSong.category, "Irish Jig")

    
    def test_Round_objects(self):
        
        testRound = Round(
            player="Chris",
            score=100
        )

        self.assertEqual(testRound.player, "Chris")
        self.assertEqual(testRound.score, 100)

        testRound.save()

        find = Round.objects.filter(player="Chris")
        self.assertEqual(find[0].player, "Chris")
        self.assertEqual(find[0].score, 100)
        