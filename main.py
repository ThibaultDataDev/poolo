from .garden import Garden
from .potatoes import BagOfPotatoes
from .tomatoes import BagOfTomatoes
from .gardener import Gardener
Audrey = Gardener()
Jardin = Garden()
p = BagOfTomatoes()
q = BagOfPotatoes()
p.howmanytogrow(23)
q.howmanytogrow(2)
Jardin.add(p)
Jardin.add(q)
Audrey.create_vegetable('Tomato')
print(Jardin.counter())