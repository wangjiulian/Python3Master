
# -*- coding: UTF-8 -*-
fo = open("test.txt", "r+")
print('文件名:',fo.name)

# fo.flush()

# fid = fo.isatty()
# print('文件描述为:', fid)



# for index in  range(5):
# 	line = next(fo)
# 	print('第%d行-%s' %(index,line))


# line = fo.read(10)
# print ("读取的字符串: %s" % (line))


# line = fo.readline()

# print ("读取的字符串: %s" % (line))

# line = fo.readline(5)
# print ("读取的字符串为: %s" % (line))


# for line in fo.readlines(): # 依次读取每行
# 	line = line.strip() # 去除头尾空白
# 	print('读取的数据为: %s' % line)


# line = fo.readline()
# print('读取的数据:%s' %(line))
# fo.seek(0,0)
# line = fo.readline()
# print('读取的数据:%s' % (line))
# # pos = fo.tell()
# # print('当前位置:%d' % (pos))

# fo.truncate()
# line = fo.readlines()
# print ("读取行: %s" % (line))


str = '\n6:wwwwwww'
fo.seek(0,2)
line = fo.write(str)
seq = ["1212 1\n", "3333 2"]
fo.writelines(seq)



fo.close()
