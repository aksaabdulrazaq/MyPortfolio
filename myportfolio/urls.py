from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django_distill import distill_path

from .views import home

urlpatterns = [
    path("admin/", admin.site.urls),
    # distill_path makes the homepage exportable as a static index.html
    distill_path("", home, name="home", distill_func=lambda: None),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
