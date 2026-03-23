import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Rectangle:
    def __init__(self, width=0, height=0, corner=None):
        self.width = width
        self.height = height
        self.corner = corner 

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

def point_in_circle(circle, point):
    distance = math.sqrt((point.x - circle.center.x)**2 + 
                         (point.y - circle.center.y)**2)
    return distance <= circle.radius
    
def rect_in_circle(circle, rect):
    p = Point(rect.corner.x, rect.corner.y)
    if not point_in_circle(circle, p): return False
    
    # Kiểm tra góc trên trái
    p = Point(rect.corner.x, rect.corner.y + rect.height)
    if not point_in_circle(circle, p): return False
    
    p = Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    if not point_in_circle(circle, p): return False

    p = Point(rect.corner.x + rect.width, rect.corner.y)
    if not point_in_circle(circle, p): return False
    
    return True

def rect_circle_overlap(circle, rect):
    corners = [
        Point(rect.corner.x, rect.corner.y),
        Point(rect.corner.x + rect.width, rect.corner.y),
        Point(rect.corner.x, rect.corner.y + rect.height),
        Point(rect.corner.x + rect.width, rect.corner.y + rect.height)
    ]
    for p in corners:
        if point_in_circle(circle, p):
            return True
    return False

tam = Point(150, 100)
hinh_tron = Circle(tam, 75)

diem_test = Point(160, 110)
print(f"Điểm có nằm trong hình tròn không? {point_in_circle(hinh_tron, diem_test)}")

hinh_chu_nhat = Rectangle(30, 40, Point(140, 90))
print(f"Hình chữ nhật có nằm trọn trong hình tròn không? {rect_in_circle(hinh_tron, hinh_chu_nhat)}")
print(f"Hình chữ nhật có chạm vào hình tròn không? {rect_circle_overlap(hinh_tron, hinh_chu_nhat)}")
