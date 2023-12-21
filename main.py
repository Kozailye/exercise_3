import random

def Atribut() :
   random1 = random.randint(1,6)
   random2 = random.randint(1, 6)
   random3 = random.randint(1, 6)
   random4 = random.randint(1, 6)
   random5 = random.randint(1, 6)
   random6 = random.randint(1, 6)


   list = [random1, random2, random3, random4, random5, random6]
   list.sort()
   list.pop(0)
   list[0] + list[1] + list[2]



class NPC:
   def __init__(self, nom, race, espèce ,profession ):
       self.Force = Atribut()
       self.Agilité = Atribut()
       self.Constitution = Atribut()
       self.Intelligence = Atribut()
       self.Sagesse = Atribut()
       self.Charisme = Atribut()
       self.classe_armure = random.randint(1,12)
       self.nom = nom
       self.race = race
       self.espèce = espèce
       self.point_de_vie = random.randint(1,20)
       self.profession = profession


   def caracteristique(self):

       print("force :", self.Force)
       print("Agilité :", self.Agilité)
       print("Constitution :", self.Constitution)
       print("Intelligence :", self.Intelligence)
       print("Sagesse :", self.Sagesse)
       print("Charisme :", self.Charisme)
       print("classe_armure :", self.classe_armure)
       print("nom :", self.nom)
       print("race :", self.race)
       print("espèce :", self.espèce)
       print("point_de_vie :", self.point_de_vie)
       print("profession :", self.profession)





class kobold(NPC):
    def attaquer(self, cible):
        de = random.randint(1,20)
        if de == 20:
            print('Critique!!')
            cible.dommages(random.randint(1,8))

        elif de == 1:
            print('rater')

        else:
            if de >= cible.classe_armure :
                print('bravo belle attaque')
                cible.dommages(random.randint(1, 6))

            elif de < cible.classe_armure :
                print('rater')



    def dommages(self, dommages):
        self.point_de_vie -= dommages




class heros(NPC):
    def attaquer(self, cible):
        de = random.randint(1,20)
        if de == 20:
            print('Critique!!')
            cible.dommages(random.randint(1,8))

        elif de == 1:
            print('rater')

        else:
            if de >= cible.classe_armure :
                print('bravo belle attaque')
                cible.dommages(random.randint(1, 6))

            elif de < cible.classe_armure :
                print('rater')



    def dommages(self, dommages):
        self.point_de_vie -= dommages
