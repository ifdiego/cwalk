class Node:
    def __init__(self, value):
        self.value = value;
        self.left = None
        self.right = None

def insert(root, number):
    if root is None:
        return Node(number)
    if number < root.value:
        root.left = insert(root.left, number)
    else:
        root.right = insert(root.right, number)
    return root

def search(root, number):
    if root is None:
        return None
    if root.value > number:
        return search(root.left, number)
    if root.value < number:
        return search(root.right, number)
    return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.value)
        inorder(root.right)

def preorder(root):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.value)

def minvalue(root):
    if root.left is not None:
        return minvalue(root.left)
    return root

def maxvalue(root):
    if root.right is not None:
        return maxvalue(root.right)
    return root

def delete(root, number):
    if root is None:
        return root
    if number < root.value:
        root.left = delete(root.left, number)
    elif number > root.value:
        root.right = delete(root.right, number)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minvalue(root.right)
        root.value = temp.value
        root.right = delete(root.right, temp.value)
    return root

def main():
    root = None

    while True:
        num = int(input("enter a number (zero to stop): "))
        if num == 0:
            break;
        root = insert(root, num)

    print("printing in order: ")
    inorder(root)
    print("printing in preorder: ")
    preorder(root)
    print("printing in postorder: ")
    postorder(root)

    min = minvalue(root)
    max = maxvalue(root)
    print("min value:\n%d" % min.value)
    print("max value:\n%d" % max.value)

    exists = int(input("enter a number to search: "))
    if search(root, exists) is not None:
        print("%d exists in tree" % exists)
    else:
        print("%d don't exist in tree" % exists)

    remove = int(input("enter a number to remove: "))
    if search(root, remove) is not None:
        root = delete(root, remove)
        print("%d removed from tree" % remove)
        print("printing in order: ")
        inorder(root)
        print("printing in preorder: ")
        preorder(root)
        print("printing in postorder: ")
        postorder(root)
    else:
        print("%d not found" % remove)

if __name__ == '__main__':
    main()
