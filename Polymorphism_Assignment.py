
# Parent Class Person
class Person:
    name = "Barry Allen"
    email = "ballen@CCPD.org"
    occupation = "Forensic Scientist"

    def getInfo(self):
        input_name = input("Please enter a name: ")
        if (input_name == self.name):
            print("\nName: {} \nContact: {} \nOccupation: {}".format(self.name, self.email, self.occupation))
        else:
             print("\n{} Not Found".format(input_name))

# Child Class Metahuman
class Metahuman(Person):
    ability = "Speedster"
    classification = "Superhero"
    affiliation = "STAR Labs"

    # Since Barry Allen also works for STAR Labs to an extent, the same method is used
    # but with affiliation instead of occupation

    def getInfo(self):
        input_name = input("Please enter a name: ")
        if (input_name == self.name):
            print("\nName: {} \nContact: {} \nAffiliation: {}".format(self.name, self.email, self.affiliation))
        else:
             print("\n{} Not Found".format(input_name))
        

# Child Class Universe
class Superhero(Person):
    comic_universe = "DC"
    tv_universe = "Arrowverse"

    # Again, the same method is used, but since Barry exists in a superhero universe,
    # It can replace occupation or affiliation

    def getInfo(self):
        input_name = input("Please enter a name: ")
        if (input_name == self.name):
            print("\nName: {} \nContact: {} \nComic Universe: {}".format(self.name, self.email, self.comic_universe))
        else:
            print("\n{} Not Found".format(input_name))
    
    
                

if __name__ == "__main__":
    person = Person()
    person.getInfo()

    metahuman = Metahuman()
    metahuman.getInfo()

    hero = Superhero()
    hero.getInfo()
