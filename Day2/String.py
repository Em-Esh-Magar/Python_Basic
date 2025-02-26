# 1.
a = input("Enter a name : ");
print("Good Afternoon ",a);
#print(f"Good Morning {a}! How are you");


# 2. Detect double space;
b = "Hello  I  am  a  Developer";
print(f"Good Morning {a}! {b}");
print(b.find("  "));

# 3. Replace double space with a single space
c = b.replace("  "," ");
print(c)

