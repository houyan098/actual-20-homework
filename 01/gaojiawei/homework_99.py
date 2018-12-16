for i in range(1,10):
     for j in range(1,10):
         count = i * j
         print(f'{i} * {j} = {count} ',end = ' ')
         if j == 9:
             print('\n')
