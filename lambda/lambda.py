TRUE = lambda a: lambda b: a
FALSE = lambda a: lambda b: b
NOT = lambda a: a(FALSE)(TRUE)

def main():
    print("x = True\ny = False\n")
    print("λxy.x\t%r" % (TRUE(True)(False)))
    print("λxy.y\t%r" % (FALSE(True)(False)))
    print("λx.xFT\t%r" % (NOT(TRUE)(True)(False)))
    print("λy.yFT\t%r" % (NOT(FALSE)(True)(False)))

if __name__ == '__main__':
    main()
