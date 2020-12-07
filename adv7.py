from collections import defaultdict, deque

file = 'inputs/input_adv7.txt'
with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

for i in range(len(lines)):
	lines[i] = lines[i].replace('.', '')
	lines[i] = lines[i].replace('contain', ',')
	lines[i] = lines[i].replace('bags', '')
	lines[i] = lines[i].replace('bag', '')
	lines[i] = lines[i].replace(' ', '')
	lines[i] = lines[i].replace(',', ' ')
	lines[i] = lines[i].split(' ')

parents = defaultdict(list)
contents = defaultdict(list)

for i in range(len(lines)):
	container = lines[i][0]
	contento = lines[i][1:]
	for j in contento:
		if j.startswith('no'):
			n = 0
		else:
			try:
				n = int(j[0])
			except ValueError:
				print(f'This is erroneous string: {j}')
		parents[j[1:]].append(container)
		contents[container].append((n,j[1:]))

# parent bag
needed = 'shinygold'

# look at every bag down the tree, until every children bag is seen
seen_bags = set()
gg = deque([needed])
while gg:
	i = gg.popleft()
	if i in seen_bags:
		continue
	seen_bags.add(i)
	for j in parents[i]:
		gg.append(j)
print(f'Part 1: {len(seen_bags)-1}') # remove shinygold itself

#recursive for part 2
def size(bag='shinygold'):
	answer = 0 # start from one
	for (amount, b) in contents[bag]:
		answer += amount*(1+size(b))
	return answer
print(f'Part 2: {size(needed)}') # remove shinygold itself
