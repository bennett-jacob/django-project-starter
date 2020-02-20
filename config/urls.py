from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView

urlpatterns = [
    # In settings.py we set APPEND_SLASH=False, which currently breaks some
    # admin functionality. To fix this, we force admin to have a trailing
    # slash.
    path("admin/", admin.site.urls),
    path("admin", RedirectView.as_view(url="admin/")),
]
