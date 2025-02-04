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