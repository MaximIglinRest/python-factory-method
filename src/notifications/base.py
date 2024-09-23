from abc import abstractmethod, ABC


class Notification(ABC):
    @abstractmethod
    def send(self, username: str, message: str) -> None:
        pass


class NotificationFactory(ABC):
    @abstractmethod
    def create_notification(self) -> Notification:
        pass
