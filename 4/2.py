with open("input.txt", 'r') as reader:
	file = [l.strip() for l in reader.readlines()]

s = 0

for i in file:
	l,m = i.split(',')
	r1, r2 = map(int, l.split('-'))
	r3, r4 = map(int, m.split('-'))

	if (r2 < r3) or (r4 < r1): s += 1
	# r1..r2........   #.......r1...r2.
	# ........r3..r4   #r3..r4.........

print(len(file)-s)

with open("output.txt", 'w') as writer:
	writer.write(str(len(file) - s))