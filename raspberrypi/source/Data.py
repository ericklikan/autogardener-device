from abc import ABC, abstractmethod


class Data(ABC):

    @property
    @abstractmethod
    def type(self):
        pass

    @property
    @abstractmethod
    def value(self):
        pass

    @property
    @abstractmethod
    def timestamp(self):
        pass
