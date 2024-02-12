person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)
print(person)
# print out the name of the second child
print(person["children"][1]) # for dictionaries, supply the key to get a list ("children"), and then give index value to get response (1)

# print out the name of the cat

print(person["pets"]["cat"]) # for dictionaries, supply the key to get a list ("pets"), and then give index value to get response (cat)
pet_dictionary = person['pets']
#print(type(pet_dictionary))
print(pet_dictionary['cat'])

# use a loop to print out the names of each child
list_of_children = person['children']
print(type(list_of_children))

for child in list_of_children:
    print(child)

#for child in person['children']:
    #print(child)

for child in person['children']:
    print(child)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for pet in person['pets']:
    print(f"The type of pet is: {pet} and the name of the pet is: {person['pets'][pet]}")

for i, j in person['pets'].items():
    print (i,j)
    print(f"The type of pet is: {i} and the name of the pet is: {j}")