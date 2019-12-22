import datetime

import dateutil

if __name__ == '__main__':
    # dateutil是一个非常强大的模块，可以处理复杂的日期问题,比如时区，模糊时间范围
    d1 = datetime.datetime(2019, 11, 22)
    #print(d1 + dateutil.relativedelta.relativedelta(month=-1))