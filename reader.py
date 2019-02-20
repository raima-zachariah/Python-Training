import sys
import argparse

def fetch_lines(filename):
	with open(filename,"r") as FH:
		data = FH.read()
	print(data)

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', type=str)
	parser.add_argument('n', type=int, required=False)
	parser.add_argument('m', type=int, required=False)

	args = parser.parse_args()
	filename = args.filename
	fetch_lines(filename)
