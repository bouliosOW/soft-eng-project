from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    join_date = models.DateTimeField("Join Date", auto_now_add=True)

    def __str__(self):
        return "User " + self.username


class Leaderboard(models.Model):
    player = models.ForeignKey(Account, on_delete=models.CASCADE)


'''
    {% for account in accounts %}
            <p>Username: {{ account.username }}</p>
            <p>Password: {{ account.password }}</p>
            <p>Joined: {{ account.join_date }}</p>
        {% endfor %}

        was used in login for testing, now am working on some things
'''

    
'''
    IMPORTANT! -----------------------

    After making any change to this file, run the following commands:
        python manage.py makemigrations
        python manage.py migrate
    The first will create the migrations to update the database with all changes
    The second will actually update the database

    Without both, no changes made will work
 '''

'''
    IMPORTANT!!! -------------------------------------------
    
    Since our file uses sqlite3, each database may or may not be specific to individual users.
    That means that pushing the files to Github WILL NOT transfer any data we have saved in our
    databse in our own work.

    THEREFORE, we will either have to use seperate admin accounts OR find a way to pre-populate the
    database with a shared admin account. I am looking into a way to do this, but we can discuss this in/after class
    on Thursday.

    NOTICE that this problem will apply to all information stored in the database. Anything not
    preset will not be saved, even with migrations. 

    TO ENSURE ALL MIGRATIONS ARE ADDED, USE:
        python manage.py migrate
    AFTER EVERY PULL TO ENSURE ALL OF OUR DATABASES WILL HAVE THE SAME TABLES, FIELDS, ETC.
    THIS WILL NOT POPULATE TABLES WITH DATA, BUT IT WILL ENSURE 
    THAT ALL TABLES ARE SAME FOR ALL PARTNERS IN THIS PROJECT


    ADDITIONALLY,

    If you are having any troubles with the database, models, or the admin page's use of them,
    then you may be having problems with migrations.
    See the comment in \grooveguesser\models.py for help

'''