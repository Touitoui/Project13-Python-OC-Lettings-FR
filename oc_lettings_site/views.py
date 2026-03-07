from django.shortcuts import render


def index(request):
    """Render the site home page.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered home page.
    """
    return render(request, 'index.html')
