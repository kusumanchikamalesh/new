a=int(input("enter a number"))
m=0
n=a
while (a>0):
    m=m+a%10
    a//=10
if n%m==0:
    print("harshad number")
else:
    print("not harshad number") 
