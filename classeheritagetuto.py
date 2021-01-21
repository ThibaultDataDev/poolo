class Voiture:

    model = 'C4'

    def __init__(self, marque, modele, couleur):
        self.__marque = marque
        self.__modele = modele
        self.__couleur = couleur
        print("Création de la voiture")

    def start(self, state = 'démarrée'):
        print (f'Votre voiture est {state}')
    

class VoiutureDesport(Voiture):
    def __init__(self, marque, modele, couleur, puissance):
        print (f'Votre {marque} {modele} de couleur {couleur} et de puissance {puissance} chevaux est prête') #methode 'fstring" pour print directement
        self.puissance = puissance

    def start(self, state = 'en chauffe'):
        print (f'Votre voiture est {state}')


if __name__ == "__main__":
    v = Voiture('Audi', 'RS6', 'Jaune')
    v.start()
    print(v.start)

    v2 = Voiture('Tesla', 'S', 'Noire')
    v2.start('Starting')
    print(v2.start)


    v3 = VoiutureDesport('Porsche', 'Panamera', 'Jaune', '600' )
    v3.start()
    print (v3.start)

    print (Voiture.model)

testt = isinstance(v, Voiture)
print (testt)





class Formation(object):
  @classmethod
  def from_string(cls, name):
    formation = cls(name)
    return formation

python = Formation.from_string(‘Python')

python = Formation().from_string(‘Python')