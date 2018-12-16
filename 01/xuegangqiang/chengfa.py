#encoding: utf8
# xuegqcto@aliyun.com
# python3.6

# 打印乘法口诀表
i = 1
while i <=9:
    j = 1
    while j <= i:
        print(str(j) + '*' + str(i)  + '=' + str(j * i), end=' ')
        j += 1
    print()
    i += 1

