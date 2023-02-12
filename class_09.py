# user = {
#     "username":"Shyam",
#     "id":321,
#     "status":"active",
#     "isMember": "true"
# }
#
# finaluser ={}
#
# finaluser=user.copy()
#
# user["deletd"]= "false"
# #del user
#
# print(user)
# print(finaluser)

user = {
    "username":"Shyam",
    "id":321,
    "status":"active",
    "isMember": "true",
}

teacher={
    "maths":"axy"
}

finaldictionary={}

for key in (user):
    finaldictionary.update(key)


print(finaldictionary)

