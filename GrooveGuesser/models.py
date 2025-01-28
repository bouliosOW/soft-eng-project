from django.db import models

# Create your models here.

class Account(models.Model):
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
    join_data = models.DateTimeField("Join Date")

    def __str__(self):
        return "User " + self.username
    
 
