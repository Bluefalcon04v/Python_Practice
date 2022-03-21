'''about abstract class and abstractmethod we can't assign object with abstract class
and functions in abstract methods become compulsory to be carried by sub_class.'''
from abc import ABC, abstractmethod


class Computer(ABC):          # abstract class
    @abstractmethod           # decorators
    def process(self):        # abstract method
        pass


class Laptop(Computer):        # sub_class of Computer
    def process (self):        # necessary to define process method
        print("it's running")


class Programmer(ABC):          # abstract class
    @abstractmethod
    def work(self, com):        # abstract method
        print("solving bugs")
        com.process()


class Whitreboard(Programmer):     # sub_class of programmer
    def write(self):
        print("it's writing")

    def work(self):
        print("on a whiteboard")


com1 = Laptop()
com2 = Whitreboard()
# com3 = programmer() or Computer() classes we can't assign it's an abstract class.
com1.process()                        # calling for class
com2.write()
com2.work()