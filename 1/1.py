with open("input.txt", 'r') as reader:
	file = reader.read()

mx = max([sum(map(int, c.split())) for c in file.split("\n\n")])

print(mx)

with open("output.txt", 'w') as writer:
	writer.write(str(mx))