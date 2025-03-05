def function(indata):
    string = ""

    for i in range(10):
        j = str(i)
    # if a.find(j)!=-1:
        if j in indata:
            continue
        else:
            string+=j

    for i in range(97,123):
        char = chr(i)
        if char in indata:
            continue
        else:
            string+=char
        
    return string


a = input("Enter number and lower letter: ")

string = function(a)
     
print(string)
