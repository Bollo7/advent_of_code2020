file = 'inputs/input_adv3.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)
print(lines)

slopes = [(1,1), (1,3), (1,5), (1,7), (2,1)]
fin = 0
all_scores = []

for (i, j) in slopes:
	row = 0
	col = 0
	score = 0
	while row + 1 < len(lines):
		col += j
		row += i
		if lines[row][col%len(lines[row])] == '#':
			score += 1
	all_scores.append(score)
	print(f'Slope({i,j}): {score}')

import functools

print(functools.reduce(lambda x,y:x*y, all_scores))