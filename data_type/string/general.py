
# 字符串的合并和连接
import re
import string


def merge_join():
    str1 = "hello"
    str2 = " world"
    # 相加 //两个字符串可以很方便的通过'+'连接起来
    new_str = str1 + str2
    print(new_str) # hello world

    # 合并//用join方法
    url = ["www","baidu","com"]
    print(".".join(url)) # www.baidu.com
# 字符串的切片和相乘
def test01():
    # 相乘 // 比如写代码的时候要分隔符
    line = '*' * 10
    print(line) # **********

    # 切片
    str = "Monday is busy day"
    # 表示取第一个到第七个的字符串
    print(str[0:7]) # Monday
    # 表示取从倒数第三个的字符到结尾的字符串
    print(str[-3:]) # day
    # 复制字符串
    print(str[::]) # Monday is busy day

# 字符串分割
def test02():
    # 普通的分割 有split,不支持多个分隔
    mobel = "176 8374    7170"
    telephone = "400-800-777-1234"
    # 无参数 以空格(不管多少空格)分割
    print(mobel.split()) # ['176', '8374', '7170']
    # 以"-"分割
    print(telephone.split("-"))

    # 复杂的分割
    line = "helloworld;  python, I,  love  ,  it  "
    # import re   说明：r表示不转义,分隔符可以是;或者,或者空格后面跟0个多个额外的空格
    print(re.split(r'[;,s]\s*',line)) # ['helloworld', 'python', 'I', 'love  ', 'it  ']

# 字符串的开头和结尾的处理
def test03():
    # 比方我们要查一个文件的名字是以什么开头或者什么结尾
    filename = 'trace.h'
    print(filename.endswith('h')) # True
    print(filename.startswith('trace')) # True

# 字符串的查找和匹配
def test04():
    # 一般查找 在长的字符串里面查找子字符串，会返回子字符串所在位置的索引, 若找不到返回-1
    title = "今天是个好日子"
    print(title.find("日子")) # 5  返回的是数字
    print(title.find("天天")) # -1

    # 复杂的匹配
    date = "22/12/2019"
    if re.match(r'\d+/\d+/\d+',date): # Ture
        print("ok,match")
    else:
        print('ok,not match')

# 字符串替换
def test05():
    # 普通的替换//用replace就可以
    text = "My name is yangjian"
    print(text.replace("yangjian","god")) # My name is god

    # 复杂的替换//若要处理复杂的或者多个的替换，需要用到re模块的sub函数
    students = "Boy 88, Girl 100"
    print(re.sub(r'\d+',"100",students)) # Boy 100, Girl 100

# 字符串中去掉一些字符
def test06():
    # 去除空格//对文本处理的时候比如从文件中读取一行，然后需要去除每一行的两侧的空格，table或者是换行符
    line = '  Congratulations, you guessed it.  	 '
    print(line.strip()) # Congratulations, you guessed it.
    #  注意:字符串内部的空格不能去掉，若要去掉需要用re模块

    # 复杂的文本清理,可以利用str.translate    import string
    instr = "to"
    outstr = "TO"
    # #maketrans生成table，右边的值替换左边的值，注意长度和内容必须一一对应
    table = str.maketrans(instr,outstr)
    old_str = "Hello world ,welcome to use Python.  1234567"
    new_str = old_str.translate(table)
    print(new_str) # HellO wOrld ,welcOme TO use PyThOn.  1234567

if __name__ == "__main__":
    # 字符串的合并和连接
    merge_join()
    # 字符串的切片和相乘
    test01()
    # 字符串分割
    test02()
    # 字符串的开头和结尾的处理
    test03()
    # 字符串的查找和匹配
    test04()
    # 字符串替换
    test05()
    # 字符串中去掉一些字符
    test06()
