from campagne.views import meldr_redirect, meldr_qr_event
from django.contrib import admin
from django.urls import path
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("redirect/", meldr_redirect, name="meldr_redirect"),
    path(f"{settings.UNPREDICTABLE_SLUG}", meldr_qr_event, name="meldr_qr_event"),
]
