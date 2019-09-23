import threading
from time import sleep

def hello_1():
	while True:
		print("1")
		sleep(1)

def hello_2():
	while True:
		print("2")
		sleep(1)

def hello_1_thread():
	thread=threading.Thread(target=hello_1)
	thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
	thread.start()


hello_1_thread()
hello_2()