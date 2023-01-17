"""
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multi(x,y):
    return x*y
def divi(x,y):
    return x/y

print("select a options:")
print("1.add")
print("2.sub")
print("3.multi")
print("4.divi")

while True:
    choice=input("enter choice(1/2/3/4):")
    
    if choice in ('1','2','3','4'):
        num1=float(input("enter a number 1:"))
        num2=float(input("enter a number 2:"))
        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice =='2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif choice =='3':
            print(num1,"*",num2,"=",multi(num1,num2))
        elif choice =='4':
            print(num1,"/",num2,"=",divi(num1,num2))
        break
else:
    print("calcluator basic program:")
"""
#hotel management bills
"""
def breakfast():
    return breakfast
def lunch():
    return lunch
def dinner():
    return dinner

print("welcome to hotel management:")
print("1.breakfast" )
print("2.lunch")
print("3.dinner")

while True:
    choice=input("enter choice(1/2/3):")
    if choice in ('1','2','3'):
        if choice=="1":
            print("welcome to breakfast:")
            idly=int(input("how many idly:"))
            dosa=int(input("how many dosa:"))
            print(idly,"*5=",idly*5)
            print(dosa,"*15=",dosa*15)
            total=(idly*5+dosa*15)
            print("total bill:",total)
            break
        if choice=="2":
            print("welcome to lunch:")
            porotta=int(input("how many porotta:"))
            briyani=int(input("how many briyani:"))
            print(porotta,"*15=",porotta*15)
            print(briyani,"*50=",briyani*50)
            total=(porotta*15+briyani*50)
            print("total bill:",total)
            break
        elif choice=="3":
            print("welcome to dinner:")
            sapathi=int(input("how many sapathi:"))
            print(sapathi,"*15=",sapathi*15)
            total=(sapathi*15)
            print("total bill:",total)
            break
    
else:
    print("items not avaliable")
"""   
"""
print("welcome to hotel:")
print("breakfast:")
idly=int(input("how many idly:"))
dosa=int(input("how many dosa:"))
print("lunch:")
porotta=int(input("how many porotta:"))
briyani=int(input("how many briyani:"))
print("dinner:")
sapathi=int(input("how many sapathi:"))
                    
if breakfast:
    print(idly,"*5=",idly*5)
    print(dosa,"*15=",dosa*15)
if lunch:
    print(porotta,"*15=",porotta*15)
    print(briyani,"*50=",briyani*50)
elif dinner:
    print(sapathi,"*15=",sapathi*15)
else:
    print("thank you ")
"""
#room booking management
"""
def totalroom():
    return totalroom
def acroom():
    return acroom
def nonacrrom():
    return nonacroom

print("welcome to hotel management:")
print("1.totalroom" )
print("2.acroom")
print("3.nonacroom")

while True:
    choice=input("enter choice(1/2/3):")
    if choice in ('1','2','3'):
        tr=20
        ac=10
        nac=10
        bac=8
        nbac=2
    if choice=="1":
        print("total room:",tr)
        print("total ac room:",ac)
        print("total non ac room:",nac)
        print("booking ac room:",bac)
        print("booking non ac rroom:",nbac)
    elif choice=="2":
        name=input("enter a customer name:")
        ac1=int(input("how many ac room:"))
        print(ac1,"*750=",ac1*750)
        total=ac1*750
        print("totalbill:",total)
        break
    elif choice=="3":
        name=input("enter a customer name:")
        nac1=int(input("how many nac:"))
        print(nac1,"*500=",nac1*500)
        total=nac1*500
        print("total bill:",total)
        break
else :
    print("not available")
"""        

