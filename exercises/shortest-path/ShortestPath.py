import math

class Point (object):
  # constructor
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get the distance to another Point object
  def dist (self, other):
    return math.hypot (self.x - other.x, self.y - other.y)

  # string representation of a Point
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test for equality of two Point objects
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

def getPoints():
    myFile = open("points.txt", "r")
    points = []
    for line in myFile:
        line = line.strip()
        x = int(line.split("\t")[0])
        y = int(line.split("\t")[1])
        z = x * y
        print(z)
        point = Point(x, y)
        points.append(point)
        #print(point)
    return(points)

def getShortestDistance(points):
    shortestDistance = -1
    for i in range(len(points) - 1):
        for j in range(i + 1, len(points)):
            if(shortestDistance == -1):
                shortestDistance = points[i].dist(points[j])
            shortestDistance = min(shortestDistance, points[i].dist(points))
    print(shortestDistance)
    return(shortestDistance)


def main():
  # create an empty list of Point objects
  points = getPoints()

  shortestDistance = getShortestDistance(points)

main()
