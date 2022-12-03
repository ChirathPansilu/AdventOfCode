with open("input.txt", 'r') as reader:
	file = reader.readlines()

s = 0

def val(c):
	if c.islower():
		return ord(c)-96
	else:
		return ord(c)-64+26

for i in range(0, len(file), 3):
	t = set(file[i].strip())

	for r in file[i+1:i+3]:
		t = t.intersection(set(r.strip()))

	s += val(list(t)[0])

print(s)

with open('output.txt', 'w') as writer:
	writer.write(str(s))