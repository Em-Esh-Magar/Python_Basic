"""
Write a program to read the text from a given file ‘poems.txt’ and find out 
whether it contains the word ‘twinkle’.
"""

with open("poem.txt","r")as f:
    poem = f.read()
# print(poem)
    
found = False

if("twinkle" in poem):
    print("Found")
    found = True
        
if found == False:
    print("Not Found")