"""
To Print a string in the number of letter provide by user:
    eg: Input = "HelloWorld",3
        Output = hel
                 loW
                 orl 
                 d
"""

def function(string, num):
    i=0
    string1 = ""
    while i<len(string):
        if(i%num==0):
            print(string1)
            string1 = ""
        string1+=string[i]
        i+=1
        if(i==len(string)):
            print(string1)
        

string = input("Enter a string : ")
num = int(input("Enter a num : "))
function(string,num)
