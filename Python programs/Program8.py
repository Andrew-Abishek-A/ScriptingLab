listofvalues=[]

def CtoF():
	print("Enter the Temperature in Centigrade:")
	n = int(input())
	n1 = (n * 9 / 5) + 32
	print("Temperature in Farenheit is:", n1)
	listofvalues.append(("C: "+str(n),"F: "+str(n1)))
	


def FtoC():
	print("Enter the Temperature in Farenheit:")
	n = int(input())
	n1 = (n -32) * 5 / 9
	print("Temperature in Centigrade is:", n1)
	listofvalues.append(("F: "+str(n),"C: "+str(n1)))






run =True
while run:
	print("1.Convert Centigrade to Farenheit: press 1")
	print("2.Convert Farenheit to Centigrade: press 2")
	print("3.Convert Centigrade to Kelvin: press 3")
	print("4.Convert Kelvin to Centigrade: press 4")
	print("5.Convert Farenheit to Kelvin: press 5")
	print("6.Convert Kelvin to Farenheit: press 6")
	print("7.View all converted values: press 7")
	n = input()
	if n is "1":
		CtoF()
	elif n is "2":
		FtoC()
	#elif n is "3":
		#CtoK()
	#elif n is "4":
		#KtoC()
	#elif n is "5":
		#FtoK()
	#elif n is "6":
		#KtoF()
	elif n is "7":
		for i in listofvalues:
			print(i)
	else:
		run = False
	
