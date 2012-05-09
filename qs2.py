def quicksort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        smaller = [small for small in lst[1:] if small < pivot]
        bigger = [big for big in lst[1:] if big >= pivot]
        return quicksort(smaller) + [pivot] + quicksort(bigger)

if __name__ == '__main__':
	l = [3,5,7,2,1,6,4]
	sortedList = quicksort(l)
	print sortedList