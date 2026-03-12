import pytest
from django.urls import reverse


# --- Index view ---

class TestIndexView:
    def test_returns_200(self, client, db):
        response = client.get(reverse("index"))
        assert response.status_code == 200

    def test_uses_correct_template(self, client, db):
        response = client.get(reverse("index"))
        assert "index.html" in [t.name for t in response.templates]


# --- Custom error handlers ---

class TestErrorHandlers:
    def test_404_page(self, client, db):
        response = client.get("/404/")
        assert response.status_code == 404

    def test_500_page(self, client, db):
        response = client.get("/500/")
        assert response.status_code == 500
