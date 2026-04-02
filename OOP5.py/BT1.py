class HangHoa:
    def __init__(self, ma_hang, ten_hang, nha_sx, gia):
        self.ma_hang = ma_hang
        self.ten_hang = ten_hang
        self.nha_sx = nha_sx
        self.gia = gia

    def hien_thi(self):
        print(f"Mã hàng: {self.ma_hang}")
        print(f"Tên hàng: {self.ten_hang}")
        print(f"Nhà sản xuất: {self.nha_sx}")
        print(f"Giá: {self.gia}")

class HangDienMay(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, tg_bao_hanh, dien_ap, cong_suat):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.tg_bao_hanh = tg_bao_hanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

    def hien_thi(self):
        super().hien_thi()
        print(f"Thời gian bảo hành: {self.tg_bao_hanh}")
        print(f"Điện áp: {self.dien_ap}")
        print(f"Công suất: {self.cong_suat}")
        print("-" * 30)

class HangSanhSu(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, loai_nguyen_lieu):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.loai_nguyen_lieu = loai_nguyen_lieu

    def hien_thi(self):
        super().hien_thi()
        print(f"Loại nguyên liệu: {self.loai_nguyen_lieu}")
        print("-" * 30)

class HangThucPham(HangHoa):
    def __init__(self, ma_hang, ten_hang, nha_sx, gia, ngay_sx, ngay_het_han):
        super().__init__(ma_hang, ten_hang, nha_sx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_het_han = ngay_het_han

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngày sản xuất: {self.ngay_sx}")
        print(f"Ngày hết hạn: {self.ngay_het_han}")
        print("-" * 30)

hang1 = HangDienMay("DM01", "Tivi", "Sony", 15000000, "24 tháng", "220V", "150W") 
hang1.hien_thi()
hang2 = HangSanhSu("SS01", "Bát sứ", "Minh Long", 50000, "Gốm cao cấp") 
hang2.hien_thi()
hang3 = HangThucPham("TP01", "Sữa", "Vinamilk", 30000, "01/01/2026", "01/07/2026")
hang3.hien_thi()


