import urllib

def read_text():
	open_file=open("abc.txt")
	readfile = open_file.read()
	print readfile
	open_file.close()
	check_profanity(readfile)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text)
	output = connection.read()
	#print (output)
	connection.close()
	if "True" in output:
		print("Profanity Alert")
	elif "False" in output:
		print("File has no curse words")
	else:
		print("there is no such document")
read_text()

