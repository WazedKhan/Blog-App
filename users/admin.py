from django.contrib import admin
from .models import Profile, Account
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'Accounts'
    
class CustomeUser(UserAdmin):
    inlines = (AccountInLine, )
    
admin.site.unregister(User)
admin.site.register(User, CustomeUser)

admin.site.register(Account)