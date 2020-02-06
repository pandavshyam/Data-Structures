class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        print ("List Contains: ")
        while (temp):
            print(temp.data)
            temp = temp.next
        print(temp.val)

    def insertBeg(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_data
            return
        new_node.next = self.head
        self.head = new_node

    def insertBefore(self,node,new_data):
        new_node = Node(new_data)
        if node is None:
            print ("Element is not present")
            return
        temp = self.head
        prev_node = self.head
        while (temp.data != node):
            prev_node = temp
            temp = temp.next
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertAfter(self,prev_node,new_data):
        new_node = Node(new_data)
        if prev_node is None:
            print("Element is not present")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertEnd(self,new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while (temp.next):
            temp = temp.next
        temp.next = new_node

    def deleteNode(self,key):
        temp = self.head
        if temp.data == None:
            print ("Linked list is empty")
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return

        while (temp is not None):
            if (temp.data == key):
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return

        prev.next = temp.next
        temp = None

    def insertElement(self,new_data):
        new_node = Node(new_data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while (temp.data != None):
            temp = temp.next
        temp.next = new_node

    def update(self,old_value,new_value):
        temp = self.head
        while (temp.data != old_value):
            temp = temp.next
        temp.data = new_value

    def search(self,key):
        flag = 0
        temp = self.head
        while (temp.next != None):
            if temp.data == key:
                flag = 1
            else :
                pass
            temp = temp.next
        if flag ==1:
            print ("Found")
        else:
            print("Not Found")

    def size(self):
        size = 0
        temp = self.head
        while (temp):
            size += 1
            temp = temp.next
        return size

    def sort(self):
        size = self.size()
        for i in range (size):
            temp = self.head
            size1 = size
            while temp != None and size1 != 1:
                if temp.data > temp.next.data:
                    temp1 = temp.data
                    temp.data = temp.next.data
                    temp.next.data = temp1
                size-=1
                temp = temp.next

    def min(self):
        min = self.head.data
        temp = self.head
        while (temp != None):
            if temp.data < min:
                min = temp.data
            temp = temp.next

    def max(self):
        max = self.head.data
        temp = self.head
        while (temp != None):
            if temp.data > max:
                max = temp.data
            temp = temp.next

while True:
    try:
        print("\n 1. Create Linked list ")
        print("\n 2. To print list ")
        print("\n 3. Insert at begin")
        print("\n 4. insert before")
        print("\n 5. insert after")
        print("\n 6. insert at end")
        print("\n 7. delete")
        print("\n 8. insert")
        print("\n 9. update")
        print("\n 10. search")
        print("\n 11. size")
        print("\n 12. sort")
        print("\n 13. min")
        print("\n 14. max")

        ch = int(input("Enter your choice: "))
        if ch == 1:
            Linkedlist = LinkedList()
        elif ch == 2:
            print("All the elements of the linked list: ")
            LinkedList.printList()
        elif ch ==3:
            new_data=input("Enter the element you want to add at beginning: ")
            LinkedList.insertBeg(new_data)
        elif ch ==4:
            new_data = input("Enter the element you want to add: ")
            node = input("Before which element you want to add: ")
            LinkedList.insertBefore(node,new_data)
    except:
        continue
