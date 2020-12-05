import functools
import numpy as np
file = 'inputs/input_adv5.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

seats = [i for i in range(128)]
cols = [i for i in range(8)]

def decipher(cipher, seats, cols):
	for i in cipher:
		if i == 'F':
			f = round(len(seats) / 2)
			seats = seats[:f]
		if i == 'B':
			b = round(len(seats) / 2)
			seats = seats[b:]
		if i == 'R':
			b = round(len(cols) / 2)
			cols = cols[b:]
		if i == 'L':
			f = round(len(cols) / 2)
			cols = cols[:f]
	return seats[0], cols[0]

fun = functools.reduce
all_ids = []
for i in lines:
	seat_id = decipher(i, seats, cols)
	res = fun(lambda x,y: x*8+y, seat_id)
	all_ids.append(res)
print(f'Part 1 answer: {max(all_ids)}')

new_seats = seats
all_combs = []
for i in new_seats:
	for j in cols:
		res = i * 8 + j
		all_combs.append(res)

for i in all_combs[min(all_ids):max(all_ids) + 1]:
	if i not in all_ids:
		print(f'Your seat from part 2 is: {i}')

