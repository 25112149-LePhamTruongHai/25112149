from abc import ABC, abstractmethod
import json

class GiaKhongHopLe(Exception):
    """Ngoại lệ khi giá hàng hóa < 0"""
    pass

class MaHangTrungLap(Exception):
    """Ngoại lệ khi thêm mã hàng đã tồn tại"""
    pass

class HangHoa(ABC):
    def __init__(self, ma_hang, ten_hang, gia):
        self._ma_hang = ma_hang   
        self._ten_hang = ten_hang  
        self.gia = gia            

    @property
    def ma_hang(self):
        return self._ma_hang

    @property
    def ten_hang(self):
        return self._ten_hang

    @property
    def gia(self):
        return self._gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(f"Lỗi: Giá cho mặt hàng '{self.ten_hang}' không được < 0.")
        self._gia = value

    @abstractmethod
    def loai_hang(self):
        pass

    @abstractmethod
    def in_ttin(self):
        pass

    def __str__(self):
        """Dùng cho print(sp) hiển thị đẹp"""
        return f"[{self.loai_hang():<}] Mã: {self.ma_hang:} | Tên: {self.ten_hang:} | Giá: {self.gia:,.0f} VNĐ"

    def __eq__(self, other):
        """So sánh 2 hàng hóa theo mã hàng"""
        if not isinstance(other, HangHoa):
            return False
        return self.ma_hang == other.ma_hang

    def __lt__(self, other):
        """So sánh theo giá để dùng hàm sorted()"""
        return self.gia < other.gia

    def __hash__(self):
        """Dùng để lưu vào set() nếu cần"""
        return hash(self.ma_hang)

class HangDienMay(HangHoa):
    def loai_hang(self):
        return "Điện Máy"
    
    def in_ttin(self):
        print(f"THÔNG TIN ĐIỆN MÁY: {self}")

class HangSanhSu(HangHoa):
    def loai_hang(self):
        return "Sành Sứ"
    
    def in_ttin(self):
        print(f"THÔNG TIN SÀNH SỨ: {self}")

class HangThucPham(HangHoa):
    def loai_hang(self):
        return "Thực Phẩm"
    
    def in_ttin(self):
        print(f"THÔNG TIN THỰC PHẨM: {self}")

class QuanLyHangHoa:
    def __init__(self):
        self.danh_sach = []

    def them_hang(self, hang):
        # Kiểm tra trùng mã trước khi thêm
        if any(h.ma_hang == hang.ma_hang for h in self.danh_sach):
            raise MaHangTrungLap(f"Lỗi: Mã hàng '{hang.ma_hang}' đã tồn tại trong hệ thống!")
        self.danh_sach.append(hang)

    def hien_thi_tat_ca(self):
        print(f"{'='*80}")
        for sp in sorted(self.danh_sach):
            sp.in_ttin()
        print(f"{'='*80}")

    def luu_vao_file(self, filename):
        """Dùng context manager 'with open' để lưu file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                data = []
                for h in self.danh_sach:
                    data.append({
                        "loai": h.loai_hang(),
                        "ma": h.ma_hang,
                        "ten": h.ten_hang,
                        "gia": h.gia
                    })
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"-> Đã lưu {len(self.danh_sach)} mặt hàng vào file '{filename}' thành công.")
        except Exception as e:
            print(f"Lỗi khi lưu file: {e}")

    def doc_tu_file(self, filename):
        """Dùng context manager 'with open' để đọc file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data:
                    loai = item['loai']
                    if loai == "Điện Máy":
                        h = HangDienMay(item['ma'], item['ten'], item['gia'])
                    elif loai == "Sành Sứ":
                        h = HangSanhSu(item['ma'], item['ten'], item['gia'])
                    else:
                        h = HangThucPham(item['ma'], item['ten'], item['gia'])
                    self.them_hang(h)
            print(f"-> Đã tải dữ liệu từ file '{filename}' thành công.")
        except FileNotFoundError:
            print(f"Thông báo: File '{filename}' chưa tồn tại.")
        except Exception as e:
            print(f"Lỗi khi đọc file: {e}")

if __name__ == "__main__":
    ql = QuanLyHangHoa()

    try:
        ql.them_hang(HangDienMay("DM01", "Tủ lạnh LG", 12000000))
        print("\nDANH SÁCH HÀNG HÓA HIỆN TẠI:")
        ql.hien_thi_tat_ca()
        ql.luu_vao_file("inventory")


    except (GiaKhongHopLe, MaHangTrungLap) as e:
        print(f"NGOẠI LỆ XẢY RA: {e}")
    except Exception as e:
        print(f"Lỗi hệ thống: {e}")
