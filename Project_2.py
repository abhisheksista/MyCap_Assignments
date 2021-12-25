#positive numbers in a range
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

#fibonacci series
n=int(input("enter number of values in fibonacci series: "))
a=0
b=1
n=n-2
print(a)
print(b)
while n>0:
    c=a+b
    print(c)
    a=b
    b=c
    n=n-1
