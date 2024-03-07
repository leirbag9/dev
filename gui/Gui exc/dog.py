# class(es)

class pet():
    name = None
    fullness = 0

    def _init_(self, name):
        self.name = name

    def eat(self,food) :
        print(self.name + "is surviving" + food +"...")
        if food == "plutonium":
            self.fullness = self.fullness + 300




# program
pet_owner_name = input("What is your name ")