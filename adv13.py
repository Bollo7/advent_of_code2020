import re
import numpy as np
import operator


file = 'inputs/input_adv13.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

pat = re.compile(r'\d*')

newest = re.findall(pat, lines[1])
new = set(newest)
new.remove('')

targ = int(lines[0])
starting_points = []
for i in new:
	i = int(i)
	start = round(targ/i)
	start = start * i
	dif = targ - start
	starting_points.append((start, i, dif))
print(starting_points)

## Part 2 ##
time_stamps = [i for i in range(len(newest))]
new_time = list(map(lambda x,y:(x,y), newest, time_stamps))

data = []
for x,y in new_time:
	if x == '':
		pass
	elif int(x) > 0:
		data.append((y,int(x)))

jump = data[0][1]
time_stamp = 0
for delta, bus_id in data[1:]:
	while (time_stamp + delta) % bus_id != 0:
		time_stamp += jump
	jump *= bus_id
print(time_stamp//2)