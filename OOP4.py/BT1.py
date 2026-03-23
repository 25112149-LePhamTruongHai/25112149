class NhanVien:
    LUONG_MAX = 20000000.0
    def __init__(self, ten_nhan_vien, luong_co_ban, he_so_luong):
        self._ten_nhan_vien = ten_nhan_vien
        self._luong_co_ban = luong_co_ban
        self._he_so_luong = he_so_luong

    @property
    def ten_nhan_vien(self):
        return self._ten_nhan_vien

    @ten_nhan_vien.setter
    def ten_nhan_vien(self, value):
        self._ten_nhan_vien = value

    @property
    def luong_co_ban(self):
        return self._luong_co_ban

    @luong_co_ban.setter
    def luong_co_ban(self, value):
        self._luong_co_ban = value

    @property
    def he_so_luong(self):
        return self._he_so_luong

    @he_so_luong.setter
    def he_so_luong(self, value):
        self._he_so_luong = value

    def tinh_luong(self):
        """Lương = Lương cơ bản * Hệ số lương"""
        return self._luong_co_ban * self._he_so_luong

    def tang_luong(self, he_so_tang):
        """Tăng hệ số lương nếu tổng lương mới không vượt quá LUONG_MAX"""
        he_so_moi = self._he_so_luong + he_so_tang
        luong_moi = self._luong_co_ban * he_so_moi

        if luong_moi > NhanVien.LUONG_MAX:
            print(f"Lỗi: Lương mới ({luong_moi:,.0f}) vượt mức tối đa {NhanVien.LUONG_MAX:,.0f}. Không thay đổi.")
            return False
        else:
            self._he_so_luong = he_so_moi
            return True

    def in_ttin(self):
        """Hiển thị thông tin nhân viên"""
        print("-" * 30)
        print(f"Nhân viên: {self._ten_nhan_vien}")
        print(f"Hệ số lương: {self._he_so_luong}")
        print(f"Lương hiện tại: {self.tinh_luong():,.0f} VND")

nv1 = NhanVien("Toàn", 5000000, 2.0)
nv1.in_ttin()

print("\nĐang thực hiện tăng hệ số thêm 1.5...")
if nv1.tang_luong(1.5):
    print("Tăng lương thành công!")
nv1.in_ttin()

print("\nĐang thực hiện tăng hệ số thêm 5.0...")
nv1.tang_luong(5.0)
