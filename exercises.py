
#Initialize a name list
names = ["Victor","Maximo","Ivan","Saul","Daniel"]

print(names)

#Add another name to the name list
names.append("Jaime")

#Print values from the name list
for name in names:
    print(name)




#Initialize a tuple with numbers from 1 to 7
numbers = (1,2,3,4,5,6,7)

i = 0

#Print values from the tuple of numbers
while i < len(numbers):
    print(numbers[i])
    i = i + 1



#Initialize a dictionary with a person's data.
data_person = {
    "Name": "Victor",
    "Last name": "Carmona",
    "Age": 18
}

#Print values from the dictionary with a person's data.
for data in data_person.values():
    print(data)

#A dictionary value is replaced.
data_person["Age"] = 19

#Print values from the dictionary with a person's data.
for data in data_person.values():
    print(data)



#Creation of a function that receives as parameter a sign and two numbers.
def operations(operator, n1, n2):
    if operator == "+":
        return n1+n2

    elif operator == "-":
        return n1-n2

    elif operator == "*":
        return n1*n2
    
    elif operator == "/":
        if n2 != 0:
            return n1 / n2
        else:
            return "It cannot be divided by 0."
        
    else: 
        return "Invalid operator"
    
print(operations("+", 10, 10))



