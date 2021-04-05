from abc import ABC, abstractmethod

class Vegetables(ABC):
    def __init__(self, seeds_number=0):
        self.seeds_number = seeds_number

    @abstractmethod
    def howmanytogrow(self, seeds_number):
        pass