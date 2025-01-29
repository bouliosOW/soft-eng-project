from django.contrib import admin
from .models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    fields = [
        "username", "password", "join_date",
    ]
    list_display = ["username", "password", "join_date"]

admin.site.register(Account, AccountAdmin)

# For Anderson's ease of remembering:
# admin username = admin
# admin email = admin@mail.com
# admin password = password
#others can use this data when creating their own admins for simplicity, 
#but each admin account will be separate, and will only work on our own machines

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

