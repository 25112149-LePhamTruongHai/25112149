class Dog:
    def __init__(self, name, color, breed, mood):
        # Thuộc tính (Attributes)
        self.name = name
        self.color = color
        self.breed = breed
        self.mood = mood

    def show_info(self):
        print(f"--- THÔNG TIN CHÚ CHÓ ---")
        print(f"Tên: {self.name} | Giống: {self.breed} | Màu sắc: {self.color} | Tâm trạng: {self.mood}")

    def bark(self):
        print(f"{self.name} đang sủa gâu gâu!")

    def wag_tail(self):
        print(f"{self.name} đang vẫy đuôi mừng chủ.")

    def run(self):
        print(f"{self.name} đang chạy tung tăng!")
    
    def eat(self):
        self.is_hungry = False
        self.mood = "Vui vẻ"
        print(f"{self.name} đã ăn. Hết đói và thấy {self.mood}!")

dog1 = Dog("Ki", "Vàng", "Poodle", "Vui vẻ")
dog1.show_info()
dog1.bark()
dog1.run()
dog1.eat()

class Car:
    def __init__(self, brand, size, color, price):
        self.brand = brand
        self.size = size
        self.color = color
        self.price = price
        self.speed = 0

    def show_info(self):
        print(f"--- THÔNG TIN XE Ô TÔ ---")
        print(f"Hãng: {self.brand} | Kích thước: {self.size} | Màu: {self.color} | Giá: ${self.price:,}")

    def accelerate(self, kmh):
        self.speed += kmh
        print(f"Xe {self.brand} đang tăng tốc. Tốc độ hiện tại: {self.speed} km/h")

    def decelerate(self, kmh):
        self.speed = max(0, self.speed - kmh)
        print(f"Xe {self.brand} giảm tốc độ xuống còn: {self.speed} km/h")

    def crash(self):
        self.speed = 0
        print("Xe đã xảy ra va chạm và dừng lại.")

car1 = Car("Porsche", "Thể thao", "Đen", 120000)
car1.show_info()
car1.accelerate(100)
car1.decelerate(40)
car1.crash()

class BankAccount:
    def __init__(self, owner, acc_num, bank, balance):
        self.owner = owner
        self.acc_num = acc_num
        self.bank = bank
        self.balance = balance

    def show_info(self):
        print(f"--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Chủ TK: {self.owner}")
        print(f"Số TK: {self.acc_num} tại {self.bank}")
        print(f"Số dư: {self.balance:,} VNĐ")

    def deposit(self, amount):
        self.balance += amount
        print(f"Đã nạp {amount:,} VNĐ. Số dư mới: {self.balance:,} VNĐ")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Đã rút {amount:,} VNĐ. Số dư còn lại: {self.balance:,} VNĐ")
        else:
            print("Giao dịch thất bại: Số dư không đủ!")

    def check_balance(self):
        print(f"Số dư hiện tại của {self.owner} là: {self.balance:,} VNĐ")

acc1 = BankAccount("Hải", "99998888", "MB Bank", 5000000)
acc1.show_info()
acc1.deposit(2000000)
acc1.withdraw(1500000)
acc1.check_balance()
