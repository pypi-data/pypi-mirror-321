from django.apps import AppConfig

class CustomersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shared_models.customers'
    verbose_name = 'Customers'
    
    def ready(self):
        try:
            import shared_models.customers.signals  # noqa
        except ImportError:
            pass 