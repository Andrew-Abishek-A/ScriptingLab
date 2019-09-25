mydictionary = {
	"name":"Archie",
	"identity":"Student",
	"age":17
}
print(mydictionary)

key = mydictionary["name"]
value = mydictionary.get("name")
print("The key is:", key)
print("The value is:", value)
