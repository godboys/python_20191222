# python的变量和数据类型
## 一、Python的变量类型非常简单：主要分下面几类：
### 1.numbers:分整数int和浮点数float
- 整数：比如1,200,-1000,0，也有用十六进制表示的比如0xff00等
- 浮点数：比如1.11,12,13，-10.02，也有比较大的浮点数比如2.12x10^9

### 2.String :单引号，双引号和三引号
python的字符串以''或者""或者''''''括起来的随意文本都是字符串
'abc',"hello world",'''This is my first code'''
有一点要注意若字符串里面包含特殊的字符，可以用转义\进行转义
```
word='Xiao Ming said \"I\'am full\".'
print(word)
>>Xiao Ming said "I'am full".
```
另外三引号一般用在类或者函数的开头用来做大段的注释用

说到字符串一点要提一下python的字符串format格式：一般有两种
1)%操作符
```
name="xiao ming"
age=20
print("Your name is %s,age is %d"%(name,age))
```
2).format
```
name="xiao ming"
age=20
print("Your name is {0},age is {1}".format(name,age))
```
.format的用法比较灵活，参数的顺序和格式化的顺序不必完全相同，一般推荐用format,而且也是Python3里面的官方力推，之所以保留%主要是为了兼容以前的代码
```
name="xiao ming"
age=20
print("age is {1},your name is {0},".format(name,age))
```

### 3.布尔值
Python中的布置值，只有True和False两种(一定要注意大小写),布尔值的运算可以用and,or 和not
A and B ,表示A和B都为True，最后的运算结果才是True.
A or B , 表示A或者B其中一个True，最后的结果就是True.
not,是非运算,它是一个单目的运算，就是把True变False,把False变True.
### 4.空值
Python的空值是用None表示,None不是0，也不是空字符串，也不是False,它是一个特殊的空值,我们可以用python的内置函数type来看一下，然后分别0,空字符，False比较一下，看看它到底是何物
```
>>> type(None)  
<class 'NoneType'>  
>>> None == 0  
False  
>>> None == ''  
False  
>>> None == None  
True  
>>> None == False  
False  
```
## 二、Python的变量命名
python的变量名必须是大小写的英文字母，数字和下划线(_)的组合,切记不能用数字开头
```
a=10
n_1=1000
a='wang01'
```
python的是动态语言，不像java是强制类型语言，是静态语言也就是说你在定义变量的时候就要指定类型，而python是动态的语言，是边执行变编译，这样就很灵活.
