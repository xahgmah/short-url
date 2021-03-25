from rest_framework import status
from rest_framework.exceptions import APIException


class InvalidShortCodeException(APIException):
    status_code = status.HTTP_412_PRECONDITION_FAILED
    default_detail = "The provided shortcode is invalid"


class UniqueShortCodeException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Shortcode is already in use"
