from vegetables import Vegetables

class BagOfPotatoes(Vegetables):

    def howmanytogrow(self, seeds_number):
        self.seeds_number += seeds_number
        print (f'Vous avez {seeds_number} graines')
