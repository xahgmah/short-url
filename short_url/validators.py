from django.core.validators import RegexValidator
from rest_framework.validators import UniqueValidator, qs_exists

from short_url.exceptions import UniqueShortCodeException, InvalidShortCodeException


class ShortCodeValidator(RegexValidator):
    regex = '^[A-Za-z0-9_]{6}$'

    def __call__(self, value):
        """
        This method is default. The only difference: it raises InvalidShortUrlException instead of ValidationError
        """
        regex_matches = self.regex.search(str(value))
        invalid_input = regex_matches if self.inverse_match else not regex_matches
        if invalid_input:
            raise InvalidShortCodeException()


class UniqueShortCodeValidator(UniqueValidator):
    def __call__(self, value, serializer_field):
        """
        This method is default. The only difference: it raises UniqueShortUrlException instead of ValidationError
        """
        field_name = serializer_field.source_attrs[-1]
        instance = getattr(serializer_field.parent, 'instance', None)

        queryset = self.queryset
        queryset = self.filter_queryset(value, queryset, field_name)
        queryset = self.exclude_current_instance(queryset, instance)
        if qs_exists(queryset):
            raise UniqueShortCodeException()
