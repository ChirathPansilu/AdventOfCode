with open("input.txt", 'r') as reader:
	file = [l.strip() for l in reader.readlines()]

s = 0

for i in file:
	l,m = i.split(',')
	r1, r2 = map(int, l.split('-'))
	r3, r4 = map(int, m.split('-'))

	if(r3 >= r1 and r4 <= r2) or (r1 >= r3 and r2 <= r4): s += 1
	# r1........r2                #....r1...r2....
	# ...r3..r4...                #.r3.........r4.

print(s)

with open("output.txt", 'w') as writer:
	writer.write(str(s))