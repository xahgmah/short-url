from rest_framework import mixins, viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from short_url.models import Url
from short_url.serializers import StatsSerializer, CreateUrlSerializer


class Stats(APIView):
    """
    Provide stats of the short url.
    """

    def get(self, request, short_code):
        """
        Return stats of the short url.
        """
        instance = get_object_or_404(Url, short_code=short_code)

        serializer = StatsSerializer(instance)
        return Response(serializer.data)


class UrlViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    Create a new short url
    """
    serializer_class = CreateUrlSerializer
    queryset = Url.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Default create method extended with the following logic:
        if short code is empty generate a new one before save
        """
        data = request.data.copy()
        if not data.get('short_code'):
            data['short_code'] = Url.get_new_short_code()
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)