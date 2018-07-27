
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


def changeme(mylist):
	"修改传入的列表"
	mylist.append([1,2,3,4])
	print("函数内取值:", mylist)
	return
mylist = [10,20,30]
changeme(mylist)
print("函数外取值:",mylist)


def printme(str):
	"打印任何传人的字符串"
	print(str)
	return


printme(str = 'gggg')



def printinfo(name, age):
	print("名字:",name)
	print("年龄:",age)
	return


printinfo(age=12, name="gggggg")


def printinfo1(name, age=34):
	print("名字: ", name)
    print("年龄", age)
printinfo1( age=50, name="runoob" )
print ("------------------------")
printinfo1( name="runoob" )














