"""
for i in range(20):
    if i==10:
        break
    print(i)
print("end")
"""
"""
for i in range(20):
    print(i)
    if i>10:
        break
print("end")
"""
"""
for i in range(20):
    print(i)
    if i>=10 or i<=15:
        break
print("end")
"""
"""
for i in range(20):
    print(i)
    if i>=10 and i<=15:
        break
print("end")
"""
"""
for i in range(20):
    print(i)
    if i>=10 or i<=15:
        continue
print("end")
"""
"""
for i in range(20):
    if i>=10 or i<=15:
        continue
    print(i)
print("end")
"""
"""
for i in range (20):
    print(i)
    if i>=10 and i<=15:
        pass
    else:
        break
print("end")
"""
"""
t="poovarasan"
t[0]
print("char to ascii:",ord(t[0]))
print("ascii to char:",chr(112))
"""
"""
t=input("enter a name:")
len=len(t)
for i in range(len):
    if ord (t[i])>=97:
        s=ord(t[i])-32
        print( chr(s),end =" ")
    else:
        print(t[i],end=" ")
"""


#use define function
"""
def display():
    n1=12
    n2=45
print(n1+n2)
display()
"""
#with arg
"""
def display(n1,n2):
    print("total:",(n1+n2))
n1=int(input("ente a n01:"))
n2=int(input("enter a n02:"))
display(n1,n2)
"""
#with return
"""
def display():
    n1=int(input("enter a no 1:"))
    n2=int(input("ente a no 2:"))
    return n1+n2
ans=display()
print("total:",ans)
"""
#global variable
"""
s=1
def display(n):
    global s
    print(s)
    s=s+1
    if n+1==s:
        return
    display(n)
n=int(input("enter a n value:"))
display(n)
"""

# recursion
"""
def display(n):
    print(n)
    n=n-1
    if n==0:
        return
    display(n)
display(10)
"""
#FUNCTION VARIABLE=>default argument
"""
def sky(name,msg="welcome to sky"):
    print("Hi!",name,msg)
sky("poovarasan")
"""
# keyword argument
"""
def show(rollno,name,mark):
    print("roll no:",rollno)
    print("name:",name)
    print("mark:",mark)
show(name="poovarasan",rollno="1234",mark="199")
"""
#arbitrary argument
"""
def friends(*names):
    for name in names:
        print("Hi",name)
friends("poo","rangith","pavi","saran")
"""
#lambda function
#basic lambda
"""
show=lambda var:print(var*var)
show(5)
"""
#lambda with filter=>normal
"""
k=[11,22,78,54,33,71,61,51]
ans=[]
for i in range(len(k)):
    if k[i]%2==0:
        ans.append(k[i])
    print(ans)
"""
"""
k=[11,22,33,44,55,66,88]
ans=list(filter(lambda var:var%2==0,k))
print(ans)
"""
"""
def display(s,n):
    print(s)
    s=s+1
    if n+1==s:
        return
    display(s,n)
display(1,15)
"""
