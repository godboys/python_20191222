import time

def calcProd():
   #Calculate the product of the first 100,000 numbers
   product=1
   for i in range(1,100000):
      product=product*i
   return product

if __name__ == '__main__':
    # 表示从1970年到当前时间一共的秒数
    print(time.time()) # 1577022497.295276

    # 计算一百万行代码运行的时间
   #startTime = time.time()
    # prod = calcProd()
   #endTime = time.time()
    # print ('The result is %s digits long' % (len(str(prod)))) # The result is 456569 digits long
   #print ('Took %s seconds to calculate' % (endTime - startTime)) # Took 2.6482274532318115 seconds to calculate

    # 定时 10s钟
    print("start: " + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
    time.sleep(10)
    print("end: " + time.strftime("%Y-%m-%d %H:%M:%S"),time.localtime())