import os,sys

ret = os.access('/Work/Python3/Python3Master/file.py', os.F_OK)
print("F_OK 返回值%s" % ret)

ret = os.access('/Work/Python3/Python3Master/file.py', os.W_OK)
print("F_OK 返回值%s" % ret)

ret = os.access('/Work/Python3/Python3Master/file.py', os.R_OK)
print("F_OK 返回值%s" % ret)

ret = os.access('/Work/Python3/Python3Master/file.py', os.X_OK);
print("F_OK 返回值%s" % ret)


# import sys
 
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except:
#     print("Unexpected error:", sys.exc_info()[0])
#     raise



class MyError(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return repr(self.value)
   
try:
    raise MyError(2*2)
    except MyError as e:
        print('My exception occurred, value:', e.value)

		






