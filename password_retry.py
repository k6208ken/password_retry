password = 'a123456'
i = 3 #剩餘機會
while i > 0:
	i -= 1
	pwd = input('請輸入密碼：')
	if pwd == password:
		print('登入成功！')
		break
	else:
		print('密碼錯誤!')
		if i > 0:
			print('還有{}次機會'.format(i))

		
