from django.test import RequestFactory
from django.urls import reverse

from oc_lettings_site.views import handler404, handler500


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
    def test_404_page(self, client):
        response = client.get("/nonexistent-url-that-does-not-exist/")
        assert response.status_code == 404

    def test_500_page(self):
        factory = RequestFactory()
        request = factory.get("/")
        response = handler500(request)
        assert response.status_code == 500
