class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1

def insert(root, number):
    if root is None:
        return Node(number)
    if number < root.value:
        root.left = insert(root.left, number)
    else:
        root.right = insert(root.right, number)
    root.height = 1 + max(height(root.left), height(root.right))
    factor = balance(root)
    if factor > 1:
        if number < root.left.value:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    if factor < -1:
        if number > root.right.value:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    return root

def height(root):
    if root is None:
        return 0
    return root.height

def balance(root):
    if root is None:
        return 0
    return height(root.left) - height(root.right)

def minvalue(root):
    if root.left is not None:
        return minvalue(root.left)
    return root

def preorder(root):
    if root is not None:
        print(root.value)
        preorder(root.left)
        preorder(root.right)

def left_rotate(root):
    a = root.right
    temp = a.left
    a.left = root
    root.right = temp
    root.height = 1 + max(height(root.left), height(root.right))
    a.height = 1 + max(height(a.left), height(a.right))
    return a

def right_rotate(root):
    a = root.left
    temp = a.right
    a.right = root
    root.left = temp
    root.height = 1 + max(height(root.left), height(root.right))
    a.height = 1 + max(height(a.left), height(a.right))
    return a

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
    root.height = 1 + max(height(root.left), height(root.right))
    factor = balance(root)
    if factor > 1:
        if balance(root.left) >= 0:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)
    if factor < -1:
        if balance(root.right) >= 0:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)
    return root

def main():
    root = None

    while True:
        num = int(input("enter a number (zero to stop): "))
        if num == 0:
            break;
        root = insert(root, num)

    print("printing in preorder: ")
    preorder(root)

if __name__ == '__main__':
    main()
