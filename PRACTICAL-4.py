Bal=0

A=str(input("Enter transaction Type and Amount: "))

list=[]
list=A.split()
t=list[0]
a=int(list[1])


if t=="D" or t=="d":
  Bal=Bal+a
  print("Balance is:",Bal)

  
elif t=="W" or t=="w":
   if a>Bal:
         print("Not sufficiant balance ")

   
else:
   Bal=Bal-a
   print("Balance is:",Bal)

