import sys
import argparse

def fetch_lines(filename, *n):
	with open(filename,"r") as FH:
		data = FH.read()
	print(data)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', type=str)
	parser.add_argument('n', type=int)
	parser.add_argument('m', type=int)
	#parser.add_argument('--sum', dest='accumulate', action='store_const',
	                   #const=sum, default=max,
	                   #help='sum the integers (default: find the max)')

	args = parser.parse_args()
	filename = args.filename
	fetch_lines(filename)