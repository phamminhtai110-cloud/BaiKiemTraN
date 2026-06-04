cart_items = [
    ["1", "Xe may", "Nguyen Van A"],
    ["2", "O to", "Tran Van B"]
]

print("""
=======================================
 QUẢN LÝ BÃI XE - SMART PARKING
=======================================
1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Xóa xe ra khỏi bãi (khi xe ra)
4. Thoát chương trình
""")

while True:
    x = input("Nhập lựa chọn: ")

    if x == "4":
        print("Thoát chương trình...")
        break

    elif x == "1":
        print("Thêm xe mới vào bãi")

    elif x == "2":
        print("Hiển thị danh sách xe trong bãi")

        for item in cart_items:
            print(item)

    elif x == "3":
        print("Xóa xe ra khỏi bãi (khi xe ra)")

    else:
        print("Lựa chọn không hợp lệ!")
        continue
