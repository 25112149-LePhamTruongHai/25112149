class SieuNhan:
    def __init__(self, ten, vu_khi, mau_sac):
        self.ten = ten
        self.vu_khi = vu_khi
        self.mau_sac = mau_sac

    def hien_thi_thong_tin(self):
        return f"Siêu nhân {self.ten}: Vũ khí {self.vu_khi}, Màu sắc {self.mau_sac}"

sieu_nhan_A = SieuNhan("A", "kiếm", "đỏ")
sieu_nhan_B = SieuNhan("B", "khiên", "xanh")

print(sieu_nhan_A.hien_thi_thong_tin())
print(sieu_nhan_B.hien_thi_thong_tin())

