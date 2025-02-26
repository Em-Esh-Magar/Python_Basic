list = ["apple", 12,"ball",True];

print(list)

list[0]="batman";
print(list);

list.append("hero");        # Adds the hero in the last of list
print(list);

list.insert(0,"I am Iron Man");
print(list);

list.reverse();
print(list);

value = list.pop(2)
print(value);
print(list);

list.remove(12);
print(list);

list1 = [11,1,0.5,22.5,22]      
list1.sort();          # Only for the numbers
print(list1);
