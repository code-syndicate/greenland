from django.apps import AppConfig


class BankingConfig(AppConfig):
    name = 'banking'

    def ready(self):
        from .import signals
