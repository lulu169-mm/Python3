# 固定的，不用动
from django.apps import AppConfig


class App01Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app01'
