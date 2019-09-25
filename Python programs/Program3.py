#Demo: Classes in Python
#Notice the use of self, it is the first argument passed to any function

class Person:
	def __init__(self,name,age):
		self.name=name
		self.age=age

#Two objects s1 and s2 is created. The __init__ constructor is automatically called
p1 = Person("Anagha", 19)
p2 = Person("Amy", 20)

print("\nName of the person 1 is:", p1.name)
print("\nAge of the person 1 is:", p1.age)

print("\nName of the person 2 is:", p2.name)
print("\nAge of the person 2 is:", p2.age)

p2.age=10

print("\nModified age of the person 2 is:", p2.age)
