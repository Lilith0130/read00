# 讀取檔案
# r = 讀去模式 read(r)

# w = 寫入模式 write(w)
data = []
with open('food.txt', 'r') as f:
	for line in f:
		#print(line)
		data.append(line.strip())



print(data)