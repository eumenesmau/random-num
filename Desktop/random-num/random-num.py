import random

num = random.randint(1 ,100) 
#if guess > 100 and guess < 1:
#	print('請輸入1-100以內的數字')
#	SystemExit
while True:
	guess = input('猜數字遊戲喔~請從1-100以內猜出正確數字:')
	guess = int(guess)
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
