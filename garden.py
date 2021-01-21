from potatoes import BagOfPotatoes
from tomatoes import BagOfTomatoes

class Garden():

    SIZE = 30

    def __init__(self):
        self.listgraines= []

    
    def add(self, vegetables):
        if self.counter()+vegetables.seeds_number <= Garden.SIZE:
            self.listgraines.append(vegetables)

    def _plant(self, cls):
        return

    def counter(self):
        compteur = 0
        for vegetables in self.listgraines:
            compteur += vegetables.seeds_number
        return compteur