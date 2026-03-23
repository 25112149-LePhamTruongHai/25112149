class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self): return f"({self.x}, {self.y})"

class LineSegment:
    def __init__(self, d1=None, d2=None, x1=None, y1=None, x2=None, y2=None):
        # 1. Constructor 4 đối số nguyên: (int x1, int y1, int x2, int y2)
        if x1 is not None and y1 is not None:
            self.__d1 = Point(x1, y1)
            self.__d2 = Point(x2, y2)
        
        elif isinstance(d1, Point) and isinstance(d2, Point):
            self.__d1 = d1 
            self.__d2 = d2
            
        else:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

    @classmethod
    def from_copy(cls, other):
        new_d1 = Point(other.get_d1().x, other.get_d1().y)
        new_d2 = Point(other.get_d2().x, other.get_d2().y)
        return cls(d1=new_d1, d2=new_d2)

    def get_d1(self): return self.__d1
    def get_d2(self): return self.__d2

    def __str__(self):
        return f"Đoạn thẳng từ {self.__d1} đến {self.__d2}"


s1 = LineSegment() 
s2 = LineSegment.from_copy(s1)

s1.get_d1().x = 100
print(f"d1: {s1}") 
print(f"d2: {s2}") 
