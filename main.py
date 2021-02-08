from kahoot import client
import threading

def thread_func(name:str):
	def joinHandle():
		pass
	bot = client()
	bot.join(2123865, str(name))
	bot.on("joined", joinHandle)

for i in range(500):
	x = threading.Thread(target=thread_func, args=(str(i),))
	x.start()
