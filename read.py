data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		if 'good' in line:
			data.append(line)
print(len(data))