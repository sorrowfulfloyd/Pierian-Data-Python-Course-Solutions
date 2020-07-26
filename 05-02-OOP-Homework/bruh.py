from math import sqrt, pi

# Problem 1

# Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:
    def __init__(self,c1,c2):
        self.c1 = c1
        self.c2 = c2
    def distance(self):

        x1,y1 = self.c1
        x2,y2 = self.c2

        return(sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))
    def slope(self):

        x1,y1 = self.c1
        x2,y2 = self.c2

        return((y2 - y1) / (x2 - x1))

c1 = (3,2)
c2 = (8,10)

li = Line((3,2),(8,10))
print(li.distance())
print(li.slope())

# Problem 2

# Bruh moment

class Cylinder:
    def __init__ (self, h=1,r=1):
        self.h = h
        self.r = r
    def volume(self):
        return (round((self.h * pi * pow(self.r, 2)), 2))
    def surface_area(self):
        return (round((2 * pi * self.r * self.h) + (2 * pi * pow(self.r, 2)), 1))

cyl = Cylinder(2,3)
print(cyl.volume())
print(cyl.surface_area())