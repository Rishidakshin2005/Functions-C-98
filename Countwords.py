def Countwords():
    filename=input("enter file name:")
    count=0
    file=open(filename,'r')
    for line in file:
        word=line.split()
        count=count+len(word)
    print(count)

Countwords()
