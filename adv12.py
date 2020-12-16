from copy import deepcopy
file = 'inputs/input_adv12.txt'

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)

raw_1 = ['F10', 'N3', 'F7', 'R90', 'F11']

dirx, diry = (0, 0)
poles_x, poles_y = [0,1,0,-1], [1,0,-1,0]
direction = 1
sums = []
for i in lines:
	if i[0] == 'N':
		diry += int(i[1:])
	if i[0] == 'E':
		dirx += int(i[1:])
	if i[0] == 'W':
		dirx -= int(i[1:])
	if i[0] == 'S':
		diry -= int(i[1:])
	if i[0] == 'F':
		dirx += poles_x[direction]*int(i[1:])
		diry += poles_y[direction]*int(i[1:])
	if i[0] == 'L':
		for _ in range(int(i[1:])//90):
			direction = (direction + 3)%4
	if i[0] == 'R':
		for _ in range(int(i[1:])//90):
			direction = (direction + 1)%4

	x, y = deepcopy(dirx), deepcopy(diry)
	sums.append(abs(x) + abs(y))
	#print(dirx, diry, abs(dirx) + abs(diry))
print(sums[-1])

# Part 2 #

dirx, diry = (0, 0)
wayx, wayy = 10, 1
sums = []
for i in lines:
	if i[0] == 'N':
		wayy += int(i[1:])
	if i[0] == 'E':
		wayx += int(i[1:])
	if i[0] == 'W':
		wayx -= int(i[1:])
	if i[0] == 'S':
		wayy -= int(i[1:])
	if i[0] == 'F':
		dirx += wayx*int(i[1:])
		diry += wayy*int(i[1:])
	if i[0] == 'L':
		for _ in range(int(i[1:])//90):
			wayx, wayy = -wayy, wayx
	if i[0] == 'R':
		for _ in range(int(i[1:])//90):
			wayx, wayy = wayy, -wayx

	x,y = deepcopy(dirx), deepcopy(diry)
	sums.append(abs(x) + abs(y))
	#print(dirx, diry, abs(x) + abs(y))
print(sums[-1])

