import datetime

# 时间的相加/相减
def and_less():
    # datetime里面有一个非常重要的模块叫timedelta,可以让时间的处理变的很灵活
    # 计算当天日期,前后的100天
    d3 = datetime.datetime(2019, 12, 22)
    print(d3 + datetime.timedelta(days=100)) # 2020-03-31 00:00:00



if __name__ == '__main__':
    # 获取当前时间
    print(datetime.datetime.now()) # 2019-12-22 21:57:27.304810
    # 获取当前日期
    print(datetime.date.today()) # 2019-12-22
    # 获取圣诞节时间差
    chrismas_day_gap = datetime.datetime(2019, 12, 25, 0, 0, 0) - datetime.datetime.now()
    print(chrismas_day_gap) # 2 days, 1:56:17.890324
    # 时间的相加/相减
    and_less()
    # 计算某两个日期差多少天
    d4 = datetime.datetime(2019, 12, 22)
    d5 = datetime.datetime(2020, 1, 25)
    print(d5 - d4) # 34 days, 0:00:00
    # imedelta有一个很大的缺点，不支持月份，天那怎么会这样，莫慌，用神补刀dateutil模块


