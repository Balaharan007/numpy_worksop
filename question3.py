#write a program to find the factorial of a nummber

n=int(input("enter the no:"))

def fact(n):
  if(n==0):
    return 1
  else:
    return n*fact(n-1)
  
 print(def(n)) 