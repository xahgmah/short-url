from django.db import models
from django.contrib import admin


class CreatedModifiedMixin(models.Model):
    """
    Add extra fields to logging create datetime and last update datetime.
    """
    created = models.DateTimeField(null=True, auto_now_add=True)
    modified = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True


class CreatedModifiedAdminMixin(admin.ModelAdmin):
    """
    Extend admin views with extra fields
    """
    readonly_fields = ('created', 'modified')
    list_filter = ('created', 'modified')
