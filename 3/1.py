with open("input.txt", 'r') as reader:
	file = reader.readlines()

s = 0

def val(c):
	if c.islower():
		return ord(c)-96
	else:
		return ord(c)-64+26

for line in file:
	sl = line.strip()
	c1, c2 = sl[:len(sl)//2], sl[len(sl)//2:]

	s += val(list(set(c1).intersection(set(c2)))[0])

print(s)

with open('output.txt', 'w') as writer:
	writer.write(str(s))