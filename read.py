data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		if len(line) < 100:
			data.append(line)
print('一共有', len(data), '長度小於100的留言')