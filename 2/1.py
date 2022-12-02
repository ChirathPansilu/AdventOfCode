with open("input.txt", 'r') as reader:
	file = reader.read()

s = 0

p = {'X': 1, 'Y': 2, 'Z': 3}

for line in file.split('\n'):
	o, m = line.split()

	if o == 'A':
		if m == 'Y': 
			s+=6
		elif m == 'X':
			s+=3
	elif o == 'B':
		if m == 'Z': 
			s+=6
		elif m == 'Y':
			s+=3
	elif o == 'C':
		if m == 'X': 
			s+=6
		elif m == 'Z':
			s+=3
	s += p[m]

print(s)
	
with open("output.txt", 'w') as writer:
	writer.write(str(s))