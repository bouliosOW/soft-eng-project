from django.test import TestCase
from django.urls import reverse
from .models import Round, Song
from unittest.mock import patch

class GameViewTest(TestCase):
    def setUp(self):
        self.song_list = [
            Song(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path='/static/mp3s/LifeIsAHighwayTomCochrane.mp3'),
            Song(title="All Star", artist="Smash Mouth", year=1999, album="Astro Lounge", path='/static/mp3s/All-Star-Smash-Mouth.mp3'),
            Song(title="Everybody Wants to Rule the World", artist="Tears for Fears", year=1985, album="Songs from the Big Chair", path='/static/mp3s/Everybody-Wants-To-Rule-The-World-Tears-For-Fears.mp3'),
            Song(title="I'm Still Standing", artist="Elton John", year=1983, album="Too Low for Zero", path='/static/mp3s/Im-Still-Standing-Elton-John.mp3'),
            Song(title="Virtual Insanity", artist="Jamiroquai", year=1996, album="Travelling Without Moving", path='/static/mp3s/Virtual-Insanity-Jamiroquai.mp3')
        ]
        self.url = reverse('game')  

    @patch('random.choice')
    def test_song_randomizer(self, mock_random_song):
        mock_random_song.return_value = self.song_list[0]
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('song', response.context)

        song = response.context['song']
        self.assertEqual(song.title, self.song_list[0].title)
        self.assertEqual(song.artist, self.song_list[0].artist)
        self.assertEqual(song.year, self.song_list[0].year)
        self.assertEqual(song.path, self.song_list[0].path)



class GameViewTest(TestCase):
    def setUp(self):
        self.url = reverse('game') 

    def test_displaying_guess_responses(self):
        score = 1000  
        guesses = {
            'title': 'Life is a Highway',
            'artist': 'Tom Cochrane',
            'year': 1991
        }
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('score', response.context)

        self.assertContains(response, f'<p id="score">{score}</p>')
        self.assertContains(response, f'<p id="titleGuess">{guesses["title"]}</p>')
        self.assertContains(response, f'<p id="artistGuess">{guesses["artist"]}</p>')
        self.assertContains(response, f'<p id="yearGuess">{guesses["year"]}</p>')

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
        