import unittest
from console import HBNBCommand
from models import storage
from models.user import User

class TestHBNBCommandCreate(unittest.TestCase):

    def setUp(self):
        """Set up test environment"""
        self.console = HBNBCommand()

    def test_create_with_string(self):
        """Test creating an object with string attributes"""
        self.console.onecmd('create User name="John_Doe"')
        #self.assertIn('User.', storage.all().keys())
        obj = list(storage.all().values())[0]
        self.assertEqual(obj.name, 'John Doe')

    def test_create_with_integer(self):
        """Test creating an object with integer attributes"""
        self.console.onecmd('create User age=30')
        #self.assertIn('User.', storage.all().keys())
        obj = list(storage.all().values())[0]
        self.assertEqual(obj.age, 30)

    def test_create_with_float(self):
        """Test creating an object with float attributes"""
        self.console.onecmd('create User height=5.9')
        #self.assertIn('User.', storage.all().keys())
        obj = list(storage.all().values())[0]
        self.assertEqual(obj.height, 5.9)

    def test_create_with_invalid_param(self):
        """Test creating an object with an invalid parameter"""
        self.console.onecmd('create User name="John" invalid_param="test"')
        #self.assertIn('User.', storage.all().keys())
        obj = list(storage.all().values())[0]
        self.assertFalse(hasattr(obj, 'invalid_param'))

    def tearDown(self):
        """Tear down test environment"""
        storage.all().clear()
        storage.save()

if __name__ == '__main__':
    unittest.main()

