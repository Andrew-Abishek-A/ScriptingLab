students = {
	"1MS17IS021":"Amy",
	"1MS17IS022":"Anagha",
	"1MS17IS023":"Andrew",
	"1MS17IS024":"Anirudh"
}
list=["Value1", "Value2", "Value3", "Value4"]
list2=[]
j=0

for i in students:
	print("Key is:", i, "Value is:", students[i])
	list[j] = students[i]
	#list2[j] = i
	j = j+1

print(list)
#print(list2)
print(students.keys())
print(students.values())
print(students.items())
