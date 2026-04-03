class CanBo:
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.ho_ten = ho_ten
        self.tuoi = tuoi
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi

    def hien_thi(self):
        print(f"Họ tên: {self.ho_ten}, Tuổi: {self.tuoi}, "
              f"Giới tính: {self.gioi_tinh}, Địa chỉ: {self.dia_chi}")

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac

    def hien_thi(self):
        super().hien_thi()
        print(f"Bậc: {self.bac}")

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.nganh = nganh

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngành đào tạo: {self.nganh}")
      
class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.cong_viec = cong_viec

    def hien_thi(self):
        super().hien_thi()
        print(f"Công việc: {self.cong_viec}")

class QLCB:
    def __init__(self):
        self.danh_sach = []

    def them(self, can_bo):
        self.danh_sach.append(can_bo)

    def tim_kiem(self, ten):
        print("Kết quả tìm kiếm:")
        for cb in self.danh_sach:
            if ten.lower() in cb.ho_ten.lower():
                cb.hien_thi()
                print("-" * 30)

    def hien_thi(self):
        print("Danh sách cán bộ:")
        for cb in self.danh_sach:
            cb.hien_thi()
            print("-" * 30)

ql = QLCB()
ql.them(CongNhan("An", 30, "Nam", "HN", 5))
ql.them(KySu("Bình", 28, "Nam", "HCM", "CNTT"))
ql.them(NhanVien("Cường", 25, "Nam", "ĐN", "Kế toán"))
ql.hien_thi()
ql.tim_kiem("An")
