file = 'inputs/input_adv6.txt'

from collections import Counter

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n\n')

clen = []
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', ' ')
	clen.append(lines[i].split(' '))
print(clen)

### P1 ###
new = []
flatten = lambda t: [item for sublist in t for item in sublist]
for i in clen:
	nn = []
	for j in i:
		nn.append(set(j))
	new.append(nn)
print(new)

cts = []
p1_new = []
for i in range(len(new)):
	p1_new.append(flatten(new[i]))
	p1_new[i] = set(p1_new[i])
	cts.append(len(p1_new[i]))
print(p1_new)
print(sum(cts))

### P2 ###
p2_new = []
for i in new:
	k = i[0].intersection(*i)
	print(k)
	p2_new.append(len(k))

print(sum(p2_new))