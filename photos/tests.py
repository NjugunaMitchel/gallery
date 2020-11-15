from django.test import TestCase
from .models import Editor, category,Pictures

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(username = 'John', email ='abc@dc.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.John,Editor))

    # Save Method
    def test_save_method(self):
        self.John.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)