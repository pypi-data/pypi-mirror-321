"""App URLs"""

# Django
from django.urls import path

# ProdOPS
# AA ProdOPS App
from ProdOPS import views

app_name: str = "ProdOPS"

urlpatterns = [
    path("", views.index, name="index"),
]
