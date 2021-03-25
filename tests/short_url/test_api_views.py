import pytest
from django.conf import settings
from rest_framework import status
from rest_framework.reverse import reverse


class TestStats:
    @pytest.mark.django_db
    def test_get(self, test_url, api_client):
        url = reverse("stats", kwargs={"short_code": test_url.short_code})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert set(response.data.keys()) == {
            "created",
            "last_redirect",
            "redirect_count",
        }
        assert response.data["redirect_count"] == 0

    @pytest.mark.django_db
    def test_get_404(self, api_client):
        url = reverse("stats", kwargs={"short_code": "emptdb"})
        response = api_client.get(url)
        assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
class TestUrlViewSet:
    def test_create_with_short_code(self, api_client):
        url = reverse("url-list")
        response = api_client.post(
            url, data={"url": "https://test.com", "short_code": "testco"}
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == {"url": "https://test.com", "short_code": "testco"}

    def test_create_without_short_code(self, api_client):
        url = reverse("url-list")
        response = api_client.post(
            url,
            data={
                "url": "https://test.com",
            },
        )
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["url"] == "https://test.com"
        assert len(response.data["short_code"]) == settings.SHORT_CODE_LENGTH

    def test_create_with_invalid_short_code(self, api_client):
        url = reverse("url-list")
        response = api_client.post(
            url, data={"url": "https://test.com", "short_code": "invalid_short_code"}
        )
        assert response.status_code == status.HTTP_412_PRECONDITION_FAILED

    def test_create_with_existing_short_code(self, test_url, api_client):
        url = reverse("url-list")
        response = api_client.post(
            url, data={"url": "https://test.com", "short_code": test_url.short_code}
        )
        assert response.status_code == status.HTTP_409_CONFLICT

    def test_create_with_invalid_url(self, api_client):
        url = reverse("url-list")
        response = api_client.post(
            url,
            data={
                "url": "invalidurl",
            },
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST
