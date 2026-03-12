import logging

from django.shortcuts import render

logger = logging.getLogger('oc_lettings_site')


def index(request):
    """Render the site home page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered home page.
    """
    logger.info("Home page accessed")
    return render(request, 'index.html')
