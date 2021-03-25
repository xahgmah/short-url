import random
import string

from django.conf import settings


class ShortCodeGenerator:
    SHORT_CODE_CHARACTERS = string.digits + string.ascii_letters + "_"

    def generate_new_short_code(self):
        return "".join(
            random.choices(self.SHORT_CODE_CHARACTERS, k=settings.SHORT_CODE_LENGTH)
        )
