password = 'a123456'
i = 3 #剩餘機會
while True:
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！')
		break
	else:
		i -= 1
		print('密碼錯誤 還有{}次機會'.format(i))
		if i == 0:
			break

