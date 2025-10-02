from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingSignalTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username="alice", password="pass123")
        self.user2 = User.objects.create_user(username="bob", password="pass123")

    def test_notification_created_on_message(self):
        # Create a message from user1 to user2
        message = Message.objects.create(
            sender=self.user1,
            receiver=self.user2,
            content="Hello Bob!"
        )

        # Check that a notification was created
        notification = Notification.objects.get(user=self.user2, message=message)
        self.assertEqual(notification.text, "You have a new message from alice")
        self.assertFalse(notification.is_read)
