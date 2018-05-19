import zipfile

zfile = Zipfile.ZipFile(raw_input("Zip file : "))
dictfile = open(raw_input('Enter dictionary file : ')
	
	
for lines in dictfile.readlines():
	word = lines.strip('\n')
	
	try:
		zfile.extractall(pwd = word)
		print '[+] Password : ' + word

	except Exception, e:
		print e
