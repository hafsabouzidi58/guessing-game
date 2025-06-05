'''fruit = {"nom":"pomme","prix":22.5,"quantite":120}
print(fruit["prix"])


print(f"le prix d'1 kilogramme {fruit["nom"]} est egal a {fruit["prix"]} dhs ")
fruit["origine"] = "midelt"
print(fruit)
del fruit["origine"]
print(fruit)
fruits = {"pomme":{"prix":22.5,"quantite":120},"orange":{"prix":9.5,"quantite":230},"banane":{"prix":20,"quantite":185}}
for nom in fruits.keys():
    print (nom) 
for nom in fruits.values():
    print(nom)
for i in fruits.values():
    print(i["prix"])
for nom , infos in fruits.items():
   # print(nom)
    #print(infos)
   print(f"le prix total de {nom} est egal a {infos["prix"]*infos["quantite"]}")


list = [] 
for nom , infos in fruits.items():
    if(infos["quantite"] > 150 ):
        list.append(nom)

print(list)
liste = []
liste = [ nom for nom , infos in fruits.items()  if infos["quantite"] > 150 ]
print(liste)


nom = ["pomme","oranges","banane"]
prix = [22.5,9.5,20]
quantite = [120,230,185]

listfruits = list(zip(nom,prix,quantite))
print(listfruits)

l = {nom :(prix,quantite) for nom , prix , quantite in zip(nom,prix,quantite)}
print(l)
l = {prix prix quantite for nom , prix , quantite in zip(nom,prix,quantite)}
print(l) '''




class Livre(object):
    def __init__(self,isbn,titre,auteur):
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
class User(object):
    def __init__(self,nom,age):
        self.nom = nom
        self.age = age
        self.lisemp = []
class Bib(object):
    def __init__(self):
        self.uti = []
        self.liv = {}
    def ajouterlivre(self,livre):
        if livre.isbn not in self.liv :
           self.liv[livre.isbn] = livre
        else:
           print("deja ajouter dans dictionnaire")
    def emprunterlivre(self,user,livre):
         if user not in self.uti :
            self.uti.append(user)
         if livre.isbn not in self.liv :
            print("le livre c pas dispo ")
         else:
            user.lisemp.append(livre)
            del self.liv[livre.isbn]
    def afficherlivre(self):
        if len(self.liv) != 0 :
            for x,y in self.liv.items():
                print(f"le code de ce livre est {x} et le nom {y}")
        else:
            print("est vide")
        
   
    def ajouteruser(self,user):
        if user not in self.uti :
            self.uti.append(user)
        else:
            print("user deja existe ")


livre1 = Livre("123", "Python Facile", "Dupont")
utilisateur1 = User("Hafsa", 20)

biblio = Bib()
biblio.ajouterlivre(livre1)
biblio.ajouteruser(utilisateur1)
biblio.afficherlivre()
biblio.emprunterlivre(utilisateur1, livre1)


        
        
