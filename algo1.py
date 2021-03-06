#! /usr/bin/env python

def merge(lleft, lright):
    i,j,k = 0,0,0
    res =[]

    while i<len(lleft) and j<len(lright):
        if lleft[i]<lright[j]:
            res.append(lleft[i])
            k+=1
            i+=1
        else:
            res.append(lright[j])
            k+=1
            j+=1

    if i<len(lleft): res[k:]=lleft[i:]
    elif j<len(lright): res[k:]=lright[j:]
    #else: logging.error("internal error")
    
    return res

def mergeSort(l):
    if len(l) <= 1:
        return l

    else:
        lleft = mergeSort(l[:len(l)/2])
        lright = mergeSort(l[len(l)/2:])
        
    return merge(lleft, lright)


def main():
	f = open('/Users/victor/Desktop/IntegerArray.txt', 'r')
	filearray = []
	
	for line in f:
		filearray.append(int(line))

	sortedList = mergeSort(filearray)
	#print sortedList
	
	
	fout = open('/Users/victor/Desktop/results.txt', 'w')
	for item in sortedList:
        fout.write("%s\n" %item)
	f.close
	fout.close

if __name__ == '__main__':
    main()