from abc import ABC, abstractmethod
from parsers.string import tokenize


TRAIN_BASES_PATH = r'C:\Projects\chatbot\bases'


class Intent(ABC):
    @abstractmethod
    def __init__(self, name: str, progress=0):
        self.name = name.lower()
        self.progress = progress

    @abstractmethod
    def maps(self, msg) -> (bool, str):
        raise NotImplemented('All intents should implement maps')

    @staticmethod
    def tokenize(msg: str, unique=False):
        return tokenize(msg, unique)
