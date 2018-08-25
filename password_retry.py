a = 0

while a < 3:
	password = input('請輸入密碼：')
	if password == 'a123456':
		print('登入成功！')
		break
	else:
		a += 1
		b = 3 - a
		print('密碼錯誤 還有{}次機會'.format(b))

