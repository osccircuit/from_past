from django.contrib import admin
from main.models import Stack

# Register your models here.
@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    '''Class to registration Stack model in Admin panel'''
    pass
