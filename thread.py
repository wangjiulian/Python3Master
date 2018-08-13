import _thread
import time
import threading

# def print_time( threadName, delay):
# 	count = 0
# 	while count < 5:
# 		time.sleep(delay)
# 		count += 1
# 		print("%s:%s" % (threadName,time.ctime(time.time())))


# try:
# 	_thread.start_new_thread(print_time, ("Thread-1",2))
# 	_thread.start_new_thread(print_time, ("Thread-2",4))
# except Exception as e:
# 	print ("Error: 无法启动线程")
# while 1:
# 	pass



exitFlag = 0

class myThread(threading.Thread):
	"""docstring for myThread"""
	def __init__(self,threadId,name,counter):
		threading.Thread.__init__(self)
		self.threadId = threading
		self.name = name
		self.counter = counter

	def run(self):
		print('开始线程：' + self.name)
		#获取锁，用于线程同步
		threadLock.acquire()
		print_time(self.name, self.counter, 5)
		#释放锁
		threadLock.release()

def print_time(threadName,delay,counter):
	while counter:
		if exitFlag:
			threadName.exit()
		time.sleep(delay)
		print ("%s: %s" % (threadName, time.ctime(time.time())))
		counter -= 1


threadLock = threading.Lock()
threads = []

thread1 = myThread(1, 'thread-1', 1)
thread2 = myThread(2, 'thread-2', 2)
thread1.start()
thread2.start()

threads.append(thread1)
threads.append(thread2)

for t in threads:
	t.join()

print('退出主线程')
