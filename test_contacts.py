import unittest
from contacts import ContactManager

class TestContactManager(unittest.TestCase):
    def test_add_contact(self):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890")
        self.assertEqual(len(manager.get_contacts()), 1)

    def test_get_contacts(self):
        manager = ContactManager()
        manager.add_contact("John Doe", "1234567890")
        contacts = manager.get_contacts()
        self.assertEqual(contacts[0]['name'], "John Doe")
        self.assertEqual(contacts[0]['phone'], "1234567890")

if __name__ == "__main__":
    unittest.main()