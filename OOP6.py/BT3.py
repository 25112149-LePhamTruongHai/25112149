import math

class MauSoBangKhong(Exception):
    pass

class PhanSo:
    def __init__(self, tu=0, mau=1):
        self.tu_so = tu      
        self.mau_so = mau   

    @property
    def tu_so(self):
        return self.__tu
    
    @tu_so.setter
    def tu_so(self, value):
        self.__tu = value

    @property
    def mau_so(self):
        return self.__mau

    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong("Mẫu số không được bằng 0!")
        self.__mau = value

    def is_toi_gian(self):
        return math.gcd(self.tu_so, self.mau_so) == 1

    def toi_gian(self):
        common = math.gcd(self.tu_so, self.mau_so)
        new_tu = self.tu_so // common
        new_mau = self.mau_so // common
        if new_mau < 0:
            new_tu = -new_tu
            new_mau = -new_mau
        return PhanSo(new_tu, new_mau)

    def __add__(self, other):
        new_tu = self.tu_so * other.mau_so + other.tu_so * self.mau_so
        new_mau = self.mau_so * other.mau_so
        return PhanSo(new_tu, new_mau).toi_gian()

    def __sub__(self, other):
        new_tu = self.tu_so * other.mau_so - other.tu_so * self.mau_so
        new_mau = self.mau_so * other.mau_so
        return PhanSo(new_tu, new_mau).toi_gian()

    def __mul__(self, other):
        return PhanSo(self.tu_so * other.tu_so, self.mau_so * other.mau_so).toi_gian()

    def __truediv__(self, other):
        if other.tu_so == 0:
            raise ZeroDivisionError("Không thể chia cho phân số có tử bằng 0.")
        return PhanSo(self.tu_so * other.mau_so, self.mau_so * other.tu_so).toi_gian()

    def __eq__(self, other):
        return self.tu_so * other.mau_so == other.tu_so * self.mau_so

    def __lt__(self, other):
        return self.tu_so * other.mau_so < other.tu_so * self.mau_so

    def __gt__(self, other):
        return self.tu_so * other.mau_so > other.tu_so * self.mau_so

    def __str__(self):
        if self.mau_so == 1:
            return f"{self.tu_so}"
        return f"{self.tu_so}/{self.mau_so}"

    def __repr__(self):
        return f"PhanSo({self.tu_so}, {self.mau_so})"

    def __hash__(self):
        ps_tg = self.toi_gian()
        return hash((ps_tg.tu_so, ps_tg.mau_so))

if __name__ == "__main__":
    try:

        input_data = input("Nhập các phân số: ").split()
        danh_sach_ps = []
        
        for item in input_data:
            t, m = map(int, item.split('/'))
            danh_sach_ps.append(PhanSo(t, m))

        print("\n1. Danh sách phân số ở dạng tối giản:")
        for ps in danh_sach_ps:
            print(f"{ps} -> tối giản: {ps.toi_gian()}")

        print("\n2. Sắp xếp dãy phân số tăng dần:")
        for ps in sorted(danh_sach_ps):
            print(ps, end=" ")

        print("\n\n3. Loại bỏ các phân số trùng giá trị (dùng set):")
        tap_hop_ps = set(danh_sach_ps)
        for ps in tap_hop_ps:
            print(ps, end=" ")

    except MauSoBangKhong as e:
        print(f"Lỗi: {e}")
    except Exception as e:
        print(f"Lỗi nhập liệu: {e}. Vui lòng nhập đúng định dạng t/m.")
