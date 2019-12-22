# Python的空值是用None表示,None不是0，也不是空字符串，也不是False,它是一个特殊的空值
if __name__ == "__main__":
    print(type(None)) # <class 'NoneType'>
    print(None == 0) # False
    print(None == "") # False
    print(None == None) # True
    print(None == False) # False
    print(None == True) # False