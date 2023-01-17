#greatest among 2 number
"""
a=30
b=20
if a>b:
    print("a is greatest number")
else:
    print("b is  greatest number")
"""
#smallest among 2 number
"""
c=int(input("enter a number:"))
d=int(input("enter a number:"))
if c<d:
    print(" c is a smallest number")
else:
    print(" d is a smallest number")
"""
#find given no is odd or even
"""
n=int(input("enter a number:"))
if n%2==0:
    print("even")
else:
    print("odd")
"""   
#find given no is +ve or -ve or zero
"""
p=int(input("ente a p value:"))
if p>0:
    print("+ve value")
elif p<0:
    print("-ve value")
else:
    print("zero")
"""
#greatest among 3 number
"""
p=12
q=35
r=25
if p>q:
    print(" p is greatest number")
elif q>r:
    print(" q is greatest number")
elif r>p:
    print(" r is  greatest number")
else:
    print("thank you")
"""
#smallest among 3 number
"""
p=17
q=5
r=2
if p<q:
    print(" p is smallest number")
elif q<r:
    print(" q is smallest number")
elif r<p:
    print(" r is  smallest number")
else:
    print("thank you")
"""
# EB Bill
"""
unit=int(input("enter yout unit value:"))
if unit<=100:
    print("unit=",unit*0)
elif unit>=101 and unit<=200:
    print("unit=",unit*4)
elif unit>=201 and unit<=300:
    print("unit=",unit*6)
elif unit>=301:
    print("unit=",unit*7)
else:
    print("thank you")
"""
#mark list (total, average, result,grade)
"""
m1=int(input("enter a mark1:"))
m2=int(input("enter a mark2:"))
m3=int(input("enter a mark3:"))
m4=int(input("enter a mark4:"))
m5=int(input("enter a mark5:"))
total=m1+m2+m3+m4+m5
ave=total/5
print("total:",total)
print("ave:",ave)
if m1>34 and m2>34 and m3>34 and m4>34 and m5>34:
    res="pass"
else:
    res="fail"
print("result:",res)
if res=="pass" and ave>=85:
    print("grade: A")
elif res=="pass" and ave>=75:
    print("grade: B")
elif res=="pass" and ave>=55:
    print("grade: C")
elif res=="pass" and ave>=45:
    print("grade: D")
elif res=="pass" and ave>=35:
    print("grade: E")
else:
    print("grade: No")
"""
#leap year or not
"""
year=2024
if year%400==0 and year%100==0:
    print("leap year1")
elif year%4==0 and year%100!=0:
    print("leap year2")
else:
    print(" not a leap year")
"""
# for loop
"""
i=1
e=3
total=0
for i in range(e):
    total= total+i
    print(i, end="+")
    i=i+1
    print(e)
    print(total+e)
"""    
#greatest among 3 number another methgod
"""    
p=12
q=35
r=25
if p>=q and q<=p:
    print(" p is greatest number")
elif q>=r and r<=q:
    print(" q is greatest number")
elif r>=p and p<=r:
    print(" r is  greatest number")
else:
    print("thank you")
"""    
    
