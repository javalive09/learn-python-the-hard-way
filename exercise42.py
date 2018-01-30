# coding=utf-8
# 对象、类、以及从属关系

# super(Employee, self).__init__(name)

# 不过我还是建议你别去理解了，干脆完全忘记旧格式和新格式类的区别吧，就假设 Python 的 class 永远都要求你加上 (object) 好了，你的脑力要留着思考更重要的问题。

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass


## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None


## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary


## ??
class Fish(object):
    pass


## ??
class Salmon(Fish):
    pass


## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()
