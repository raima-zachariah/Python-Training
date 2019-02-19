string = input("Enter a string: ")

twitterfy = ''.join(string.title().split())
print("#"+twitterfy)

twitterfy = string.title().replace(' ','')
print("#"+twitterfy)
