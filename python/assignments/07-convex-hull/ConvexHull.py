#  File: ConvexHull.py

#  Description: Assignment 07 | Convex Hull

#  Student Name: Matthew Maxwell

#  Student UT EID: mrm5632

#  Course Name: CS 313E

#  Unique Number: 50205

#  Date Created: 09-23-2019

#  Date Last Modified: 09-27-2019

import math

class Point (object):
  # constructor
  def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # equality tests of two Points
  def __eq__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

  def __ne__ (self, other):
    tol = 1.0e-8
    return ((abs(self.x - other.x) >= tol) or (abs(self.y - other.y) >= tol))

  def __lt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y < other.y)
    return (self.x < other.x)

  def __le__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y <= other.y)
    return (self.x <= other.x)

  def __gt__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return False
      else:
        return (self.y > other.y)
    return (self.x > other.x)

  def __ge__ (self, other):
    tol = 1.0e-8
    if (abs(self.x - other.x) < tol):
      if (abs(self.y - other.y) < tol):
        return True
      else:
        return (self.y >= other.y)
    return (self.x >= other.x)

# read points from input file, return sorted list of points
def getPoints():
    myFile = open("points.txt", "r")
    lines = [line.strip() for line in myFile]
    points = [Point(int(lines[i + 1].split("\t")[0]), int(lines[i + 1].split("\t")[1])) for i in range(int(lines[0]))]
    points.sort()
    myFile.close()
    return(points)

# compute and return the determinant of the coordinates of three points
# p, q, and r are Point objects
# NEGATIVE = right turn, POSITIVE = left turn, ZERO = same line
def det (p, q, r):
    return(((q.x * r.y) - (q.y * r.x)) - (p.x * (r.y - q.y)) + (p.y * (r.x - q.x)))

# computes and returns the convex hull of a sorted list of Points
# convex hull is a list of Point objects starting at the extreme
# left point and going clockwise in order
def convex_hull (sorted_points):
    upperHull = [] 
    upperHull.append(sorted_points[0])
    upperHull.append(sorted_points[1])
    for i in range(2, len(sorted_points)):
      upperHull.append(sorted_points[i])
      while(len(upperHull) >= 3 and det(upperHull[-3], upperHull[-2], upperHull[-1]) > 0):
        del upperHull[-2]

    lowerHull = []
    lowerHull.append(sorted_points[-1])
    lowerHull.append(sorted_points[-2])
    for i in range(len(sorted_points) - 3, -1, -1):
      lowerHull.append(sorted_points[i])
      while(len(lowerHull) >= 3 and det(lowerHull[-3], lowerHull[-2], lowerHull[-1]) > 0):
        del lowerHull[-2]

    lowerHull = lowerHull[1:-1]
    convexHull = upperHull
    [convexHull.append(point) for point in lowerHull]
    return(convexHull)

# compute and return the area of a convex polygon
# convex_poly is a list of Point objects that define the vertices
# of a convex polygon in order
def area_poly (convex_poly):
    convex_poly.append(convex_poly[0])
    # det = 0
    # for i in range(len(convex_poly) - 1):
    #   det += (convex_poly[i].x * convex_poly[i + 1].y) - (convex_poly[i].y * convex_poly[i + 1].x)
    det = sum([((convex_poly[i].x * convex_poly[i + 1].y) - (convex_poly[i].y * convex_poly[i + 1].x)) for i in range(len(convex_poly) - 1)])
    area = 0.5 * abs(det)   
    return(area)

def main():
    # get point data
    points = getPoints()
    #[print(point) for point in points]

    # get convex hull
    convexHull = convex_hull(points)
    print("Convex Hull")
    [print(point) for point in convexHull]
    print()

    # get convex polygon area
    convexHullArea = area_poly(convexHull)
    print("Area of Convex Hull = " + str(convexHullArea))

    #print(det(Point(-95, -98), Point(-96, -82), Point(-100, -33)))

main()