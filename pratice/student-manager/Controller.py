import random

import json

from Student import Student


# def checkId(students, id):
#     for i in students:


def add():
    def generateID():
        accountID = random.randint(100001, 999999)
        while checkId(accountID):
            accountID = random.randint(100001, 999999)
        return accountID

    id = generateID()

def edit():
    print("edit")
def info():
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)
        students = []
        for obj in data:
            id = obj['id']
            name = obj['name']
            age = obj['age']
            student = Student(id, name, age)
            students.append(student)
        # for i in students:
        #     print(i.get_id(),i.get_Name(),i.get_Age())
        return students


def delete():
    print("delete")


def readData(data):
    with open('data.json', 'r') as json_file:
        data = json.load(json_file)


def writeData(data):
    with open('data.json', 'w') as json_file:
        json.dump(data, json_file)
