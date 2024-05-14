class Car:
    def __init__(self, marc, subname, age):
        self.marc = marc
        self.subname = subname
        self.age = age

    def my(self):
        print("Марка " + self.marc, self.subname, self.age)

p1 = Car("Toyota", "Camry", 2024)
p1.my


class Person:
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print("Аты:",self.name)

class Employee(Person):
    def job(self,job_name):
        print("Аты:",self.name,"жұмыс:",job_name)

employee_obj=Employee("Канат")
employee_obj.job("programmer")


class Figura:
    def _init_(self, p):
        self.p = p
    
    def get_info(self):
        print("Периметр:", self.p)

class Triangle(Figura):
    def _init_(self, a, b, c):
        Figura._init_(self, a + b + c)

triangle_obj = Triangle(10, 20, 30)
triangle_obj.get_info()



class Color:
    def _init_(self, color):
        self.color = color
    
    def get_info(self):
        print("Цвет:", self.color)

class Triangle(Color):
    def _init_(self, color):
        Color._init_(self, color)

triangle_obj = Triangle("красный")
triangle_obj.get_info()
