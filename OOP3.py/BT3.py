class SieuNhan:
    def __init__(self, ten, suc_manh, mau_sac):
        self.ten = ten
        self.suc_manh = suc_manh
        self.mau_sac = mau_sac

    def __str__(self):
        return f"Siêu nhân: {self.ten} | Sức mạnh: {self.suc_manh} | Màu: {self.mau_sac}"

danh_sach_sieu_nhan = []

print("--- CHƯƠNG TRÌNH QUẢN LÝ SIÊU NHÂN ---")
while True:
    ten = input("\nNhập tên siêu nhân ( gõ 'done' để dừng): ")
    if ten.lower() == 'done':
        break
        
    suc_manh = input(f"Nhập tuyệt chiêu của {ten}: ")
    mau_sac = input(f"Nhập màu sắc đại diện của {ten}: ")

    sn = SieuNhan(ten, suc_manh, mau_sac)
    danh_sach_sieu_nhan.append(sn)
    print(f"Đã thêm {ten} vào hệ thống!")

print("\n" + "="*35)
print(f"DANH SÁCH {len(danh_sach_sieu_nhan)} SIÊU NHÂN TOÀN THẾ GIỚI:")
print("="*35)

for index, sn in enumerate(danh_sach_sieu_nhan, start=1):
    print(f"{index}. {sn}")
