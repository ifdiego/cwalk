def factorial(n):
    if (n == 0):
        return 1
    return n * factorial(n - 1)

def main():
    num = int(input("enter a number: "))
    print('%d! = %d' % (num, factorial(num)))

if __name__ == '__main__':
    main()
