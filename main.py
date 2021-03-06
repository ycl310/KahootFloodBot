from kahoot import client
#import threading
import threading2
import argparse
import time

f = open("names", 'r').readlines()

parser = argparse.ArgumentParser(description="Arguments from the terminal")
parser.add_argument('--pin', type=int, help="game pin of the kahoot session")
parser.add_argument('--amt', type=int, help="amount of bots that join the session")
parser.add_argument('--wait', type=int, help="time of await")
args = parser.parse_args()

pin = 0
ite = 0
wait = 0

try:
	pin = int(args.pin)
	ite = int(args.amt)
	wait = args.wait
	if(wait==None):
		wait = 0
except TypeError as e:
	print(str(e)+"""
		Make sure you have passed in the required arguments,
		use the --help flag to get information
	""")
	exit()


def thread_func(name:str):
	def joinHandle():
		pass
	bot = client()
	bot.join(int(pin), str(name))
	bot.on("joined", joinHandle)

def main():
	t = None
	for i in range(int(ite)):
		t = threading2.Thread(target=thread_func, args=(str(f[i]),))
		t.start()
		time.sleep(int(wait))
	while True:
		try:
			pass
		except KeyboardInterrupt:
			t.stop()
			exit()

if __name__ == "__main__":
	main()
