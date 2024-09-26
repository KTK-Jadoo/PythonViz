from abc import ABC, abstractmethod

class Deque(ABC):
    @abstractmethod
    def add_first(self, value):
        pass

    @abstractmethod
    def add_last(self, value):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass

    @abstractmethod
    def size(self):
        pass