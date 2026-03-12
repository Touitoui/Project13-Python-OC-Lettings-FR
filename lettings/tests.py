import pytest
from django.urls import reverse

from lettings.models import Address, Letting


@pytest.fixture
def address(db):
    return Address.objects.create(
        number=7,
        street="Test Street",
        city="Test City",
        state="TS",
        zip_code=12345,
        country_iso_code="TST",
    )


@pytest.fixture
def letting(db, address):
    return Letting.objects.create(title="Test Letting", address=address)


# --- Model tests ---

class TestAddressModel:
    def test_str(self, address):
        assert str(address) == "7 Test Street"

    def test_verbose_name_plural(self):
        assert Address._meta.verbose_name_plural == "addresses"


class TestLettingModel:
    def test_str(self, letting):
        assert str(letting) == "Test Letting"


# --- View tests ---

class TestLettingsIndexView:
    def test_returns_200(self, client, db):
        response = client.get(reverse("lettings_index"))
        assert response.status_code == 200

    def test_uses_correct_template(self, client, db):
        response = client.get(reverse("lettings_index"))
        assert "./lettings/index.html" in [t.name for t in response.templates]

    def test_empty_list(self, client, db):
        response = client.get(reverse("lettings_index"))
        assert list(response.context["lettings_list"]) == []

    def test_populated_list(self, client, letting):
        response = client.get(reverse("lettings_index"))
        assert letting in response.context["lettings_list"]


class TestLettingDetailView:
    def test_returns_200(self, client, letting):
        response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
        assert response.status_code == 200

    def test_uses_correct_template(self, client, letting):
        response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
        assert "./lettings/letting.html" in [t.name for t in response.templates]

    def test_context_title(self, client, letting):
        response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
        assert response.context["title"] == "Test Letting"

    def test_context_address(self, client, letting):
        response = client.get(reverse("letting", kwargs={"letting_id": letting.id}))
        assert response.context["address"] == letting.address
