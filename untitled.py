
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










