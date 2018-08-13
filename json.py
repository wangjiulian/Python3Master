 
# import json
 
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'Runoob',
#     'url' : 'http://www.runoob.com'
# }
 
# json_str = json.dumps(data)
# print ("Python 原始数据：", repr(data))
# print ("JSON 对象：", json_str)

import time

print(time.time())

localtime = time.asctime(time.localtime(time.time()))
print ("本地时间为 :", localtime)


print(time.strftime("%Y-%m-%d %H:%M:%S :%A", time.localtime()))
a = "Sat Mar 28 22:24:24 2016"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

import calendar

cal = calendar.month(2016,1)
print(cal)

print(time.clock())




