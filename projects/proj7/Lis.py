# Project 7 - LIS
# gets longest increasing sequence from a given sequence
# runs in O(nlogn) time complexity


def verify_subseq(seq, subseq):
	"""
	Verify a subsequence of a given sequence
	runs in O(n) time
	"""
	if not subseq: # if subseq empty return true
		return True

	new = []      # n extra space
	subseq = list(subseq)
	for ele in seq: # O(n)
		if ele == subseq[len(new)]: # check the corresponding subseq memeber
			new.append(ele)
		if new == subseq:     # check if done
			return True
	return False              # ran through and is not a subseq

def verify_increasing(seq):
	"""
	verify the sequence increases
	param a sequence as a string or list
	"""
	seq = list(seq)  # get list version to work with 
	if not seq:      # test empty
		return True

	c = seq[0]   # start comparer
	for i in range(1,len(seq)):  # iterate through full list
		if seq[i] <= c:   # check if breaks conditions of increasing
			return False
		c = seq[i]    # iterate to next
	return True       # never was false so it is increasing

def find_lis(seq):
	"""
	Find the longest increasing seq in a seq
	param a seq
	"""
	seq = list(seq)   # make sure for strings
	l = len(seq) # get length
	prev = [0] * l    # n space
	tmp = [0] * (l+1)  # n space
	L = 0    
	for i in range(l):
	   low = 1
	   high = L
	   while low <= high:        # gets index needed
	       mid = (low+high)//2
	       if (seq[tmp[mid]] < seq[i]):
	           low = mid+1
	       else:
	           high = mid-1

	   newL = low               # reassign
	   prev[i] = tmp[newL-1]
	   tmp[newL] = i

	   if (newL > L):     # check largest
	       L = newL

	result = []    # rebuild the result
	k = tmp[L]     # first index
	for i in range(L-1, -1, -1):    # reverse range
	    result.append(seq[k])
	    k = prev[k]

	return result[::-1] # return reversed list

