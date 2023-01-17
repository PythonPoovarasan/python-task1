#simple if
"""
mark=78
if mark>34:
    print("pass")
"""
#if else
"""
mark=int(input("enter a mark:"))
if mark>34:
    print("pass")
else:
    print("fail")
    print("good")
    print("thank you")
"""
#elif statement
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
