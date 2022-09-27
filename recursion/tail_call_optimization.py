from functools import lru_cache

@lru_cache(maxsize=None)
def factorial(n, count):
    if (n == 0):
        return count
    return factorial(n - 1, n * count)

def main():
    num = int(input("enter a number: "))
    print('%d! = %d' % (num, factorial(num, 1)))

if __name__ == '__main__':
    main()
