from django.shortcuts import render
from profiles.models import Profile


def index(request):
    """Render the profiles index page listing all user profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered profiles index page with all profiles.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, './profiles/index.html', context)


def profile(request, username):
    """Render the detail page for a single user profile.

    Args:
        request (HttpRequest): The incoming HTTP request.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: Rendered profile detail page.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, './profiles/profile.html', context)
