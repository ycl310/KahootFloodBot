from kahoot import client
import threading
import time

f = open("names", 'r').readlines()

def thread_func(name:str):
	def joinHandle():
		pass
	bot = client()
	bot.join(6466955, str(name))
	bot.on("joined", joinHandle)

for i in range(500):
	x = threading.Thread(target=thread_func, args=(str(f[i]),))
	x.start()
	#time.sleep(1)
