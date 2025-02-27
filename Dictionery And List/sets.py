emptySet = set();

print(type(emptySet))


set1 = {1,2,3,4,5}
set2 = {5,6,7,8,9}

print(len(set1));

copySet = set1.copy();
print(copySet)

print(set1.union(set2))

print(set2.intersection(set1))

# discarding the element
copySet.discard(1)
value = copySet.pop();      
print(value)

# set1-set2
print(set1.difference(set2))

# set2-set1
print(set2.difference(set1))

# Removes the common value between set1 and set2 form set2
set2.difference_update(set1)
print(set2)


# adding the element in set1
set1.add(10);
print(set1)


# can written as set and another set as :
print(set1.union({1,9}))
print(set1.difference({1,9}))