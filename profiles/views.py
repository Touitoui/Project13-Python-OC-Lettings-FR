import logging

import sentry_sdk
from django.http import Http404
from django.shortcuts import render
from profiles.models import Profile

logger = logging.getLogger('profiles')


def index(request):
    """Render the profiles index page listing all user profiles.

    Args:
        request (HttpRequest): The incoming HTTP request.

    Returns:
        HttpResponse: Rendered profiles index page with all profiles.
    """
    profiles_list = Profile.objects.all()
    logger.info("Profiles index accessed — %d profiles found", profiles_list.count())
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
    logger.debug("Fetching profile for username=%r", username)
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        logger.warning("Profile not found: username=%r", username)
        raise Http404(f"Profile for user '{username}' not found")
    except Exception as e:
        logger.error("Unexpected error fetching profile username=%r: %s", username, e, exc_info=True)
        sentry_sdk.capture_exception(e)
        raise
    logger.info("Profile detail accessed: username=%r", username)
    context = {'profile': profile}
    return render(request, './profiles/profile.html', context)
