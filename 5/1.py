with open('stacks_input.txt', 'r') as reader:
	file = reader.readlines()

stacks = [[] for _ in range(9)]

for l in file:
	l = l.rstrip('\n').replace('[', ' ').replace(']', ' ')

	for i in range(len(l)):
		if l[i] != ' ':
			stacks[i//4].append(l[i])

ins = []
with open('instructions.txt', 'r') as reader:
	for l in reader.readlines():
		t = []
		for s in l.split():
			if s.isdigit():
				t.append(int(s))
		ins.append(t)

for i in ins:
	f = i[1] - 1
	t = i[2] - 1
	c = i[0]

	r = list(reversed(stacks[f][:c]))
	r.extend(stacks[t])
	stacks[t] = r
	
	del stacks[f][:c]

s = ''

for l in stacks:
	if len(l) != 0:
		s += l[0]

print(s)

with open('output.txt', 'w') as writer:
	writer.write(s)