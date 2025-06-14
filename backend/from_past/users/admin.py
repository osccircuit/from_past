from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import User
from letter.models import Letter

class LetterItemInline(admin.TabularInline):
    model = Letter
    extra = 1

@admin.register(User)
class AdminUser(admin.ModelAdmin):
    inlines = [LetterItemInline]