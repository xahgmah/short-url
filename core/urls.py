from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from short_url.urls import urlpatterns
urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', include(urlpatterns), name='api'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
