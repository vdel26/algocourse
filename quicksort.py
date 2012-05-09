def partition(myList, start, end, pivot):
	pivot = myList[0]
	i = start + 1
	for j in (start+1, end):
		if myList[j] < pivot:
			myList[i], myList[j] = myList[j], myList[i]
			i += 1
	myList[start], myList[i-1] = myList[i-1], myList[start]
	return i-1


def choosePivot(myList):
	return myList[0]

def quicksort(myList, start, end):
	if start < end: 
		pivot = choosePivot(myList)
		split = partition(myList, start, end, pivot)
		
		quicksort(myList, start, split) 
		quicksort(myList, split+1, end)

if __name__ == '__main__':
	l = [3,5,7,2,1,6,4]
	start = 0
	end = len(l)-1
	quicksort(l, start, end)
	print l