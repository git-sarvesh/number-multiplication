print('welcome to my table learning platform:) ')
ourNum = int(input("pls enter the positive nmber you want to get the multiplication for: "))
ourRange = range(1,21)
for x in ourRange:
    result = ourNum * x
    print(ourNum," * ",x," = ",result)