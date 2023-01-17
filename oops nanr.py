#no argument no return
"""
class student():
    def getinfo(self):
        self.rollno=int(input("enter a roll number:"))
        self.name=input("enter a name:")
        self.mark=int(input("enter a mark:"))
    def dis(self):
        print("roll number:",self.rollno)
        print("name:",self.name)
        print("mark:",self.mark)
s1=student()
s1.getinfo()
s1.dis()
"""
#with argument no return
"""
class student():
    def getinfo(self,rollno,name,mark):
        self.rollno=rollno
        self.name=name
        self.mark=mark
    def dis(self):
        print("roll number:",self.rollno)
        print("name:",self.name)
        print("mark:",self.mark)
s1=student()
s1.getinfo(101,"poo",199)
s1.dis()
"""
#with argument with return
"""
class student():
    def getinfo(self,rollno,name,mark):
        self.rollno=rollno
        self.name=name
        self.mark=mark
        return self
s1=student()
self=s1.getinfo(101,"poo",199)
print("roll number:",self.rollno)
print("name:",self.name)
print("mark:",self.mark)
"""
#no argument with return
"""
class student():
    def getinfo(self):
        self.rollno=int(input("enter a roll number:"))
        self.name=input("enter a name:")
        self.mark=int(input("enter a mark:"))
        return self
s1=student()
self=s1.getinfo()
print("roll number:",self.rollno)
print("name:",self.name)
print("mark:",self.mark)
"""
#mark list=>you try
"""
class student():
    def getinfo(self,rollno,name,tamil,english,maths,science,social):
        self.rollno=rollno
        self.name=name
        self.tamil=tamil
        self.english=english
        self.maths=maths
        self.science=science
        self.social=social
        if tamil>34 and english>34 and maths>34 and science>34 and social>34:
            print("you score:pass")
        else:
            print("hard work must")
    def dis(self):
        print("rollno:",self.rollno)
        print("name:",self.name)
        print("tamil:",self.tamil)
        print("english:",self.english)
        print("maths:",self.maths)
        print("science:",self.science)
        print("social:",self.social)
    
s1=student()
s1.getinfo(101,"poo",99,98,98,99,96)
s1.dis()
"""
