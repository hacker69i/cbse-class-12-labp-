Students = ['Harsh', 'Andrew', 'Danny']
vole=['a','e','i','o','u','e','i','o','u,'u'']
print (Students)
print(vole)
print ("enter the digit of the  funtion u want to run  ")

print ("""

enter 1 for sort
enter 2 for reverse
enter 3 to  find index value
enter 4 to pop
enter 5 to count 

""")
b=int(input("enter the digit: "))
if b==1:
  Students.sort()
  print(Students)
if b==2:
  Students.reverse()
  print(Students)
if b==3:
  print(students)
  a=str(input("enter the name for which ur finding index value "))
  print(Students.index(a))
if b==4:
  c=int(input("enter the index val of the element "))
  print(Students)
  Students.pop(c)
  print("element with index value",c,"was ejected ")
  print(Students)
if b==5:
  print(vole)
  j=str(input("which element u want to count "))
  count = vole.count(j)
  print("the count of ", j,"is ",count)


 



