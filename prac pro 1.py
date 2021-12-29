import random
print ("enter the digit of the  funtion u want to run  ")
print("""
1 for random 
2 for randint
3 for randrange

""")

a=int(input("enter the digit"))



if a==1:
 print( random.random())
  


  
if a==2:
  print("Random integer from 0 to 9")
  num1 = random.randint(0, 9)
  print("Random integer: ", num1)
if a==3:
  print ("Random number from 0-100 is : ",end="")
  print(random.randrange(100))
