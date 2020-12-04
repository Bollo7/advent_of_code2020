import json
import re
from collections import Counter


with open('inputs/input_adv4.txt', 'r') as f:
	lines = f.read()
	lines = lines.split('\n\n')

clen = []
for i in range(len(lines)):
	lines[i] = lines[i].replace('\n', ' ')
	clen.append(lines[i].split(' '))

lst_of_dcts = []
for b in clen:
	dct = {}
	for k in b:
		try:
			i = k.split(':')
			dct[i[0]] = i[1]
		except IndexError:
			pass
	lst_of_dcts.append(dct)
chec = list(lst_of_dcts[0].keys())
chec.pop(1)

def checker(cts, chec, mode='advanced'):
	count_false = 0
	count_true = 0
	truthy, falsy = [], []

	# rules for part 2
	eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	def hgt(i):
		patt = re.compile(r'\d+')
		if i.endswith('cm'):
			tet = 150 <= int(re.match(patt, i).group()) <= 193
			return tet
		if i.endswith('in'):
			tet = 59 <= int(re.match(patt, i).group())  <= 76
			return tet
		else:
			return False

	for i in cts:
		keys = list(i.keys())
		if 'cid' in keys:
			keys.remove('cid')
		if all(j in keys for j in chec):
			count_true += 1
			if (int(i['byr']) in range(1920, 2003) and
				int(i['iyr']) in range(2010, 2021) and
				int(i['eyr']) in range(2020, 2031) and
				(i['hcl'].startswith('#') and len(i['hcl']) == 7) and
				i['ecl'] in eye_color and
				len(i['pid']) == 9 and
				hgt(i['hgt'])):
				truthy.append(i)
			else:
				falsy.append(i)
		else:
			count_false += 1
	return count_true, count_false, truthy, falsy

t_pt1, f_pt1, t_pt2, f_pt2 = checker(lst_of_dcts, chec, mode='advanced')

print(f'part one: {t_pt1}, part two: {len(t_pt2)}')