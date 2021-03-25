import mock
import pytest

from short_url.models import Url


class TestUrl:
    @mock.patch("short_url.models.Url.get_unique_short_code")
    def test_get_new_short_code(self, mock_short_code):
        mock_short_code.return_value = "qwe123"
        assert Url.get_new_short_code() == "qwe123"
        mock_short_code.assert_called_once()

    @pytest.mark.django_db
    @mock.patch(
        "short_url.short_code_generator.ShortCodeGenerator.generate_new_short_code"
    )
    def test_get_unique_short_code(self, mock_generator, test_url):
        """
        Create url object (test_url fixture)
        Imitate a situation where existing short code was generated
        Ensure that generator was triggered second time to regenerate the short code
        """
        mock_generator.side_effect = [test_url.short_code, "unique"]
        assert Url.get_unique_short_code() == "unique"
        assert mock_generator.call_count == 2
