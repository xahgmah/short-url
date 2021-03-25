import pytest
from django.urls import reverse
from rest_framework import status

from short_url.models import Url


class TestProcessUrl:
    @pytest.mark.django_db
    def test_process_url(self, test_url, client):
        """
        First create a short_code (test_short_url fixture)
        Then ensure that redirect is happened.
        Check that number of redirects has increased
        """
        old_redirect_count = test_url.redirect_count
        old_redirect_time = test_url.last_redirect
        url = reverse("process_url", kwargs={"short_code": test_url.short_code})
        response = client.get(url)
        assert response.status_code == status.HTTP_302_FOUND
        assert response["Location"] == test_url.url
        url_obj = Url.objects.get(short_code=test_url.short_code)
        assert url_obj.redirect_count == old_redirect_count + 1
        assert url_obj.last_redirect > old_redirect_time

    @pytest.mark.django_db
    def test_process_url_404(self, client):
        """
        Test request to by non existing short code
        Currently DB table is empty
        """
        url = reverse("process_url", kwargs={"short_code": "emptdb"})

        response = client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND
