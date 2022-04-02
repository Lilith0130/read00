data = []
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
print(len(data))		


print(data[0]) #印出留言第一筆
print('----------------------') #分隔線
print(data[1]) #第二個留言
