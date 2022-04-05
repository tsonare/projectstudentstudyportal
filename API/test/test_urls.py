from django.test import SimpleTestCase
from django.urls import reverse, resolve
from API.views import *


class ApiTestUrls(SimpleTestCase):
    def test_note_api_resolve(self):
        url = reverse("note")
        print(resolve(url))
        self.assertEquals(resolve(url).func, NoteViewSet)

    def test_subject_api_resolve(self):
        url = reverse("subject")
        print(resolve(url))
        self.assertEquals(resolve(url).func, SubjectViewSet)

    def test_homework_api_resolve(self):
        url = reverse("homeworks")
        print(resolve(url))
        self.assertEquals(resolve(url).func, HomeworkViewSet)

    def test_todo_api_resolve(self):
        url = reverse("todos")
        print(resolve(url))
        self.assertEquals(resolve(url).func, TodoViewSet)
