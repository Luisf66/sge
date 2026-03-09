from django.apps import AppConfig


class OutflowsConfig(AppConfig):
    name = 'outflows'

    def ready(self):
        import outflows.signals