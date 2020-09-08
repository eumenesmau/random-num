import random

start = input('請輸入起始範圍:')
end = input('請輸入結束範圍:')
start = int(start)
end = int(end)
num = random.randint(start, end) 
count=0
while True:
	start = str(start)
	end = str(end)
	guess = input('猜數字遊戲喔~請從' + start + '-'+ end +'以內猜出正確數字:')
	guess = int(guess)
	count += 1
	print('你目前猜了', count, '次了')
	if guess == num:
		print('這你也猜得對，太屌了吧!')
		break
	elif guess > num and guess < 101 and guess > 0:
		print('答案比你猜的', guess, '還要小')
	elif guess < num and guess < 101 and guess > 0:
		print('答案比你猜的', guess, '還要大')
	#elif guess > 100 and guess < 1:
	#	print('請從1-100以內去猜喔!')
	else:
		print('請從1-100填入數字喔!')
