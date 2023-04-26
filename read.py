sum = 0
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		sum += (len(line))
		count +=1
print(sum / count)