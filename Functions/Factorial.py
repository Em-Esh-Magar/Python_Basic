def recursion(num = 5):
    if num==0 or num==1:
        return 1
    else:
        return num * recursion(num-1)

num = int(input("Enter a number : "))
print(f"The factorial of {num} is ",recursion(num))
