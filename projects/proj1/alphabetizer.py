"""
Project 1 - Alphabetizer
Use Merge sort to sort a list of people
sort by either first or last name
"""
cost=0 #global variable to keep track of the cost of alpabetizing

def order_first_name(a, b):
	"""
	Orders two people by their first names
	:param a: a Person
	:param b: a Person
	:return: True if a comes before b alphabetically and False otherwise
	"""
	global cost
	cost+=1
	if (a.first == b.first): #if same
		return a.last <= b.last
	return a.first <= b.first
	
def order_last_name(a, b):
	"""
	Orders two people by their last names
	:param a: a Person
	:param b: a Person
	:return: True if a comes before b alphabetically and False otherwise
	"""
	global cost
	cost=cost+1
	if (a.last == b.last): #if same
		return a.first <= b.first
	return a.last <= b.last

def is_alphabetized(roster, ordering):
	"""
	Checks whether the roster of names is alphabetized in the given order
	:param roster: a list of people
	:param ordering: a function comparing two elements
	:return: True if the roster is alphabetized and False otherwise
	"""
	for i in range(0,len(roster)-1): #goes through full roster
		if not ordering(roster[i],roster[i+1]): #makes sure that all are ordered
												#based on a given ordering
			return False
	return True

def merge(roster, ordering, l, mid, r): 
	"""
	merges two smaller lists that are divisions of the roster
	orders them according to the merge sort algorithm
	"""
	x = int(mid - l + 1) #variables for array sizes
	y = int(r - mid)
 
 	#new temp arrays
	L = [None] * (x)
	R = [None] * (y)
 
 	#copies data from roster to smaller arrays
	for i in range(0 , x):
		L[i] = roster[l + i]

	for j in range(0 , y):
	    R[j] = roster[mid + 1 + j]

	i = 0  #variables for comparing small lists   
	j = 0    
	k = l 

	while i < x and j < y : #goes through all of the smaller lists
		if ordering(L[i], R[j]):
			roster[k] = L[i]
			i += 1
		else:
		    roster[k] = R[j]
		    j += 1
		k += 1

	#copy remaining persons if there are any
	while i < x:
	    roster[k] = L[i]
	    i += 1
	    k += 1

	while j < y:
	    roster[k] = R[j]
	    j += 1
	    k += 1

def mergeSort(roster, ordering, l, r):
	"""
	function which is recursive to divide up the roster
	into smaller lists of persons and sort them
	based on the mergesort algorithm
	"""
	if l < r:
		mid = int((l+(r-1))/2)
		mergeSort(roster, ordering, l, mid)
		mergeSort(roster, ordering, mid+1, r)
		merge(roster, ordering, l, mid, r)
	
def alphabetize(roster, ordering):
	"""
	Alphabetizes the roster according to the given ordering
	:param roster: a list of people
	:param ordering: a function comparing two elements
	:return: a sorted version of roster
	:return: the number of comparisons made
	"""
	l=0
	r=len(roster)-1
	#calls merge sort algorithm which ensures
	#O(nlogn) runtime in best and worst case
	mergeSort(roster, ordering, l, r)


	return (list(roster), cost)


	

