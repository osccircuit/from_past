from django.apps import AppConfig


class MainConfig(AppConfig):
    '''Config main app'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Главная'
