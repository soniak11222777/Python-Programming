number_per_line= 10
count=0
for i in range (100,201):
    if (i %6==0 and i%5!=0) or (i%5==0 and i%6!=0):
        count+=1
        print(format(i, "5d"),end = '')
        if count % number_per_line==0:
            print()

