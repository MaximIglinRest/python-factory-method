from src.notifications.base import Notification, NotificationFactory


class EmailNotification(Notification):
    def send(self, username: str, message: str) -> None:
        print(f"Send email to user {username}: {message}")


class EmailNotificationFactory(NotificationFactory):
    def create_notification(self) -> Notification:
        return EmailNotification()
