#! /usr/bin/env python


def MergeAndCountSplitInv(lleft, lright):
    i,j,k, count = 0,0,0,0
    res =[]

    while i<len(lleft) and j<len(lright):
        if lleft[i]<lright[j]:
            res.append(lleft[i])
            k+=1
            i+=1
        else:
            res.append(lright[j])
            count += len(lleft[i:])
            k+=1
            j+=1

    if i<len(lleft): res[k:]=lleft[i:]
    elif j<len(lright): res[k:]=lright[j:]
    #else: logging.error("internal error")
    
    return (res, count)


def mergeSort(l):
    if len(l) <= 1:
        return l

    else:
        (lleft, x) = mergeSort(l[:len(l)/2])
        (lright, y) = mergeSort(l[len(l)/2:])
        (res, z) = MergeAndCountSplitInv(lleft, lright)
    
    return (res, x+y+z)
    #return merge(lleft, lright)


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
    #main()
    testlist = [3, 4, 8, 0, 6, 7, 4, 2, 1, 9, 4, 5]
    (res, numinv) = mergeSort(testlist)
    #print "The sorted list is %s" %sortedList
    print "Num of inversions is %d" %numinv



