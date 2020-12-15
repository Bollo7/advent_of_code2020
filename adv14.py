import re
file = 'inputs/input_adv14.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)
print(lines)

raw_1 = ['mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 'mem[8] = 11', 'mem[7] = 101', 'mem[8] = 0', 'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XX1X0X']

mask = ''
mask_list = []
mem_list = []
pat = re.compile(r'mask\W+\w+')
mem_pat = re.compile(r'mem\W+(\d+)\W\W+(\d+)')
dic = {}
get_bin = lambda x, n: format(x, 'b').zfill(n)

for l in lines:
	if l.startswith('mask'):
		newmask = l.split()[-1]
		mask = newmask
	else:
		idx, val = int(re.match(mem_pat, l).group(1)), int(re.match(mem_pat, l).group(2))
		upd = []
		mem = get_bin(val, 36)
		for i, j in zip(mask, mem):
			if i == 'X' and (j == '0' or j == '1'):
				upd.append(j)
			if (i == '1' or i == '0'):
				upd.append(i)
		dic[idx] = int(''.join(i for i in upd), base=2)

print(f'Part 1: {sum(dic.values())}')

# Part 2 #