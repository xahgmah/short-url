import re

from short_url.short_code_generator import ShortCodeGenerator


class TestShortCodeGenerator:
    def test_generate_new_short_code(self):
        short_code1 = ShortCodeGenerator().generate_new_short_code()
        assert re.match("^[A-Za-z0-9_]{6}$", short_code1)
        short_code2 = ShortCodeGenerator().generate_new_short_code()
        assert re.match("^[A-Za-z0-9_]{6}$", short_code2)
        assert short_code1 != short_code2, (
            "Short codes are non- unique. Could be that collision has happened. "
            "Please try again."
        )
