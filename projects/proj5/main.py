from HashMap import HashMap

def main():
	letters = ['alfa', 'bravo', 'charlie', 'delta']

	hashmap = HashMap()
	for l in letters:
		hashmap[l] = l
	for l in letters:
		del hashmap[l]
main()