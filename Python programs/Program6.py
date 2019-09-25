f1 = open('file1.txt', 'r')
list = []
d = {}
for x in f1:
	list1 = x.split(" ")
	list1[-1] = list1[-1][:-1]
	for i in list1:
		if i not in list:
			d[i] = 1
			list.append(i);
		else:
			d[i] = d[i]+1

print(d)
count=0
for x in d:
	count += d[x]
print("Number if words in the file:",count)

