# ==> Here a=1, b=1 is a default value

def add(a=1,b=1):
    # print(f"The sum of {a} and {b} is ",a+b)
    return a+b
    
x = int(input("Enter a number : "));
y = int(input("Enter a number : "));

# Default value will be replaced by value of x and y 
z = add(x,y)
print(z)

# call a function with default parameter
m = add();
print(m)