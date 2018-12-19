# conding: utf-8
import random

# 获取随机数
random_num = random.randint(0, 100)
err_cnt = 0

# 只有答对才会跳出
while True:
	# 错误5次后退出
	if err_cnt < 5:
		# 接收用户输入
	    input_num = input('猜中数字有奖，请输入:')
	    # 判断是否为数字
	    if input_num.isdigit():
	        # 转换为数字后比对
	        if int(input_num) > random_num:
	            print('数字大了，再来！')
	            err_cnt += 1
	            continue
	        elif int(input_num) < random_num:
	            print('数字小了，再来！')
	            err_cnt += 1
	            continue
	        else:
	            print('猜对了，你真棒!!!')
	            break
	    else:
	        print('数字才可以哦，再来吧。')
	        continue
	else:
		print('你太笨了，下次再来吧~~')
		break


