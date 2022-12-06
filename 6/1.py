with open("input.txt", 'r') as reader:
	file = reader.read()

r = 0

for i in range(4, len(file)):
	if(len(set(file[i-4:i])) == 4):
		print(i)
		r = i
		break

with open("output.txt", 'w') as writer:
	writer.write(str(r))