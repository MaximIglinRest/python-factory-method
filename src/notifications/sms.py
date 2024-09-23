from src.notifications.base import Notification, NotificationFactory


class SmsNotification(Notification):
    def send(self, username: str, message: str) -> None:
        print(f"Send sms to user {username}: {message}")


class SmsNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return SmsNotification()
