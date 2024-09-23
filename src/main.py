from src.notifications.base import NotificationFactory
from src.notifications.email import EmailNotificationFactory
from src.notifications.sms import SmsNotificationFactory


def notify_user(factory: NotificationFactory, message: str, username: str) -> None:
    notification = factory.create_notification()
    notification.send(username, message)


if __name__ == "__main__":
    username = "Yeblan"
    message = f"Hello, {username}"

    email_factory = EmailNotificationFactory()
    sms_factory = SmsNotificationFactory()

    notify_user(email_factory, message, username)
    notify_user(sms_factory, message, username)
