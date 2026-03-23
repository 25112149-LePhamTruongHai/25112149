import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def hiển_thị(self, tên="Điểm"):
        print(f"{tên}({self.x}, {self.y})")

    def khoảng_cách_gốc_O(self):
        return math.sqrt(self.x**2 + self.y**2)

    def khoảng_cách_đến(self, điểm_khác):
        return math.sqrt((self.x - điểm_khác.x)**2 + (self.y - điểm_khác.y)**2)

A = Point(3, 4)
A.hiển_thị("A")

print("\nNhập tọa độ cho điểm B:")
x_b = int(input("Nhập x: "))
y_b = int(input("Nhập y: "))
B = Point(x_b, y_b)
B.hiển_thị("B")

C = Point(-B.x, -B.y)
C.hiển_thị("C (đối xứng B qua O)")

d_BO = B.khoảng_cách_gốc_O()
print(f"\nKhoảng cách từ B đến O: {d_BO:.2f}")

d_AB = A.khoảng_cách_đến(B)
print(f"Khoảng cách từ A đến B: {d_AB:.2f}")
