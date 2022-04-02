"""
1st defining Node class (it will represent one block with data and next node address)
2nd defining Linked_list class That will contain rest of methods
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        

class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:                 # if list have only one element
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:                       # iterating to get last element
            itr = itr.next
        itr.next = Node(data, None)           # assigning last element with data and None

    def insert_values(self, data_list):
        # self.head = None                      # it will clear all previous "data" and add "data_list" in linked_list
        for data in data_list:
            self.insert_at_end(data)          # we can also use method "insert_at_beginning" it will reverse the data

    def print(self):
        if self.head is None:                 # if list doesn't have any nodes
            print("list is empty")
            return
        # iterating in the list
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.data) + ' ---> '  # assigning data to empty linked list
            itr = itr.next
        print(llstr)


"""
The way we are calling the method will also affect the result.
Below, we have called 'insert_at_end(10)' first before even printing any other data so it will get executed.
after that insert_at_beginning(8) will get printed before 10      {8--->10--->}
followed by 6                                                     {6--->8--->10--->}
after this 'insert_values(["python", "java", "c", "java_script"])' will printed at the "end" of the current list
{4 ---> 6 ---> 8 ---> 10 ---> python ---> java ---> c ---> java_script --->}
and then 12 will get called at the last
"""

ll = Linked_list()
ll.insert_at_end(10)
ll.insert_at_beginning(8)
ll.insert_at_beginning(6)
ll.insert_values(["python", "java", "c", "java_script"])
ll.insert_at_beginning(4)
ll.insert_at_end(12)
ll.print()
