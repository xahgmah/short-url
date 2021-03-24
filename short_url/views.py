from django.http import HttpResponse
from datetime import datetime
from short_url.models import Url
from django.shortcuts import get_object_or_404


def process_url(request, short_code):
    """
    This view redirects user to the full url by short representation
    """
    url_obj = get_object_or_404(Url, short_code=short_code)

    # TODO move this part to background process
    url_obj.last_redirect = datetime.now()
    url_obj.redirect_count += 1
    url_obj.save()

    response = HttpResponse(status=302)
    response['Location'] = url_obj.url
    return response
