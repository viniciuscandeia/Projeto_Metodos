from src.models.repository.notification_repository import NotificationRepository
from src.singletons.meta_singleton import SingletonMeta


class NotificationRepositorySingleton(metaclass=SingletonMeta):
    def __init__(self):
        self.repository = NotificationRepository()

    def getInstance(self):
        return self.repository
