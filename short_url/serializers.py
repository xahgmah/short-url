from rest_framework import serializers

from short_url.models import Url
from short_url.validators import ShortCodeValidator, UniqueShortCodeValidator


class StatsSerializer(serializers.ModelSerializer):
    """
    Serializer to provide stats data of the url
    """

    class Meta:
        model = Url
        fields = ['created', 'last_redirect', 'redirect_count']


class CreateUrlSerializer(serializers.ModelSerializer):
    """
    Serializer for Url creation.
    It is using custom validators to raise exceptions with certain error_codes:
    409 - Shortcode is already in use
    412 - The provided shortcode is invalid

    Rest of validation errors return default 400 code
    """
    short_code = serializers.CharField(validators=[
        ShortCodeValidator(),
        UniqueShortCodeValidator(queryset=Url.objects.all()),
    ], required=False)

    class Meta:
        model = Url
        fields = ['url', 'short_code']
