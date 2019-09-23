#  File: OfficeSpace.py

#  Description: Assignment 06 | Office Space

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-23-2019

#  Date Last Modified: 09-23-2019

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

class Rectangle (object):
  # constructor
  def __init__ (self, ll_x = 0, ll_y = 0, ur_x = 1, ur_y = 1):
    if ((ll_x < ur_x) and (ll_y < ur_y)):
      self.ll = Point (ll_x, ll_y)
      self.ur = Point (ur_x, ur_y)
    else:
      self.ll = Point (0, 0)
      self.ur = Point (1, 1)

  # determine length of Rectangle (distance along the x axis)
  # takes no arguments, returns a float
  def length (self):
    return(self.ur.x - self.ll.x)

  # determine width of Rectangle (distance along the y axis)
  # takes no arguments, returns a float
  def width (self):
    return(self.ur.y - self.ll.y)

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
    return(self.ur.x > p.x > self.ll.x and self.ur.y > p.y > self.ll.y)

  # determine if another Rectangle is strictly inside this Rectangle
  # takes a rectangle object r as an argument, returns a boolean
  # should return False if self and r are equal
  def rectangle_inside (self, r):
    return(self.ll.x < r.ll.x < r.ur.x < self.ur.x and self.ll.y < r.ll.y < r.ur.y < self.ur.y)

  # determine if two Rectangles overlap (non-zero area of overlap)
  # takes a rectangle object r as an argument returns a boolean
  def rectangle_overlap (self, r):
      print("FIXME: Complete rectangle overlap function...")
      return(-1)

  # give string representation of a rectangle
  # takes no arguments, returns a string
  def __str__ (self):
    return "LL: " + str(self.ll) + ", UR: " + str(self.ur)

  # determine if two rectangles have the same length and width
  # takes a rectangle other as argument and returns a boolean
  def __eq__ (self, other):
    return(self.ll == other.ll and self.ur == other.ur)

# read data from file
def readFile():
    myFile = open("office.txt", "r")
    data = []
    lines = [line.strip() for line in myFile]
    for i in range(len(lines)):
        if(i == 0):
            points = lines[i].split(" ")
            data.append((int(points[0]), int(points[1])))
        if(i == 1):
            for j in range(2, 2 + int(lines[i])):
                employee = lines[j].split(" ")
                name = employee[0]
                requestedSpace = Rectangle(int(employee[1]), int(employee[2]), int(employee[3]), int(employee[4]))
                data.append([name, requestedSpace])
    myFile.close()
    [print(item) for item in data]
    return(data)

# print data according to format
def printData(myData):
    totalArea = myData[0][0] * myData[0][1]
    # total area of office space (x times y)
    print("Total " + str(totalArea))
    # unallocated area of office space (total minus area of squares)
    totalRequestedArea = sum([employee[1].area() for employee in myData[1:]])
    print("FIXME: Unallocated office space is " + str(totalArea - totalRequestedArea))
    # contested area of office space (find total area of rectangular overlap)
    print("FIXME: Contested office space")
    # each employee with guaranteed space (original request minus contested) * same order as input
    for employee in myData[1:]:
        print("FIXME: " + employee[0] + "'s guaranteed space is " + str(employee[1].area()))

def main():
    myData = readFile()
    printData(myData)

main()