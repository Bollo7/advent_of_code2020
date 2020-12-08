import sys
import copy
file = 'inputs/input_adv8.txt'
with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)
print(lines)

raw_1 = ['nop +0', 'acc +1', 'jmp +4', 'acc +3', 'jmp -3', 'acc -99', 'acc +1', 'jmp -4', 'acc +6']

for i in range(len(raw_1)):
	raw_1[i] = raw_1[i].split(' ')

for i in range(len(lines)):
	lines[i] = lines[i].split(' ')

def sequence(inp, setting = 'part1'):
	if setting == 'part2':
		new_inps = []
		results = []
		for instance in range(len(inp)):
			new_inp = copy.copy(inp)
			if new_inp[instance][0] == 'nop':
				new_inp[instance] = ['jmp', inp[instance][1]]
			if new_inp[instance][0] == 'jmp':
				new_inp[instance] = ['nop', inp[instance][1]]
			else:
				continue
			new_inps.append(new_inp)
			accumulator = 0
			iteration = 0
			i = 0
			traversed = set()
			while iteration < 1000:  # set boundaries
				try:
					iteration += 1
					if i in traversed: # if index is already traversed --> break
						results.append((accumulator, i, iteration, traversed))
						break
					traversed.add(i) # add index if unseen
					if new_inp[i][0] == 'nop':
						i += 1  # traverse further
					elif new_inp[i][0] == 'acc':
						i += 1  # traverse further
						accumulator += int(new_inp[i-1][1][:])
					elif new_inp[i][0] == 'jmp':
						i += int(new_inp[i][1][:])  # traverse further or backwards, depending on the sign
				except IndexError:
					return (accumulator, i, iteration, traversed)

	else:
		accumulator = 0
		iteration = 0
		i = 0
		traversed = set()
		while iteration < 1000: # set boundaries
			iteration += 1
			if i in traversed: # if index is already traversed --> break
				break
			traversed.add(i)
			if inp[i][0] == 'nop':
				i += 1 # traverse further
			elif inp[i][0] == 'acc':
				i += 1 # traverse further
				accumulator += int(inp[i-1][1][:])
			elif inp[i][0] == 'jmp':
				i += int(inp[i][1][:]) # traverse further or backwards, depending on the sign
		return accumulator, i, iteration, traversed

print(f'Part 1: {sequence(lines, "part1")[0]}')
print(f'Part 2: {sequence(lines, "part2")[0]}')


