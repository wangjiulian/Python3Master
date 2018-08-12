import os
import shutil
import glob
import sys
import re
import math
import random
import smtplib
from datetime import date

from urllib.request import urlopen

from timeit import Timer

print(os.getcwd())
os.chdir('/Work/Python3/Python3Master')
print(glob.glob('*.py'))


print(sys.argv)
sys.stderr.write('2121212112121')


print(math.cos(math.pi / 4))



print(random.choice(['apple','banana','pear']))

print(random.sample(range(100),10))

print(random.random())
print(random.randrange(6))



# for line in urlopen('http://www.runoob.com/python3/python3-class.html'):
# 	line = line.decode('utf-8')
# 	print(line)

# server = smtplib.SMTP('localhost')
# # server.sendmail(from_addr, to_addrs, msg, mail_options)
# server.quit()

# shutil.copyfile('test.txt','test1.txt')
# shutil.move('/test/test1.txt','/')

now = date.today()
print(now)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)



print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())


def average(values):

	return sum(values) / len(values)

import doctest
doctest.testmod() 

# import unittest

# class TestStatisticalFunctions(unittest.TestCase):

# 	def test_average(self):
# 		self.assertEqual(average([20, 30, 70]), 40.0)
# 		self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
# 		self.assertRaises(ZeroDivisionError, average, [])
# 		self.assertRaises(TypeError, average, 20, 30, 70)
# unittest.main()


import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
zlib.decompress(t)
