with open("input.txt", 'r') as reader:
	file = reader.read()

s = 0

p = {'A': 1, 'B': 2, 'C': 3}

towin =  {'A': 'B', 'B': 'C', 'C': 'A'}
tolose = {'A': 'C', 'B':'A', 'C':'B'}


def calc(o, m):
	s = 0
	
	if m == 'X':  # lost  0
		s += p[tolose[o]]
	elif m == 'Y': # draw 3
			s += p[o] + 3
	elif m == 'Z': # win 6
		s += p[towin[o]] + 6

	return s

for line in file.split('\n'):
	o, m = line.split()

	if o == 'A':
		s += calc(o, m)			
	elif o == 'B':
		s += calc(o, m)
	elif o == 'C':
		s += calc(o, m)

print(s)
	
with open("output.txt", 'w') as writer:
	writer.write(str(s))