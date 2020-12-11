
file = 'inputs/input_adv10.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

for i in range(len(lines)):
	lines[i] = int(lines[i])

raw_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
raw_2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3]


raw_1 = sorted(raw_1)
raw_2 = sorted(raw_2)
lines = sorted(lines)

new = []
newer = []
adap = 0
for i in lines:
	dif = abs(adap - i)
	if  0 < dif <= 3:
		adap += dif
		new.append(dif)
print(f'Part 1: {new.count(1) * (new.count(3)+1)}')

## Part 2 ##

from collections import defaultdict

def all_combs(arr):
	arr.insert(0, 0), arr.append(arr[-1]+3)
	d = defaultdict(int)
	d[0] = 1

	for i in sorted(arr):
		for dif in range(1,4):
			next_i = i + dif
			if next_i in arr:
				d[next_i] += d[i]
	print(f"Part 2: {d[max(arr)]}")
	return d

dd = all_combs(lines)