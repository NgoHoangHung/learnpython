import time
class Student:
    count = 0

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        Student.count+=1

    def get_id(self):
        return self.id

    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def set_Age(self, age):
        self.age = age

    def get_Age(self):
        return self.age

    def show_info(self):
        # for s in "[#####               ]25%\n[##########          ]50%\n[###############     ]75%\n[####################]100%\n":
        #     print(s, end='', flush=True)
        #     time.sleep(0.05)
        print(f"Id: {self.get_id()}")
        print(f"Name: {self.get_Name()}")
        print(f"Age: {self.get_Age()}")


sv = Student(1, "hung", 23)
sv1 = Student(2, "hung1", 25)
sv2 = Student(3, "hung2", 26)
# sv.show_info()
# print("Tổng số lượng học sinh:",Student.count)
