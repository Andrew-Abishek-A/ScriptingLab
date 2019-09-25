#Demo: Classes in python
#Concept: Use of del function to delete attributes of an object and the object itself

class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person("Anagha", 19)

print("\nName of the person 1 is:", p1.name)
print("\nAge of the person 1 is:", p1.age)

print("*****Printing after deleting attribute of Person p1*****");
del p1.age #Deleting the age attribute of p1 Person
print("\nName of the person 1 is:", p1.name)
#print("\nAge of the person 1 is:", p1.age)
#Error is: AttributeError: 'Person' object has no attribute 'age'

print("*****Printing after deleting Person p1*****");
del p1 #Deleting the Person p1
#print("\nName of the person 1 is:", p1.name)
#print("\nAge of the person 1 is:", p1.age)
#Error is: NameError: name p1 is not defined
