import logging

import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from lettings.models import Letting

logger = logging.getLogger('lettings')


def index(request):
    """Render the lettings index page listing all lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered lettings index page with all lettings.
    """
    lettings_list = Letting.objects.all()
    logger.info("Lettings index accessed — %d lettings found", lettings_list.count())
    context = {'lettings_list': lettings_list}
    return render(request, './lettings/index.html', context)


def letting(request, letting_id):
    """Render the detail page for a single letting.

    Args:
        request (HttpRequest): The incoming HTTP request.
        letting_id (int): The primary key of the letting to display.

    Returns:
        HttpResponse: Rendered letting detail page.
    """
    logger.debug("Fetching letting with id=%s", letting_id)
    try:
        letting = Letting.objects.get(id=letting_id)
    except Letting.DoesNotExist:
        logger.warning("Letting not found: id=%s", letting_id)
        raise Http404(f"Letting with id {letting_id} not found")
    except Exception as e:
        logger.error("Unexpected error fetching letting id=%s: %s", letting_id, e, exc_info=True)
        sentry_sdk.capture_exception(e)
        raise
    logger.info("Letting detail accessed: id=%s title=%r", letting_id, letting.title)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, './lettings/letting.html', context)
