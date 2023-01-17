n1=int(input("enter number of round:"))
n2=int(input("enter number of passes per round:"))
def classname():
    num=0
    for i in range(1,50):
        for j in range(1,6):
            num=num+1
            if num==((n1*n2)+1):
                print((num-1),"th time ball with person:",j)
                break
classname()
