from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from .models import Song

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

