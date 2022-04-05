from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
import json
from rest_framework.test import APIRequestFactory


class TestNoteCreateApi(APITestCase):
    def test_note(self):
        factory = APIRequestFactory()
        request = factory.post(
            "note",
            {"title": "Api Testing", "description": "Testing Api Views"},
            format="json",
        )

    # def test_should_not_note_create_with_no_auth(self, title="Api testing",
    #         description="Testing api view for creating notes" ):
    #     self.client.login(username="tanuj", password="developer")
    #     note_data = {
    #            title:title,
    #            description:description
    #     }
    #     response = self.client.post(reverse("note"),note_data )
    #     self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
