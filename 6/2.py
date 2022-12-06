with open("input.txt", 'r') as reader:
	file = reader.read()

r = 0

for i in range(14, len(file)):
	if(len(set(file[i-14:i])) == 14):
		print(i)
		r = i
		break

with open("output.txt", 'w') as writer:
	writer.write(str(r))