with open("input.txt", 'r') as reader:
	file = reader.read()

sm = [sum(map(int, c.split())) for c in file.split("\n\n")]

sm.sort(reverse=True)

mx3 = sum(sm[:3])

print(mx3)

with open("output.txt", 'w') as writer:
	writer.write(str(mx3))