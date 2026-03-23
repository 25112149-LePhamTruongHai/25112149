class NhanVien:
    LUONG_MAX = 50000000.0 

    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong):
        self.__ten_nhan_vien = ten_nhan_vien
        self.__luong_co_ban = luong_co_ban
        self.__he_so_luong = he_so_luong

    @property
    def ten_nhan_vien(self):
        return self.__ten_nhan_vien

    @ten_nhan_vien.setter
    def ten_nhan_vien(self, value):
        self.__ten_nhan_vien = value

    @property
    def luong_co_ban(self):
        return self.__luong_co_ban

    @luong_co_ban.setter
    def luong_co_ban(self, value):
        self.__luong_co_ban = value

    @property
    def he_so_luong(self):
        return self.__he_so_luong

    @he_so_luong.setter
    def he_so_luong(self, value):
        self.__he_so_luong = value

    def tinh_luong(self):
        return self.__luong_co_ban * self.__he_so_luong

    def in_thong_tin(self):
        luong_hien_tai = self.tinh_luong()
        print(f"--- THÔNG TIN NHÂN VIÊN ---")
        print(f"Tên: {self.__ten_nhan_vien}")
        print(f"Lương cơ bản: {self.__luong_co_ban:,.0f} VNĐ")
        print(f"Hệ số lương: {self.__he_so_luong}")
        print(f"Tổng lương: {luong_hien_tai:,.0f} VNĐ")

    def tang_luong(self, delta):
        he_so_moi = self.__he_so_luong + delta
        luong_moi = self.__luong_co_ban * he_so_moi
        
        if luong_moi > NhanVien.LUONG_MAX:
            print(f"!!! Lỗi: Lương mới ({luong_moi:,.0f}) vượt giới hạn cho phép!")
            return False
        else:
            self.__he_so_luong = he_so_moi
            print(f"Đã tăng hệ số lương lên: {self.__he_so_luong}")
            return True

nv1 = NhanVien("Trường Hải", 5000000, 2.5)
nv1.in_thong_tin()

print("\nThực hiện tăng lương (delta = 1.0):")
nv1.tang_luong(1.0)
nv1.in_thong_tin()

print("\nThực hiện tăng lương (delta = 10.0):")
nv1.tang_luong(10.0)
