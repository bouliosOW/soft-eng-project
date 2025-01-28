from django.contrib import admin
from .models import Account

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    fields = [
        "username", "password",
    ]

admin.site.register(Account, AccountAdmin)