from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_project.users'   # ✅ FIXED

    def ready(self):
        from . import signals   # ✅ BEST PRACTICE