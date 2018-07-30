
import sys



list = [1,2,3,4]
it = iter(list)

# while True:
# 	try:
# 		print(next(it))
# 	except StopIteration:
# 		sys.exit()


def hello():
    print("Hello World!")

hello()		
	   

def area(width, height):	
	   	return width * height

def print_welcome(name):
	print("Welcome",name)

print_welcome('Runn')
w = 4
h = 5
print("width=",w," height=",h ," area=",area(w,h))	


def printinfo11222( arg1, *vartuple):
	"打印任何传入的参数"
	print("输出:")
	print(arg1)
	print(vartuple)

printinfo11222(70,60,80,90,100)	
printinfo11222(90)

def print2222( arg1, **vardict):
	print("输出:")
	print(arg1)
	print(vardict)

print2222(222, a=1,b=3)

sum1 = lambda arg1, arg2 : arg1 + arg2

print("相加后的值为:", sum1(1,3))	
def sum( arg1, arg2 ):
   # 返回2个参数的和."
   total = arg1 + arg2
   print ("函数内 : ", total)
   return total
 
# 调用sum函数
total = sum( 10, 20 )
print ("函数外 : ", total)

num = 1
def func1():
	global num
	print(num)
	num = 222
	print(num)

def outer():
	numm = 100
	def inner():
		nonlocal numm
		numm = 100
		print(numm)
	inner()
	print(numm)

outer()				
func1()
a = 10
def test(a):
    a = a + 1
    print(a)
test(a)

b = [-1, 1, 66.25, 333, 333, 1234.5]
del b[2:4]
del b[:]
print(b)
t = 12345, 54321, 'hello!'
print(t[0])
print(t)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
if 'apple' in basket:
		print('ok')	

c = set('abbdadadd')
d = set('dadaaadaaad')
print(c)


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4234
print(tel)
print(tel.keys())
if 'guido' not in tel:
	print('21121')
d = dict([('sape', 4193),('hhh',222)])
print(d)

for k,v in d.items():
	print(k,v)
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)	

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue'] 

for q,a in zip(questions, answers):
	print('What is your {0} It is {1}'.format(q,a))
for i in reversed(range(1, 10, 2)):
   print(i)

for f in sorted(set(basket)):
	print(f)


print(sys.version)














