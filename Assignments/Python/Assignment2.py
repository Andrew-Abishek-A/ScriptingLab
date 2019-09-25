class Student:
	#def __init__(self):
		
	def display(self):
		print("The name of the student is:", self.name)
		print("The age of the student is:", self.age)
		print("The marks obtained by the student is:\n", self.list)
		
	def accept(self):
		print("Enter the name of the student")
		self.name=input()
		print("Enter the age of the student")
		self.age=input()
		print("Enter the marks")
		list1 = []
		for i in range(3):
			a = int(input())
			list1.append(a)
		self.list = list1

s1 = Student()
Student.accept(s1)
Student.display(s1)


student = {
	1 : "Amy",
	2 : "Anagha",
	3 : "Andrew"
}

for i in student:
	if int(i)%2 == 0:
		print(student[i])
		

