""" Defining outer class and inner class """


class Student:                                     # outer class
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def show_char(self):
        print('name: ', self.name, '\nroll_no: ', self.roll_no)

    class Laptop:                                # inner class
        def __init__(self, brand, CPU, RAM):
            self.brand = brand
            self.CPU = CPU
            self.RAM = RAM

        def show_lap(self):
            print('brand: ', self.brand, '\nCPU: ', self.CPU, '\nRAM: ', self.RAM)


s1 = Student("jon", 23)                     # making object for outer class 'Student'
l1 = Student.Laptop('hp', 'i5', 16)         # making object for inner class 'Laptop'
s2 = Student("sam", 52)                     # making object for outer class 'Student'
l2 = Student.Laptop('Dell', 'i7', 32)       # making object for inner class 'Laptop'

s1.show_char()                                   # calling for outer class
l1.show_lap()                                   # calling for inner class
print("________________")
s2.show_char()                                   # calling for outer class
l2.show_lap()                                   # calling for inner class
