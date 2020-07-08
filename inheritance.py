#all the different kingdoms of life could extend from a single class type object each inheriting kingdoms familys and species as each layer of polymorphism increases
#class Life():
    #def __init__(self,name,age=0,family="",kingdom=""):

class Animal():#class Animal(Life):     Kingdom layer
    def __init__(self,name,age=0,family="",kingdom="Animal"):
        #Life.__init__(self,...)
        self.name=name
        self.family=family
        self.age=age
        self.kingdom=kingdom
    #both animal functions would make sense for all Life type objects if implemented
    def greet(self):
        print("Hello my name is {a}, I am a {b} year old {c} from the {d} kingdom".format(a=self.name,b=self.age,c=self.family,d=self.kingdom))
    def eat(self,food):
        print("Thank you for the {a}!".format(a=food))


class Cat(Animal):#famlily/species layer
    def __init__(self,name,age,family="Felion"):
        Animal.__init__(self,name,age,family)
    def greet(self):#overide the greet function from the parent object
        print("Meow Meow {a}, Meow {b} Meow Meow {c} nyuuu {d} Mau".format(a=self.name,b=self.age,c=self.family,d=self.kingdom))
class Human(Animal):#family/species Layer
    def __init__(self,name,age,family="Human"):
        Animal.__init__(self,name,age,family)


me=Human("Kurt",25)#human animal
brother=Cat("Nelson",14)#Felion animal
newborn=Animal("Alive")#defualt age for animals is 0

brother.greet()
me.greet()

brother.eat("fish")
me.eat("ramen")

newborn.greet()
newborn.eat("energy")
