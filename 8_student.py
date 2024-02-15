# Create a dictionary named student with the following key-value pairs:
# "name": Your Name
# "age": Your Age
# "major": Your Major
# "hobbies": A list of your top three hobbies
# Add a new key-value pair for "State": Your State of Residence
# Update the "age" to your current age + 1
# Write a loop to iterate over the key-value pairs in the student 
# dictionary and print each pair on a new line in a well formatted way.

#student dictionary
student={
    'name': 'Garrett Austin','age': 22,
    'major': 'MIS and Management',
    'hobbies': ['Driving', 'Gaming', 'Watching Movies']}

#introduce state key-value
student['state']='Texas'

#add one to current age
student['age']+=1

#print loop
for x, y in student.items(): # x = key, y = values
    print(f"{x}: {y}")