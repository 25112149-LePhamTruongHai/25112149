from abc import ABC, abstractmethod

class TuoiKhongHopLe(Exception): pass
class BacKhongHopLe(Exception): pass

class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi 
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    @property
    def tuoi(self): return self._tuoi
    @tuoi.setter
    def tuoi(self, v):
        if not (18 <= v <= 65): raise TuoiKhongHopLe(f"Tuổi {v} sai")
        self._tuoi = v

    @abstractmethod
    def mo_ta(self): pass

    def __str__(self):
        return f"{self.ho_ten:15} | {self.tuoi} | {self.gioi_tinh} | {self.dia_chi}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.ho_ten}', {self.tuoi}, '{self.gioi_tinh}', '{self.dia_chi}')"

    def __lt__(self, other):
        return self.ho_ten.split()[-1] < other.ho_ten.split()[-1]

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    def mo_ta(self): return f"Công nhân bậc {self.bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh
    def mo_ta(self): return f"Kỹ sư ngành {self.nganh}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec
    def mo_ta(self): return f"Nhân viên: {self.cong_viec}"

ds = [
    CongNhan("Nguyen Van An", 30, "Nam", "HN", 5),
    KySu("Tran Thi Binh", 28, "Nu", "HCM", "CNTT"),
    NhanVien("Le Van Cuong", 35, "Nam", "DN", "Ke toan")
]

print("--- Danh sách cán bộ: ---")
for cb in sorted(ds):
    print(f"{cb} -> {cb.mo_ta()}")

ten_can_tim = "Binh"
print(f"\n--- Kết quả tìm kiếm cho từ khóa '{ten_can_tim}': ---")
kq = [cb for cb in ds if ten_can_tim.lower() in cb.ho_ten.lower()]
for item in kq:
    print(item)

with open("canbo.txt", "w", encoding="utf-8") as f:
    for cb in ds:
        f.write(repr(cb) + "\n")
