from django.core.validators import MinLengthValidator
from django.db import models
from django.conf import settings
from core.mixins import CreatedModifiedMixin
import string
import random

SHORT_CODE_CHARACTERS = string.digits + string.ascii_letters + "_"


class Url(CreatedModifiedMixin):
    """
    Url shortener model
    """
    url = models.URLField()
    short_code = models.CharField(
        max_length=settings.SHORT_CODE_LENGTH,
        validators=[MinLengthValidator(settings.SHORT_CODE_LENGTH)],
        db_index=True)
    last_redirect = models.DateTimeField(null=True, auto_now_add=True)
    redirect_count = models.IntegerField(default=0)

    def __str__(self):
        return "{}-{}".format(self.short_code, self.url)

    @classmethod
    def get_new_short_code(cls):
        # TODO create a background task which creates a queue with list of generated short codes in advance.
        return cls.generate_new_short_code()

    @classmethod
    def generate_new_short_code(cls):
        """
        Generate a random string with certain allowed parameters.
        Ensure that it is a unique short_code.
        Regenerate  again and again until it is presented in the database
        """
        while True:
            short_code = "".join(random.choices(SHORT_CODE_CHARACTERS, k=settings.SHORT_CODE_LENGTH))
            try:
                # check if this short code exists in database
                # generate a new one if so and repeat the check
                cls.objects.get(short_code=short_code)
            except cls.DoesNotExist:
                # short code is unique
                return short_code
