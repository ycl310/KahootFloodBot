from kahoot import client
import threading
import argparse
import time

f = open("names", 'r').readlines()

parser = argparse.ArgumentParser(description="Arguments from the terminal")
parser.add_argument('--pin', type=int, help="game pin of the kahoot session")
parser.add_argument('--amt', type=int, help="amount of bots that join the session")
args = parser.parse_args()

try:
	pin = args.pin
	ite = args.amt
	print("pin: "+str(pin))
	print("amount: "+str(ite))
except TypeError:
	print(str(e)+"""
		Make sure you have passed in the required arguments,
		use the --help flag to get information
	""")
	exit()

def thread_func(name:str):
	def joinHandle():
		pass
	bot = client()
	bot.join(pin, str(name))
	bot.on("joined", joinHandle)

for i in range(ite):
	x = threading.Thread(target=thread_func, args=(str(f[i]),))
	x.start()
	#time.sleep(1)
