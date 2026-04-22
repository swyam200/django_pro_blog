from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name ='django_project.blog'

    def ready(self):
       import users.signals
