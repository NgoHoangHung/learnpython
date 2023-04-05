import random

import json

students = []
from Student import Student


def checkId(id):
    # students = readData()
    left = 0
    right = len(students)
    if id > right:
        return False
    while left <= right:
        mid = (left + right) // 2
        if students[mid].id == id:
            return students[mid]
        elif students[mid].id < id:
            left = mid + 1
        else:
            right = mid - 1
    return None


def add():
    # students = readData()
    # with open('data.json', 'r') as json_file:
    #     data = json.load(json_file)
    id = len(students) + 1
    name = input("Nhập tên sinh viên: ")
    age = input("Nhập tuổi sinh viên: ")
    student = Student(id, name, age)
    students.append(student)


def edit(id):
    flag = False
    for i in students:
        if i.get_id == id:
            print(f'''
                1. Chỉnh tên
                2. Chỉnh tuổi
                3. Chỉnh cả hai
                4. Hủy
            ''')
        select = int(input("Mời chọn chức năng: "))
        if str(select).isdigit():
            select = int(select)
            if select == 1:
                name = input("Edit Name:")
                i.setName(name)
            if select == 2:
                age = input("Edit Age:")
                i.setAge(age)
            if select == 3:
                name = input("Edit Name:")
                i.setName(name)
                age = input("Edit Age:")
                i.setAge(age)
            if select == 4:
                break
        else:
            print("Nhập sai lựa chọn")
        flag = True
        print("")
    if not flag:
        print("Id không tồn tại")


def info():
    for i in students:
        print(i.get_id(),i.get_Name(),i.get_Age())


def delete(id):
    flag = False
    for i in students:
        if i.get_id == id:
            students.remove(i)
            flag = True
            print("Xóa thành công")
    if not flag:
        print("Xóa không thành công")

def readData():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        students = []
        for obj in data:
            id = obj['id']
            name = obj['name']
            age = obj['age']
            student = Student(id, name, age)
            students.append(student)


def writeData(data):
    with open('data.json', 'w'):
        try:
            json.dump([s.__dict__ for s in data])
            # data, json_file)
        except TypeError as e:
            print("Error:", e)
