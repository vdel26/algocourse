#! /usr/bin/env python


def SortAndCount(A, n):
	if n == 1: 
		return 0
	else:
		(B, x) = SortAndCount(A[:n/2], n/2)
		(C, y) = SortAndCount(A[n/2:], n/2)
		(D, z) = MergeAndCountSplitInv(A, n)	

def MergeAndCountSplitInv():
	pass


f = open('/Users/victor/Desktop/IntegerArray.txt', 'r')
x = f.readlines()


