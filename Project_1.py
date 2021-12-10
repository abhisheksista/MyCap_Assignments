#task_1
import math
x=float(input("Input the radius of the circle: "))
y=(math.pi)*x*x
print("The area of the circle with radius "+str(x)+" is: "+str(y))
#task_2
fn=input("Input the Filename: ")
ext=fn.split(".")
if ext[-1]=="py":
    print("The extension of the file is: 'python'")
elif ext[-1]=="java":
    print("The extension of the file is: 'java'")
elif ext[-1]=="docx":
    print("The extension of the file is: 'document'")
elif ext[-1]=="txt":
    print("The extension of the file is: 'text'")
elif ext[-1]=="ppt":
    print("The extension of the file is: 'ppt'")
elif ext[-1]=="c":
    print("The extension of the file is: 'C'")
