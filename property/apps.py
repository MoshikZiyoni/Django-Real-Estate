from django.apps import AppConfig


class BooksConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField' ***maybe need to return
    name = 'property'
    def ready(self):
        from property.my_filters import intcomma
        from .import my_filters
