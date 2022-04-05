from django.test import SimpleTestCase
from django.urls import reverse, resolve
from dashboard.views import *
from API.views import *
from time import perf_counter

start = perf_counter()


class HomeTestUrls(SimpleTestCase):
    def test_home_not_authenticated_resolve(self):
        url = reverse("home_not_authenticated")
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_not_authenticated)

    def test_home_authenticated_resolve(self):
        url = reverse("home_authenticated")
        print(resolve(url))
        self.assertEquals(resolve(url).func, home_authenticated)


class NoteTestUrls(SimpleTestCase):
    def test_note_create_resolve(self):
        url = reverse("notes")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteCreateView)

    def test_note_display_resolve(self):
        url = reverse("display_notes")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteDisplayView)

    def test_note_detail_resolve(self):
        url = reverse("note_detail", args=[8])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteDetailView)

    def test_note_update_resolve(self):
        url = reverse("update_note", args=[8])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteUpdateView)

    def test_note_delete_resolve(self):
        url = reverse("delete_note", args=[8])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, NoteDeleteView)


class HomeworkTestUrls(SimpleTestCase):
    def test_homework_create_resolve(self):
        url = reverse("homework")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeworkCreateView)

    def test_homework_display_resolve(self):
        url = reverse("display_homework")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeworkDisplayView)

    def test_homework_detail_resolve(self):
        url = reverse("homework_detail", args=[4])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeworkDetailView)

    def test_homework_update_resolve(self):
        url = reverse("update_homework", args=[4])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeworkUpdateView)

    def test_homework_delete_resolve(self):
        url = reverse("delete_homework", args=[4])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, HomeworkDeleteView)


class TodoTestUrls(SimpleTestCase):
    def test_todo_create_resolve(self):
        url = reverse("todo")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoCreateView)

    def test_todo_display_resolve(self):
        url = reverse("display_todo")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoDisplayView)

    def test_todo_Update_resolve(self):
        url = reverse("update_todo", args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoUpdateView)

    def test_todo_delete_resolve(self):
        url = reverse("delete_todo", args=[2])
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, TodoDeleteView)


class YoutubeTestUrls(SimpleTestCase):
    def test_youtube_resolve(self):
        url = reverse("youtube")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, YoutubeView)


class WikipediaTestUrls(SimpleTestCase):
    def test_wikipedia_resolve(self):
        url = reverse("wikipedia")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, WikipediaView)


class DictionaryTestUrls(SimpleTestCase):
    def test_dictionary_resolve(self):
        url = reverse("dictionary")
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, DictionaryView)


end = perf_counter()
execution_time = end - start
print(execution_time)
