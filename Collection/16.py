num_per_line=10
def printChars(ch1, ch2, numberPerLine):
    count=0
    for i in range (ch1,ch2):
        count+=1
        print(i,end= '')
        if count % num_per_line==0:
            print()
printChars(1, 90, 10)
