# String :单引号，双引号和三引号
if __name__ == "__main__":
    print('abc')
    print("hello world")
    print('''This is my first code''')

    # 若字符串里面包含特殊的字符，可以用转义\进行转义

    print('Xiao Ming said \"I\'am full\".')

    # 三引号一般用在类或者函数的开头用来做大段的注释用

    # python的字符串format格式
    # 1)%操作符 保留%主要是为了兼容以前的代码
    name = "yangjian"
    age = 20
    print("My name is %a,age is %d"%(name,age))
    # 2).format
    print("My name is {},age is {}".format(name,age))
    print("My name is {0},age is {1}".format(name,age))
    # 参数的顺序和格式化的顺序不必完全相同
    print("age is {1},My name is {0}".format(name,age))
    print("age is {},My name is {}".format(name,age))

    strs = ["123", "334", "877"]
    str = "123"
    print(str == strs[0]) # True
    print(str is strs[0]) # True
    print(str in strs[0]) # True
