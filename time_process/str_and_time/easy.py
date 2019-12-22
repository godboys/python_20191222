

# python中时间日期格式化符号：
# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
import datetime

if __name__ == '__main__':
    # 把字符串转日期
    cday = datetime.datetime.strptime('2017-2-6 18:19:59', '%Y-%m-%d %H:%M:%S')
    print(cday, type(cday)) # 2017-02-06 18:19:59 <class 'datetime.datetime'>
    # 时间转字符串
    now = datetime.datetime.now()
    print(now.strftime('%a, %b %d %H:%M')) # Sun, Dec 22 22:42