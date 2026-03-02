import math



class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def distance_from_xy(self, x, y):
        dis = math.sqrt(((self.x-x)**2) + ((self.y-y)**2))
        return dis

    def distance_from_point(self, point):
        x2=point.getx()
        y2=point.gety()
        return math.sqrt(((self.x-x2)**2)+((self.y-y2)**2))
class Triangle(Point):
    def __init__(self, vertice1, vertice2, vertice3):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3

    def perimeter(self):
        s1 = self.vertice1.distance_from_point(self.vertice2)
        s2 = self.vertice2.distance_from_point(self.vertice3)
        s3 = self.vertice3.distance_from_point(self.vertice1)
        return s1 + s2 + s3


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
