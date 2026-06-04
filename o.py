parking_lot = []
next_id = 1

while True:
    print("""
=======================================
      QUẢN LÝ BÃI XE - SMART PARKING
=======================================
1. Thêm xe mới vào bãi
2. Hiển thị danh sách xe trong bãi
3. Xóa xe ra khỏi bãi
4. Thoát chương trình
=======================================
""")

    choice = input("Nhập lựa chọn: ").strip()

    # Chức năng 1: Thêm xe
    if choice == "1":

        while True:
            vehicle_type = input("Nhập loại xe: ").strip()
            if vehicle_type != "":
                break
            print("Loại xe không được để trống!")

        while True:
            owner = input("Nhập tên chủ xe: ").strip()
            if owner != "":
                break
            print("Tên chủ xe không được để trống!")

        vehicle = {
            "id": next_id,
            "type": vehicle_type,
            "owner": owner
        }

        parking_lot.append(vehicle)

        print(f"Đã thêm xe ID {next_id} thành công!")

        next_id += 1

    # Chức năng 2: Hiển thị
    elif choice == "2":

        if len(parking_lot) == 0:
            print("Bãi xe hiện đang trống!")

        else:
            print("\n{:<5} {:<20} {:<25}".format(
                "ID", "Loại xe", "Chủ xe"))
            print("-" * 55)

            for vehicle in parking_lot:
                print("{:<5} {:<20} {:<25}".format(
                    vehicle["id"],
                    vehicle["type"],
                    vehicle["owner"]
                ))

    # Chức năng 3: Xóa xe
    elif choice == "3":

        if len(parking_lot) == 0:
            print("Bãi xe hiện đang trống!")
            continue

        try:
            delete_id = int(input("Nhập ID xe cần xóa: "))

            found = False

            for vehicle in parking_lot:
                if vehicle["id"] == delete_id:
                    parking_lot.remove(vehicle)
                    print(f"Đã xóa xe ID {delete_id} thành công!")
                    found = True
                    break

            if not found:
                print("Không tìm thấy xe để xóa!")

        except ValueError:
            print("ID phải là số nguyên!")

    # Chức năng 4: Thoát
    elif choice == "4":
        print("Thoát chương trình...")
        break

    else:
        print("Lựa chọn không hợp lệ!")
