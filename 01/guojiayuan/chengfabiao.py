for a in range(1 , 10):
	for b in range(1 , a+1):
		print(str(a) + '*' + str(b) + '=' + str(a*b) , end = ' ')
		if a == b:
			print('\n')
