
class Animal:

    """Classe mère qui contient les éléments communs aux classes filles
    """

    def __init__(self,nom,age) -> None:
        self.nom = nom
        self.age = age

    def emettre_son(self):
        print("Son de l'animal......")


class Chat(Animal):
    
    def __init__(self, nom, age, couleur) -> None:
        #super() -> mot clé qui pointe vers la classe mère
        super().__init__(age,nom)
        self.couleur = couleur

    def dormir(self):
        print('Dormir.........')

    # Surcharge de fonctions (overload): modifier les fonctions définies dans la classe mère

    def emettre_son(self):
        print('Miauller................')


class Chien(Animal):

    def emettre_son(self):
        print('Aboyer................')


class Giraffe(Animal):
    pass
        

    



# Une classe mère définie une sorte de structure de base pour les classes, elle contient les éléments (attributs, fonctions)
# communs aux classes filles
# Une classe fille, via l'héritage récupère tous les éléments de la classe mère
# Une classe, en plus des attributs définis dans la classe, elle peut avoir des attributs qui lui spécifiques
# Une classe, en plus des fonctions définies dans la classe, elle peut avoir des fonctions qui lui spécifiques
# Une classe fille peut en cas de besoin surcharger les fonctions définies dans la classe mère

a = Animal("nom_animal", 5)
a.emettre_son()


c = Chat('nom_chat', 3, 'gris')
c.emettre_son()
c.dormir()

chien = Chien('bobby', 5)
chien.emettre_son()

print(isinstance(a, Animal))
print(isinstance(c, Chat))
print(isinstance(c, Animal))
print(isinstance(a, Chat))

# Polymorphisme est une conséquence de l'héritage. C'est le fait que l'objet parent puisse prendre
# la forme de tous les objets enfants.


# Fonction polymorphique
def son(a:Animal):
    a.emettre_son()


son(a)
son(c)
son(chien)
son(Giraffe('sdsq',15))

