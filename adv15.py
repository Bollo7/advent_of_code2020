
raw_1 = [19,0,5,1,10,13]

def p2(starting_seq, iterations):
	turns = len(starting_seq) + 1
	hist = {i: e+1 for e,i in enumerate(starting_seq[:-1])}
	old_i = starting_seq[-1]
	while turns <= iterations:
		if old_i not in hist.keys():
			hist[old_i] = turns - 1
			new_i = 0
		elif old_i in hist.keys():
			new_i = turns - hist[old_i] - 1
			hist[old_i] = turns - 1
		old_i = new_i
		turns += 1
	return new_i

print(p2(raw_1, 2020))
print(p2(raw_1, 30000000))
