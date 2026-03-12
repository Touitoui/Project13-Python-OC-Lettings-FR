import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from profiles.models import Profile


@pytest.fixture
def user(db):
    return User.objects.create_user(username="testuser", password="testpass")


@pytest.fixture
def profile(db, user):
    return Profile.objects.create(user=user, favorite_city="Paris")


# --- Model tests ---

class TestProfileModel:
    def test_str(self, profile):
        assert str(profile) == "testuser"

    def test_favorite_city(self, profile):
        assert profile.favorite_city == "Paris"

    def test_favorite_city_blank_allowed(self, db, user):
        p = Profile.objects.create(user=user)
        assert p.favorite_city == ""


# --- View tests ---

class TestProfilesIndexView:
    def test_returns_200(self, client, db):
        response = client.get(reverse("profiles_index"))
        assert response.status_code == 200

    def test_uses_correct_template(self, client, db):
        response = client.get(reverse("profiles_index"))
        assert "./profiles/index.html" in [t.name for t in response.templates]

    def test_empty_list(self, client, db):
        response = client.get(reverse("profiles_index"))
        assert list(response.context["profiles_list"]) == []

    def test_populated_list(self, client, profile):
        response = client.get(reverse("profiles_index"))
        assert profile in response.context["profiles_list"]


class TestProfileDetailView:
    def test_returns_200(self, client, profile):
        response = client.get(reverse("profile", kwargs={"username": "testuser"}))
        assert response.status_code == 200

    def test_uses_correct_template(self, client, profile):
        response = client.get(reverse("profile", kwargs={"username": "testuser"}))
        assert "./profiles/profile.html" in [t.name for t in response.templates]

    def test_context_profile(self, client, profile):
        response = client.get(reverse("profile", kwargs={"username": "testuser"}))
        assert response.context["profile"] == profile
