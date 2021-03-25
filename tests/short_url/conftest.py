import pytest

from short_url.models import Url


@pytest.fixture
@pytest.mark.django_db
def test_url():
    return Url.objects.create(url="https://google.com", short_code="google")
