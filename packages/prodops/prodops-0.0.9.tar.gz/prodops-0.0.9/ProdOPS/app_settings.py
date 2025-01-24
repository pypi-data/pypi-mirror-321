"""App Settings"""

# Django
from django.conf import settings

# put your app settings here


ProdOPS_SETTING_ONE = getattr(settings, "ProdOPS_SETTING_ONE", None)
