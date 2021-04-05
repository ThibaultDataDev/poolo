from .tomatoes import BagOfTomatoes
from .potatoes import BagOfPotatoes
from .carrots import BagOfCarrots

class Gardener():
    def getseedsnb(self):
        pass

    def count(self):
        total = 0
        for graine in self.listgraines:
            #print(graine.getseedsnb())
            total += graine.getseedsnb()
        #print ('il y a' + total + 'legumes')
        return total
    
    def __init__(self):
        self.list_vegetable_created = []
    
    def create_vegetable(self, category_choice):

        if category_choice in ["tomato", "Tomato"]:
            self.list_vegetable_created.append(BagOfTomatoes)

        if category_choice in ["potato", "Potato"]:
            self.list_vegetable_created.append(BagOfPotatoes)
        
        if category_choice in ["carrot", "Carrot"]:
            self.list_vegetable_created.append(BagOfCarrots)