def add():
 f=int(input("Enter the first number: "))
 s=int(input("Enter the second number: "))
 print(f+s)

def sub():
 f=int(input("Enter the first number: "))
 s=int(input("Enter the second number: "))
 print(f-s)

def mul():
 f=int(input("Enter the first number: "))
 s=int(input("Enter the second number: "))
 print(f*s)
		
def div():
 f=int(input("Enter the first number: "))
 s=int(input("Enter the second number: "))
 print(f/s)
a = 1		
while a>0:
 print("         Menu           ")
 print("------------------------")
 print("1.Addition   2.Subtraction")
 print("3.Multiplication   4.Division")
 print("0.Exit")
 a=int(input("Enter your choice: "))
 if a==1:
  add()
 elif a==2: 
  sub()
 elif a==3:
  mul()
 elif a==4:
  div()
 else:
  print("This is wrong")