# code 1:

"""

def happy_birthday(name):
  print("Happy brithday to you,")
  print("Happy brithday to you,")
  print("Happy brithday, Happy Birthday ")
  print("Happy brithday ", name)
  
name1 = input("What is your name")
happy_birthday(name1)

"""

#code 2

PI = 3.141
def area(radius):
  
  radius_squared = radius*radius
  area = PI * radius_squared
  return area

def circumference(radius):
  diameter = radius * 2
  circumference = PI * diameter
  return circumference 
  
def printing(area,circumference):
  print( "The area is", area_returned)
  print( "The circumference is", circumference_returned)
  

radius = int(input("Please enter a radius"))
area_returned = area(radius)
circumference_returned = circumference(radius)
printing (area,circumference)
#print(area_returned)


  
  


  
  
