# Dictionary.

student = {
    "firstname" : "Ronaldo",
    "lastname": "xyz",
    "class" : 10,
    "roll": 210,
    "address" : "INDIA",
    "car": "audi"
}



#Dictionary are ordered, changable and donot allow duplicates

# print(student["firstname"])
#
# print(" the First name of student is", student["roll"])
#
#
# # via get method
# print(" the First name of student is",student.get("firstname"))

#get the key present in dictionary

# print(student.keys())
# print(student.values())
#
# if "class" in student:
#     print("class key is present")
# else:
#     print("key doesnot exist")

# Change the value of dictionary:

# print(student["firstname"])
# print(student["lastname"])
#
#
# student["firstname"] = "cristiano"
# student["lastname"] =  "Ronaldo"
#
# print(student["firstname"])
# print(student["lastname"])
#
# print(student)


# student.update({"firstname" : "cristiano", "lastname":"Ronaldo"})
#
# print(student)

#Add a new value to dictionary


# student["age"] = 20
# student.update({"grade": "A"})
#
# print(student)

#Remove the key value pair

# print(student)
# del student["car"]
# print(student)
#
# student.clear()
# print(student)


# objectValue = student.values()
# print(objectValue)
#
# if "INDIA" in objectValue:
#     print("yes")
# else:
#     print("no")

guest={}

guest["name"] = "ram"

print(guest)



