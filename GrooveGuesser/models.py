from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    year = models.IntegerField()
    album = models.CharField(max_length=100)
    path = models.CharField(max_length=100)


Song.objects.create(title="Life is a Highway", artist="Tom Cochrane", year=1991, album="Mad Mad World", path="mp3s/LifeIsAHighwayTomCochrane.mp3")

# Create your models here.

# class Account(models.Model):
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=20)
#     join_date = models.DateTimeField("Join Date")

#     def __str__(self):
#         return "User " + self.username


# class Leaderboard(models.Model):
#     player = models.ForeignKey(Account, on_delete=models.CASCADE)
    
'''
    IMPORTANT! -----------------------

    After making any change to this file, run the following commands:
        python manage.py makemigrations
        python manage.py migrate
    The first will create the migrations to update the database with all changes
    The second will actually update the database

    Without both, no changes made will work
 '''
