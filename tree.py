class Node:
    def __init__(self, data):
        self.data = data
        self.left = "Null"
        self.right = "Null"

def printPreorder(root):
    if root == "Null":
        pass
    else:
        print (root.data)
        printPreorder(root.left)
        printPreorder(root.right)

def printPostorder(root):
    if root == "Null":
        pass
    else:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.data)
        

def printinorder(root):
    if root == "Null":
        pass
    else:
        printinorder(root.left)
        print(root.data)
        printinorder(root.right)
        

header = "Null"

ch = "0"
while ch != "5":
    print("\n 1. Add \n 2. Print in Preorder \n 3. Print in postorder \n 4. Print in inorder")
    ch = input("Enter your choice: ")
    if ch == "1":
        new_data = input("Enter element to add: ")
        new_node = Node(new_data)
        # if header :
        #     if new_data < header:
        #         if header.left == "Null":
        #             header.left = new_node
        #         else :
        #             header.left.left = new_node
        #     elif new_data > header:
        #         if header.right == "Null":
        #             header.right = new_node
        #         else :
        #             header.right.right = new_node
        # else :
        #     header = new_node
        if header == "Null":
            header = new_node
        else:
            ctr = 0
            temp = header
            while ctr == 0:
                if temp.data == new_data:
                    print("Element is already present in Tree")
                    ctr = 3
                elif temp.data > new_data:
                    if temp.left != "Null":
                        temp = temp.left
                    else:
                        ctr = 1
                elif temp.data < new_data:
                    if temp.right != "Null":
                        temp = temp.right
                    else:
                        ctr = 2

            if ctr == 1:
                temp.left = new_node
                print(" Inserted at left ")
            else:
                temp.right = new_node
                print(" Inserted at Right ")
    if ch == "2":
        printPreorder(header)
    if ch == "3":
        printPostorder(header)
    if ch == "4":
        printinorder(header)