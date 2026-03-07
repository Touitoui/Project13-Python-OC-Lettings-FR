from django.contrib import admin
from django.urls import path
import django.views.defaults

from . import views
from lettings import views as lettings_views
from profiles import views as profiles_views


def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)


def custom_server_error(request):
    return django.views.defaults.server_error(request)


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', lettings_views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    path('profiles/', profiles_views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),

    path("404/", custom_page_not_found),
    path("500/", custom_server_error),
]
