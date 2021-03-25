from django.urls import re_path
from rest_framework.routers import DefaultRouter

from short_url import api_views, views

router = DefaultRouter()
router.register(r"shorten", api_views.UrlViewSet, basename="url")
urlpatterns = router.urls + [
    re_path(
        r"^(?P<short_code>[A-Za-z0-9_]{6})/stats/$",
        api_views.Stats.as_view(),
        name="stats",
    ),
    re_path(
        r"^(?P<short_code>[A-Za-z0-9_]{6})$", views.process_url, name="process_url"
    ),
]
