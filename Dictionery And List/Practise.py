"""1. Write a program to create a dictionary of Nepali words with values as their English
translation. Provide user with an option to look it up!
"""

words = {
    "Kitab" : "Book",
    "Kalam" : "Pen",
    "Sapana" : "Dream"
}

word1 = input("Enter Kitab/Kalam/Sapana :")
print(words.get(word1))


"""
2. Write a program to input eight numbers from the user and display all the unique 
numbers (once).
"""

unique = set();

a = 0;
while a<8:
    b = input("Enter a number : ")
    unique.add(b)
    a+=1

print(unique)


"""3. Can we have a set with 18 (int) and '18' (str) as a value in it?  ==> Yes we can"""
data = {18,"18"}
print(data)

"""4. What will be the length of following set s: 11,11.0,"11" --> 2"""
s = set();
s.add(11)
s.add(11.0)
s.add('11')
print(len(s),s)


"""5. Create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique."""

language = {}
check = 0;

while check<4:
    key = input("Enter your name : ")
    value = input("Enter your favorite language : ")
    language.update({key : value})
    check+=1
    
print(language,type(language))

"""6. If the names of 2 friends are same; what will happen to the program in problem 5? ==> It is override  """


"""7.If languages of two friends are same; what will happen to the program in problem 5? ==> Many friends can have same favorite language"""

"""8. Can you change the values inside a list which is contained in set S?
    set = {12,"Em Esh"}  ==> No we can't
"""



