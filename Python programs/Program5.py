def removeduplicates(list1):
	newlist = [];
	for number in list1:
		if number not in newlist:
			newlist.append(number)
	print(newlist);


removeduplicates([1,1,2,2,3,3,4,5,5,4])
