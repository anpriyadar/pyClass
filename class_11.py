# def addition(num1,num2):
#     num1+num2
#
# value= addition(10,20)
# print(value)
#
#
# def fullname(fname, lname):
#     return fname+lname
#
# name=fullname("ram", "shyam")
#
# print(name)



# def addFruits(fruitname):
#     fruit = []
#     fruit.append(fruitname)
#     return fruit
#
# fruits= addFruits("apple")
#
# print(fruits)

# attendee=[]
# def greetUsers(name):
#     for name in name:
#         attendee.append(name)
#
# usernames = ["ram", "hanah", "tom", "margot"]
# greetUsers(usernames)
#
# print(attendee)

# arbitary keyword arguments **


def empdetails(**data):
    print("data", data["fname"])

# fname="tom"
# lname="rock"
# address="xyz"
# salar=50000

empdetails(fname="tom", lname="rock", address="xyz", salar=50000)




