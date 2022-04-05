from django.test import TestCase, Client
from django.urls import reverse
from dashboard.models import Note
from time import perf_counter
import json

# Create your tests here.
start = perf_counter()


class HomeTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_not_authenticated_get(self):
        response = self.client.get("home_not_authenticated")
        self.assertTrue(response.status_code, 200)

    def test_home_authenticated_get(self):
        response = self.client.get("home_authenticated")
        self.assertTrue(response.status_code, 200)


class NoteTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_note_create(
        self, title="Unit test case", description="Testing Unit test case"
    ):
        self.client.login(username="tanuj", password="developer")
        note_create_url = reverse("notes")
        response = self.client.post(
            note_create_url, {title: title, description: description}
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/notes.html")

    def test_note_display(self):
        self.client.login(username="tanuj", password="developer")
        note_display_url = reverse("display_notes")
        response = self.client.get(note_display_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/notes_display.html")

    def test_note_detail(self):
        self.client.login(username="tanuj", password="developer")
        note_detail_url = reverse("note_detail", args=[8])
        response = self.client.get(note_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/notes_detail.html")

    def test_note_update(
        self, title="view testcase", description="Writing Unit test case for view."
    ):
        self.client.login(username="tanuj", password="developer")
        note_create_url = reverse("update_note", args=[8])
        response = self.client.post(
            note_create_url, {title: title, description: description}
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/note_update.html")

    def test_note_delete(self):
        self.client.login(username="tanuj", password="developer")
        note_delete_url = reverse("delete_note", args=[8])
        response = self.client.get(note_delete_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/note_delete.html")


class HomeworkTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homework_create(
        self,
        subject=2,
        title="Unit test case",
        description="Testing Unit test case",
        due_date="2022-01-03 06:08:00",
        status="Incomplete",
    ):
        self.client.login(username="tanuj", password="developer")
        homework_create_url = reverse("homework")
        response = self.client.post(
            homework_create_url,
            {
                subject: subject,
                title: title,
                description: description,
                due_date: due_date,
                status: status,
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/homework.html")

    def test_homework_display(self):
        self.client.login(username="tanuj", password="developer")
        homework_display_url = reverse("display_homework")
        response = self.client.get(homework_display_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/homework_display.html")

    def test_homework_detail(self):
        self.client.login(username="tanuj", password="developer")
        homework_detail_url = reverse("homework_detail", args=[4])
        response = self.client.get(homework_detail_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/homework_detail.html")

    def test_homework_update(
        self,
        subject=2,
        title="Unit test case",
        description="Testing Unit test case update",
        due_date="2022-01-03 06:08:00",
        status="Completed",
    ):
        self.client.login(username="tanuj", password="developer")
        homework_update_url = reverse("update_homework", args=[4])
        response = self.client.post(
            homework_update_url,
            {
                subject: subject,
                title: title,
                description: description,
                due_date: due_date,
                status: status,
            },
        )
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/homework_update.html")


class YoutubeTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_youtube(self, text="python"):
        self.client.login(username="tanuj", password="developer")
        youtube_url = reverse("youtube")
        response = self.client.post(youtube_url, {"text": text})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/youtube.html")


class WikipediaTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_wikipedia(self, text="Climate Change"):
        self.client.login(username="tanuj", password="developer")
        wikipedia_url = reverse("wikipedia")
        response = self.client.post(wikipedia_url, {"text": text})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/wikipedia.html")


class DictionaryTestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_dictionary(self, text="forgot"):
        self.client.login(username="tanuj", password="developer")
        dictionary_url = reverse("dictionary")
        response = self.client.post(dictionary_url, {"text": text})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dictionary.html")


end = perf_counter()
execution_time = end - start
print(execution_time)
