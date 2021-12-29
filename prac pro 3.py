import math
print("welcome")
print("""
To find the area of
triangle enter 1
square enter 2
rectangle enter 3
circle enter 4
polygon enter 5

note units wont be metioned in the output


""")

a= int(input("enter the digit "))

if a==1:
  print("triangle")
  print("print which formula will you  use")
  print("""
   enter 1 for herons formula if only sides are give 
  enter 2 for general formula
 """ )
  b=int(input("enter ur choice of formula "))
  if b==1:
    print("using herons formula ")
    print ("enter the length of sides ")
    ab=int (input("enter the len of AB "))
    bc=int(input("enter the length  BC "))
    ca =int(input("enter the length CA"))
    s=(ab+bc+ca)/2
    artri1=(s(s-a)(s-b)(s-c))**1/2
    print("area of the triangle is  ",artri)
  if b==2:
    print("general formula")
    zx=int(input("enter heigth"))
    xv=int(input("enter base"))
    areagrtri=(zx*xv)/2
    print("area of the triangle is ", areagrtri)
if a==2:
  print("square ")
  ad=int(input("enter the len of one side "))
  areasq=ad*ad
  print("area of square ", areasq)
if a==3:
  print ("rectangle")
  ae=int (input("enter the length "))
  af=int(input("enter the base "))
  arearec=ae*af
  print("area of rectangle ",arearec)
if a==4:
  print("circle")
  rad=int(input("enter radius"))
  areacir=3.14*rad*rad
  print("area of circle ",areacir)
if a==5:
  print("polygon")
  nosides = int(input("Input number of sides: "))
  slength = float(input("Input the length of a side: "))
  polarea = nosides * (slength ** 2) / (4 * math.tan(3.14 / nosides) )
  print("area of polygon = ",polarea)
  
  
    
  
  
  

