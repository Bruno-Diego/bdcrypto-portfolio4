from django.apps import AppConfig


class UpdaterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'updater'

    def ready(self):
        from updater.update import start
        start()
