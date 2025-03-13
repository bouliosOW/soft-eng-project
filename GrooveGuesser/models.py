from django.db import models
from user.models import Account

# Create your models here.

# class Account(models.Model):
#     username = models.CharField(max_length=15)
#     password = models.CharField(max_length=20)
#     join_date = models.DateTimeField("Join Date")

#     def __str__(self):
#         return "User " + self.username


# class Leaderboard(models.Model):
#     player = models.ForeignKey(Account, on_delete=models.CASCADE)


class Round(models.Model):
    player = models.CharField(max_length=10)
    score = models.BigIntegerField(blank=0)
    
'''
    IMPORTANT! -----------------------

    After making any change to this file, run the following commands:
        python manage.py makemigrations
        python manage.py migrate
    The first will create the migrations to update the database with all changes
    The second will actually update the database

    Without both, no changes made will work
 '''
