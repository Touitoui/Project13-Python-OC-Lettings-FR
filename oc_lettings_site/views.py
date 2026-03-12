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


def handler404(request, exception=None):
    """Render the custom 404 page."""
    return render(request, '404.html', status=404)


def handler500(request):
    """Render the custom 500 page and log the event."""
    logger.error("500 Internal Server Error: %s", request.path)
    return render(request, '500.html', status=500)
