from django.apps import AppConfig


class DrfserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drfservice'

    def ready(self):
        import drfservice.signals
