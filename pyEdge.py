from subprocess import Popen
import time

def call(first, second, third, sleep=1):
	Popen(["sudo", "./source", first, second, third])
	time.sleep(sleep)
	Popen(["sudo", "./source", "00", "00", "00"])
	return




