for items in range(0,100,2):
    if(items%5==0):
        print(items)
    else:
        continue


list = ["Babu","Hari","Ram"]
for items in list:
    pass  # ==> We can skip this lop for now


for items in range(1,10,2):
    if(items==7):
        break
    else:
        print(items)