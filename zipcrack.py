import zipfile
import sys
import optparse
from threading import Thread 

def extractFile(zfile, password):
	try:
		zfile.extractall(pwd=password)
		return password
	except Exception, e:
		print e
		return
	
def main():
	
	parser = optparse.OptionParser('usage%prog ' +\
		'-f <zipfile> -d <dictionary>')
	parser.add_option('-f', dest='zname', type='string', \
		help='specify zip file')
	parser.add_option('-d', dest='dname', type='string', \
		help='specify dictionary file')		
	(options, args) = parser.parse_args()
	if (options.zname == None) | (options.dname == None):
		print parser.usage
		exit()
	else:
		zname = options.zname
		dname = options.dname
	zfile = zipfile.ZipFile(zname)
	dicfile = open(dname)
		for lines in dictfile.readlines():
				password = lines.strip('\n')
				t = Thread(target=extractFile, args=(zfile, password))
				t.start()
				if compare:
					print '[+] Password Found : ' + password
					return
				else:
					print '[+] Not found'
					return

if __name__ == '__main__':
	main()
