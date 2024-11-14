#Write a program to show students' grades by entering five subject marks and calculating average marks and grades. For example, if the average is between 91 to 100, A2 is between 81 to 90, and so on, do it till grade E2?

t=int(input("enter your marks at Maths"))
y=int(input("enter your marks at science"))
u=int(input("enter your marks at social"))
c=int(input("enter your marks at english"))
g=int(input("enter ypur marks at computer"))

h=(t+y+u+c+g)/5

if h>=91 and h <=100:
    print("Your grade is A1")

elif h>=81 and h<=90:
    print("Your grade is A2")
elif h>=71 and h<=80:
    print("Your grade is b1")
elif h>=61 and h<=70:
    print("Your grade is b2")
elif h>=51 and h<=60:
    print("Your grade is c1")

else:
    print("rewrite your exam")