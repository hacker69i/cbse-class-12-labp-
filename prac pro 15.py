stack =[]
maxcapacity=10
while(True):
  print("""
1.push value.
2.pop value.
3.print top value from stack.
4. print whole stack.
any other number to exit .
""")
  choice = int(input("enter your choice"))
  if (choice== 1):
    if (len(stack) == maxcapacity):
      print("stack overflow >>>___<<<<")
    else :
      val = int (input("enter ur element"))
      stack.append(val)
  elif (choice == 2):
    if(len(stack)==0):
      print("stack underflow")
    else:
      n=stack.pop()
      print(n,"removed from stack")
  elif (choice == 3):
    top = stack[-1]
    print("top of stack is ",top)
  elif(choice == 4):
    print("all elements of stack are",stack)
  else:
    break 
        
