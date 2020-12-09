file = 'inputs/input_adv9.txt'
from itertools import combinations

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

for i in range(len(lines)):
	lines[i] = int(lines[i])


raw_1 = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]
line_preamble = [int(i) for i in lines[:25]]
raw_preamble = [int(i) for i in raw_1[:5]]

def printPairs(arr, length = 5):
	new_r = []
	length = length
	for k in range(length, len(arr)):
		preamble = arr[k-length:k]
		for x, y in combinations(preamble, 2):
			if x + y == arr[k]:
				new_r.append(arr[k])
	return line_preamble + new_r

new = printPairs(lines, 25)

for i in lines:
	if i not in new:
		print(f"Part 1: {i}")
		target = i


# Part 2 #
def find_weakness(arr, target=target):
	for i in range(len(arr)):
		for j in range(i, len(arr)):
			subarray = lines[i:j]
			if sum(subarray) == target:
				return min(subarray) + max(subarray)

print(f"Part 2: {find_weakness(lines)}")
