from django.contrib import admin

from core.mixins import CreatedModifiedAdminMixin
from short_url.models import Url


@admin.register(Url)
class UrlAdmin(CreatedModifiedAdminMixin):
    list_display = ('url', 'short_code', 'redirect_count', 'last_redirect')
    search_fields = ('url', 'short_code')
