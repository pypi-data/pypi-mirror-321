"""App Configuration"""

# Django
from django.apps import AppConfig

# ProdOPS
# AA ProdOPS App
from ProdOPS import __version__


class ProdOPSConfig(AppConfig):
    """App Config"""

    name = "ProdOPS"
    label = "ProdOPS"
    verbose_name = f"ProdOPS App v{__version__}"
