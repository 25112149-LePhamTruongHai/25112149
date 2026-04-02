class NhanVien:
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.gioi_tinh = gioi_tinh
        self.dia_chi = dia_chi
        self.he_so_luong = he_so_luong if he_so_luong > 0 else 1
        self.luong_toi_da = luong_toi_da

    def tinh_luong(self):
        return self.he_so_luong * self.luong_toi_da

    def hien_thi(self):
        print(f"Mã NV: {self.ma_nv}")
        print(f"Họ tên: {self.ho_ten}")
        print(f"Năm sinh: {self.nam_sinh}")
        print(f"Giới tính: {self.gioi_tinh}")
        print(f"Địa chỉ: {self.dia_chi}")
        print(f"Lương: {self.tinh_luong()}")


class CongTacVien(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da,
                 thoi_han_hop_dong, phu_cap):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.thoi_han_hop_dong = thoi_han_hop_dong
        self.phu_cap = phu_cap

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap

    def hien_thi(self):
        super().hien_thi()
        print(f"Thời hạn HĐ: {self.thoi_han_hop_dong}")
        print(f"Phụ cấp: {self.phu_cap}")
        print("-" * 30)

class NhanVienChinhThuc(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da,
                 vi_tri_cong_viec):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.vi_tri_cong_viec = vi_tri_cong_viec

    def hien_thi(self):
        super().hien_thi()
        print(f"Vị trí: {self.vi_tri_cong_viec}")
        print("-" * 30)

class TruongPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da,
                 ngay_bat_dau, phu_cap_quan_ly):
        super().__init__(ma_nv, ho_ten, nam_sinh, gioi_tinh, dia_chi, he_so_luong, luong_toi_da)
        self.ngay_bat_dau = ngay_bat_dau
        self.phu_cap_quan_ly = phu_cap_quan_ly

    def tinh_luong(self):
        return super().tinh_luong() + self.phu_cap_quan_ly

    def hien_thi(self):
        super().hien_thi()
        print(f"Ngày bắt đầu QL: {self.ngay_bat_dau}")
        print(f"Phụ cấp QL: {self.phu_cap_quan_ly}")
        print("-" * 30)

nv1 = CongTacVien("CT01", "An", 2000, "Nam", "HN", 2.5, 1500000, "6 tháng", 500000)
nv1.hien_thi()
nv2 = NhanVienChinhThuc("NV01", "Bình", 1998, "Nam", "HCM", 3.0, 1500000, "Kỹ sư")
nv2.hien_thi()
nv3 = TruongPhong("TP01", "Cường", 1985, "Nam", "ĐN", 4.0, 1500000, "01/01/2020", 2000000)
nv3.hien_thi()


