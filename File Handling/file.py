with open("abc.txt","w") as f:
    f.write("Hello, I am future python developer.")
    f.write("I am currently learning python.")
    
with open("abc.txt","r") as f1:
    a=f1.read();

print(a)