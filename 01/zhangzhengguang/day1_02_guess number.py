# ----------------作业二：-----------
import random
count=0
while count<5:
    random_num = random.randint(0, 100)
    usr_input=int(input("你猜！猜对了我嫁给你！"))
    if usr_input > random_num:
        print("猜小了")

    elif usr_input < random_num:
        print("猜大了")
    else:
        print("兄弟你可以去买彩票了！嫁给你是不存在的！")
        break
    count+=1
    if count == 5:
        agin=input("菜鸡!再给你一次机会？（y/n):")
        if agin == 'y':
            count=0
        else:
            break
