# Dictationery in presented in 
data = {
    "key" : "value"
}


# age of people
age = {
    "Anil" : 23,
    "Ram" : 33,
    "Hari" : 24,
    "Gita" : 45,
    "Ramesh" : [11,20,34]
}

print(type(age))

print(age.items())
print(age.values())
print(age.keys())

age.update({"Anil":10 , "Em Esh":21})
print(age.items());

print(age.get("Anil"));         #return none if the key is not in there
print(age["Anil"])              #return error if the key is not in there

value = age.pop("Gita",45);
print(value)

print(age.items())

item = age.popitem();
print(age.items())
print(item)

age.clear();
print(age.items());

