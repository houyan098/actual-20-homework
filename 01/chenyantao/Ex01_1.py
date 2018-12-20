for row in range(1,10):
    for column in range(row,10):
        print(str(row)+"*"+str(column)+"="+str(row * column), end="  ")
    print("")
