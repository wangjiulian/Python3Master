

class people:
	"""docstring for People"""
	name = ''
	age =''
	__weight = ''
	def __init__(self,n,a,w):
		self.name = n
		self.age = a
		self.__weight = w

	def speak(self):
		print("My name is %s, %d old , %d weight" % (self.name, self.age,self.__weight))


# p = people('mary',12,80)
# p.speak()


class student(people):
	"""docstring for student"""
	grade = ''
	def __init__(self,n,a,w,g):
		people.__init__(self,n, a, w)
		self.grade = g
	def speak(self):
		print("我是个演说家 %s, %d old , %d grade" % (self.name, self.age,self.grade))

# s = student('jack',13,99,4)
# s.speak()

class speak():
	"""docstring for speak"""
	topic = ''
	name = ''
	def __init__(self,n,t):
		self.name = n
		self.topic = t
	def speak(self):
		print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))

class sample(speak,student):
	"""docstring for sample"""
	def __init__(self,n,a,w,g,t):
		student.__init__(self,n, a, w, g)
		speak.__init__(self,n, t)

sam = sample('222','12',22,2, 222)
sam.speak()

 
class Parent:        # 定义父类
	def myMethod(self):
		print ('调用父类方法')
 
class Child(Parent): # 定义子类
	def myMethod(self):
		print ('调用子类方法')
 
c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
# super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
super(Child,c).myMethod()

class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量
 
	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print (self.__secretCount)
 
counter = JustCounter()
counter.count()
counter.count()
print (counter.publicCount)
# print (counter.__secretCount)  # 报错，实例不能访问私有变量

class Site:
	def __init__(self, name, url):
		self.name = name       # public
		self.__url = url   # private
 
	def who(self):
		print('name  : ', self.name)
		print('url : ', self.__url)

	def __foo(self):          # 私有方法
		print('这是私有方法')

	def foo(self):            # 公共方法
		print('这是公共方法')
		self.__foo()
 
x = Site('菜鸟教程', 'www.runoob.com')
x.who()        # 正常输出
x.foo()        # 正常输出
# x.__foo()      # 报错

