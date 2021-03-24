from django.urls import re_path
from short_url import views, api_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'shorten', api_views.UrlViewSet, basename='url')
urlpatterns = router.urls + [
    re_path(r'^(?P<short_code>[A-Za-z0-9_]{6})/stats/$', api_views.Stats.as_view()),
    re_path(r'^(?P<short_code>[A-Za-z0-9_]{6})/$', views.process_url),

]
