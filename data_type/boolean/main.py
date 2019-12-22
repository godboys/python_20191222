# Python中的布置值，只有True和False两种(一定要注意大小写)
# not,是非运算,它是一个单目的运算，就是把True变False,把False变True
if __name__ == "__main__":
    a = True
    b = False
    c = a and b
    d = a or b
    e = not a
    print(c)
    print(d)
    print(e)