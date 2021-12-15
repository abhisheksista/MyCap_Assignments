i=int(input("Enter length of a list: "))
print("Enter a range of random numbers: ")
list1=[]
list2=[]
while i>0:
    x=int(input())
    list1.append((x))
    i=i-1
for number in list1:
    if number>0:
        list2.append((number))
print("The positive numbers in given list are:",list2)
