highest = 0
for i in range(100,1000):
    for j in range(100, 1000):
        product = i * j
        strProduct = str(product)
        length = len(strProduct)
        correct = True
        if (length % 2 == 0):
            for k in range(0,int(length/2)):
                if (strProduct[k] == strProduct[(length-1-k)]):
                    pass
                else:
                    correct = False
        else:
            middle = int(length/2)
            strProduct = strProduct[0:middle] + strProduct[middle+1:]
            #print(strProduct)
            for k in range(0,int((length-1)/2)):
                if (strProduct[k] == strProduct[(length-2-k)]):
                    pass
                else:
                    correct = False
        if correct:
            if product > highest:
                highest = product
print(highest)

#Answer - 906609
