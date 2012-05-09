import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

fh = logging.FileHandler('log_filename.txt')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(formatter)
logger.addHandler(ch)

logger.debug('This is a test log message.')

def countinversions(inputList):
	count = 0
	for i in range(0, len(inputList)-1):
		for j in range(i+1, len(inputList)):
			if inputList[i] > inputList[j]: count +=1
		logger.info(i)
	return count

def countFile():
	f = open('/Users/victor/Desktop/IntegerArray.txt', 'r')
	filearray = []
	
	for line in f:
		filearray.append(int(line))
	
	numinv = countinversions(filearray)
	print "Num of inversions is %d" %numinv	

def countList():
	testlist = [3,4,2,6,1,5]
	numinv = countinversions(testlist)
	print "Num of inversions is %d" %numinv	

if __name__ == '__main__':
	countList()