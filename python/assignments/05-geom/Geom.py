#  File: Geom.py

#  Description: Assignment 05 | Geom.py

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-17-2019

#  Date Last Modified: 09-07-2019

import math

class Point (object):
  # constructor 
  # x and y are floats
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance
  # other is a Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # get a string representation of a Point object
  # takes no arguments
  # returns a string
  def __str__ (self):
    return '(' + str(self.x) + ", " + str(self.y) + ")"

  # test for equality
  # other is a Point object
  # returns a Boolean
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs (self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Circle (object):
  # constructor
  # x, y, and radius are floats
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point (x, y)

  # compute cirumference
  def circumference (self):
    return 2.0 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius * self.radius

  # determine if point is strictly inside circle
  def point_inside (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if a circle is strictly inside this circle
  def circle_inside (self, c):
    distance = self.center.dist (c.center)
    return (distance + c.radius) < self.radius

  # determine if a circle c overlaps this circle (non-zero area of overlap)
  # but neither is completely inside the other
  # the only argument c is a Circle object
  # returns a boolean
  def circle_overlap (self, c):
    distance = self.center.dist(c.center)
    if(distance < self.radius + c.radius and self.circle_inside(c) != True):
      return(True)
    return(False)
   
  # determine the smallest circle that circumscribes a rectangle
  # the circle goes through all the vertices of the rectangle
  # the only argument, r, is a rectangle object
  def circle_circumscribe (self, r):
    center = Point(r.lr.x - (r.length () / 2), r.ul.y - (r.width() / 2))
    return(Circle(center.dist(Point(r.lr.x, r.ul.y)), center.x, center.y))

  # string representation of a circle
  # takes no arguments and returns a string
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: " + str(self.center)
    
  # test for equality of radius
  # the only argument, other, is a circle
  # returns a boolean
  def __eq__ (self, other):
    tol = 1.0e-8
    return(abs(self.radius - other.radius) < tol)

class Rectangle (object):
  # constructor
  def __init__ (self, ul_x = 0, ul_y = 1, lr_x = 1, lr_y = 0):
    if ((ul_x < lr_x) and (ul_y > lr_y)):
      self.ul = Point (ul_x, ul_y)
      self.lr = Point (lr_x, lr_y)
    else:
      self.ul = Point (0, 1)
      self.lr = Point (1, 0)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return(self.lr.x - self.ul.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return(self.ul.y - self.lr.y)

  # determine the perimeter
  # takes no arguments, returns a float
  def perimeter (self):
    return(2 * (self.length() + self.width()))
    
  # determine the area
  # takes no arguments, returns a float
  def area (self):
    return(self.length() * self.width())

  # determine if a point is strictly inside the Rectangle
  # takes a point object p as an argument, returns a boolean
  def point_inside (self, p):
    return(self.lr.x > p.x and p.x > self.ul.x and self.ul.y > p.y and p.y > self.lr.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    return(r.ul.x > self.ul.x and r.ul.y < self.ul.y and r.lr.x < self.lr.x and r.lr.y > self.lr.y)

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
    if(self.rectangle_inside(r)):
      return(False)
    elif(self.point_inside(r.ul) or self.point_inside(r.lr) or self.point_inside(Point(r.ul.x, r.lr.y)) or self.point_inside(Point(r.lr.x, r.ul.y))):
      return(True)
    elif((self.ul.x < r.ul.x and r.ul.x < r.lr.x and r.lr.x < self.lr.x) and (r.lr.y < self.lr.y and self.lr.y < self.ul.y and self.ul.y < r.ul.y)):
      return(True)
    elif((r.ul.x < self.ul.x and self.ul.x < self.lr.x and self.lr.x < r.lr.x) and (self.lr.y < r.lr.y and r.lr.y < r.ul.y and r.ul.y < self.ul.y)):
      return(True)
    return(False)

  # determine the smallest rectangle that circumscribes a circle
  # sides of the rectangle are tangents to circle c
  # takes a circle object c as input and returns a rectangle object
  def rectangle_circumscribe (self, c):
    return(Rectangle(c.center.x - c.radius, c.center.y + c.radius, c.center.x + c.radius, c.center.y - c.radius))

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "UL: " + str(self.ul) + ", LR: " + str(self.lr)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    return(self.ul == other.ul and self.lr == other.lr)

# Read file's data
def readFile():
  #file = open("geom.txt", "r")
  file = open(r"c:/users/matt/documents/school/2019/fall/cs-313e/assignments/5-geom/geom.txt", "r")
  lineIndex = 0
  variables = []
  for line in file: 
    line = line.strip()
    lineItems = line.split(" ")
    if(lineIndex <= 1):
      variables.append(Point(float(lineItems[0]), float(lineItems[1])))
    elif(1 < lineIndex <= 3):
      variables.append(Circle(float(lineItems[0]), float(lineItems[1]), float(lineItems[2])))
    elif(3 < lineIndex <= 5):
      variables.append(Rectangle(float(lineItems[0]), float(lineItems[1]), float(lineItems[2]), float(lineItems[3])))
    lineIndex += 1
  file.close()
  return(variables[0], variables[1], variables[2], variables[3], variables[4], variables[5])

def main():
  # Open the file geom.txt
  P, Q, C, D, G, H = readFile()

  # Print the coordinates of the points P and Q
  print("Coordinates of P: " + str(P))
  print("Coordinates of Q: " + str(Q))

  # Find the distance between the points P and Q
  print("Distance between P and Q: " + str(P.dist(Q)))

  # Print C and D
  print("Circle C: " + str(C))
  print("Circle D: " + str(D))

  # Compute the circumference of C
  print("Circumference of C: " + str(C.circumference()))

  # Compute the area of D
  print("Area of D: " + str(D.area()))

  # Determine if P is strictly inside C
  if(C.point_inside(P)):
    print("P is inside C")
  else:
    print("P is not inside C")

  # determine if C is strictly inside D
  if(D.circle_inside(C)):
    print("C is inside D")
  else:
    print("C is not inside D")

  # determine if C and D intersect (non zero area of intersection)
  if(D.circle_overlap(C)):
    print("C does intersect D")
  else:
    print("C does not intersect D")

  # Determine if C and D are equal (have the same radius)
  if(C == D):
    print("C is equal to D")
  else:
    print("C is not equal to D")

  # print the two rectangles G and H
  print("Rectangle G: " + str(G))
  print("Rectangle H: " + str(H))

  # Determine the length of G (distance along x axis)
  print("Length of G: " + str(G.length()))

  # Determine the width of H (distance along y axis)
  print("Width of H: " + str(H.width()))

  # Determine the perimeter of G
  print("Perimeter of G: " + str(G.perimeter()))

  # Determine the area of H
  print("Area of H: " + str(H.area()))

  # Determine if point P is strictly inside rectangle G
  if(G.point_inside(P)):
    print("P is inside G")
  else:
    print("P is not inside G")

  # Determine if rectangle G is strictly inside rectangle H
  if(H.rectangle_inside(G)):
    print("G is inside H")
  else:
    print("G is not inside H")

  # Determine if rectangles G and H overlap (non-zero area of overlap)
  if(G.rectangle_overlap(H)):
    print("G does overlap H")
  else:
    print("G does not overlap H")

  # Find the smallest circle that circumscribes rectangle G
  # goes through the four vertices of the rectangle
  print("Circle that circumscribes G: " + str(C.circle_circumscribe(G)))

  # Find the smallest rectangle that circumscribes circle D
  # all four sides of the rectangle are tangents to the circle
  print("Rectangle that circumscribes D: " + str(H.rectangle_circumscribe(D)))

  # Determine if the two rectangles have the same length and width
  if(G == H):
    print("Rectangle G is equal to H")
  else:
    print("Rectangle G is not equal to H")

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
  main()