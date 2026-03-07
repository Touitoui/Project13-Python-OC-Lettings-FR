from django.shortcuts import render
from lettings.models import Letting


def index(request):
    """Render the lettings index page listing all lettings.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered lettings index page with all lettings.
    """
    lettings_list = Letting.objects.all()
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
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, './lettings/letting.html', context)
