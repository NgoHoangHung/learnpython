# n = int(input())
# result = 0.0
# i = 1
# while i < n:
#     result += float(i/i+1)
#     i+=1
# print(round(result,2))
#
# n = int(input())
# result = 0
# for i in range(1,n+1)
#     result += i/(i+1)
# print(round(result,2))
# n = int(intput())
# lst = []
# resultList = []
# for i in range(n):
#     lst.append(int(input()))
# for i in lst:
#     if i &1 ==1:
#         resultList.append(i)
# print(resultList)        
# s = """
# Banana
# Apple
# Orange
# """
# print(s)
# from pip._vendor.rich.__main__ import message

# message = "   Welcome   to Codelearn.io!   "
# print(" ".join(message.split()))

# s = "codelearn"
# print(s.isalpha())
# # Kết quả sẽ là False do chuỗi s chứa số 2020
# s = "codelearn2020"
# print(s.isalpha())


#
# s = "2020"
# print(s.isnumeric())
# s = "c2020"
# print(s.isnumeric())
#
# s = "Welcome to Codelearn.io!"
# print(s.split(" "))
# s = "A1B1C1D1E1"
# print(s.split("1"))

# lst = ["Welco  me", "to", "Cod ele arn. io!"]
# message = " ".join(lst)
# print(" ".join(message.split()))
# lst = ["A", "B", "C"]
# print("-".join(lst))
# s1 = "sdfs"
# s2 = 'sdfsadfsdfsadf'
#
# tmp = s1
# if len(s1) >=2 and len(s2)>=2:
#     s1 = s2[0:2] + tmp[2:]
#     s2 = tmp[0:2] + s2[2:]
# print(s1 + " " + s2)

# s = str(input())
# tmp  = s.split
# result = ""
# for i in tmp:
#     result_tmp = i + result
#     result = result_tmp
# print(result)

# def show(s):
#     countUpperCase = 0
#     countLowerCase = 0
#     for i in s:
#         if i.isupper():
#             countUpperCase +=1
#         if i.islower():
#             countLowerCase +=1
#     print("Given string:",s)
#     print("Number of uppercase letters:",countUpperCase)
#     print("Number of lowercase letters:",countLowerCase)
#
# s = str(input())
# show(s)
#Initial list
# res = []
#
# # Input lengths
# lengths = int(input())
#
# # Add element
# for i in range(lengths):
#     # Input elements
#     n = int(input())
#     res.append(n)
#
# def evenNum(res):
#     result  = []
#     for i in res:
#         if i & 1 == 0:
#             result.append(i)
#     print(result)
# evenNum(res)

# list1 = ['saf','asdf',4234,234]
# list2 = ['saf','asdf',4234,234]
#
# print(complex(list1,list2))
#
# print("sadf:",list1)
# print("sadf:",list2)
#
# del(list1[0:3])
# print(list1)

# data =(10,20,'ram',56.8)
# data1 =(103,20,'ram',56.8)
# data2 =(56.8,)
# data3 =()
# print(data2)
# print(data3)
#
# data={100:'Hoang' ,101:'Nam' ,102:'Binh'}
# print (data )
# class MyClass:
#     x = "ahihi"
# print(MyClass.x)

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
# p1 = Person("John", 36)
#
# print(p1.name)
# print(p1.age)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return "hỗ trợ em cái"+ f"{ self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name)
#
# p1 = Person("John", 36)
# p1.myfunc()