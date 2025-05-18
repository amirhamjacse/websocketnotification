from django.apps import AppConfig


class WesockappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wesockapp'

    def ready(self):
        import wesockapp.signals  # noqa