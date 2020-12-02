from time import perf_counter

file = 'inputs/input_adv1.txt'

n3 = []

with open(file, 'r') as f:
	lines = f.read()
	lines = lines.split('\n')
	lines.pop(-1)
	for i in range(len(lines)):
		lines[i] = int(lines[i])

# cubic speed
start = perf_counter()
for i in lines:
	for j in lines:
		for k in lines:
			if i + j + k == 2020:
				print(i, j, k, i*j*k)
				break
end = perf_counter()


print(end-start)
print(n3)

# quadratic speed
n2 = []
start = perf_counter()
for i in lines:
	for j in lines:
		if i + j == 2020:
			n2.append((i, j))
end = perf_counter()

print(end-start)
print(n2)

# itertools.combinations 
import itertools
start = perf_counter()
ii = [x for x in list(itertools.combinations(lines, 3)) if sum(x) == 2020]
end = perf_counter()
import numpy as np

print(ii)
print(end-start)



