# class person:
#     def display(self,name,age):
#         print(name,age)
# class student(person):
#     def show(self,grade):
#         print(grade)
# a = student()
# a.display("kummar",56)
# a.show(6)


# class animal:
#     def eat(self):
#         print("animal eats")
# class dog(animal):
#     def brak(self):
#         print("dog brak")
# a = dog()
# a.eat()
# a.brak()

# class employee:
#     def display(self,nmae,salary):
#         print(nmae,salary)
# class Manager(employee):
#     def show(self,department):
#         print(department) 
# a = Manager()
# a.display("hari",23450)
# a.show("kerala")

# class grandparent:
#     def grandparent(self,name):
#         print(name)
# class parent(grandparent):
#     def parent(self,name):
#         print(name)
# class child(parent):
#     def child(self,name):
#         print(name)
# a = child()
# a.grandparent("kumar")
# a.parent("rahul")
# a.child("rahul kumar")

# class person:
#     def __init__(self,name):
#         self.name = name
# class teacher(person):
#     def __init__(self,name,subject):
#         super().__init__(name)
#         self.subject=subject
#     def display(self):
#         print(self.name,self.subject)
# a = teacher("hari","it")
# a.display()

