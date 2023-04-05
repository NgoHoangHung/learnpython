from Student import Student
import Controller


flag = True

while flag:
    print(f'''
                 ======================================================
                |                    Viindoo-school                    |
                 ======================================================
                |                [Lựa chọn:]                           |
                |                [1] Thêm sinh viên                    |
                |                [2] Cập nhật thông tin sinh viên      |
                |                [3] Thông tin sinh viên               |
                |                [4] Xóa sinh viên                     |
                |                [5] Thoát                             |
                 ======================================================
        ''')
    select = int(input("Mời chọn chức năng: "))

    if str(select).isdigit():
        select = int(select)
        if select == 1:
            Controller.add()
        if select == 2:
            Controller.edit()
        if select == 3:
            Controller.info()
        if select == 4:
            Controller.delete()
        if select == 5:
            break
    else:
        print("Nhập sai lựa chọn!")
