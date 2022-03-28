from django.test import TestCase
from .models import Note
# Create your tests here.

class NoteTest(TestCase):
    def create_note(self, title="Unit test case", description="Testing Unit test case"):
        return Note.objects.create(title=title, description=description)

    def test_note_creation(self):
        note = self.create_note()
        self.assertTrue(isinstance(note, Note))
        self.assertEqual(note.__str__, note.title)
