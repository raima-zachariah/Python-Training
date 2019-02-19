if __name__ == "__main__":
	filename = "details.txt"
	vowels = ['a','e','i','o','u']
	newtext = []
	with open(filename) as fh:
		data = fh.read()
	lines = data.split('\n')
	for line in lines:
		words = line.split()
		# for word in words:
		newtext.append(''.join(c for i, c in enumerate(line) if not (c in 'aeiou' and i>1 and line[i-1].isalpha())))
		
	print(newtext)