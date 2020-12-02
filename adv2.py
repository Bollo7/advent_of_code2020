import re

file = 'inputs/input_adv2.txt'


with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)
	for i in range(len(lines)):
		lines[i] = str(lines[i])

print(lines)

counting = {}
numl = []
litral = []
passl = []
for i in lines:
	nums = re.match(r'\d*-\d+', i)
	litra = re.search(r'\w:', i)
	password = re.search(r'[a-z]{3,}', i)
	numl.append(nums.group().replace('-', ','))
	litral.append(litra.group()[0])
	passl.append(password.group())

for i in range(len(numl)):
	numl[i] = numl[i].split(',')
	for j in range(len(numl[i])):
		numl[i][j] = int(numl[i][j])

print(numl,'\n', litral,'\n', passl)


from collections import Counter

def check_validity(numl, litral, passw):
	dic = {}
	for i in passw:
		dic[i] = dic.get(i, 0) + 1
	try:
		if dic[litral] in range(numl[0], numl[1]+1):
			return True
		else:
			return False
	except KeyError:
		return False

ans = []
debug = []
for i,j,k in zip(numl, litral, passl):
	debug.append((i,j,k,check_validity(i,j,k)))
	ans.append(check_validity(i, j, k))

print(debug)
print(Counter(ans))

### Part 2 ###

def check_validity_adv(numl, litral, passw):
	if passw[numl[0]-1] == litral and passw[numl[1]-1] != litral:
		return True
	elif passw[numl[0]-1] != litral and passw[numl[1]-1] == litral:
		return True
	else:
		return False

ans = []
debug = []
for i,j,k in zip(numl, litral, passl):
	debug.append((i,j,k,check_validity_adv(i,j,k)))
	ans.append(check_validity_adv(i, j, k))

print(debug)
print(Counter(ans))