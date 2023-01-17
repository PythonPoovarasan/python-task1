#default constructor:
"""
class student:
    def __init__(self):
        print("this is a default or null constructor:")
        self.rno=int(input("enter a roll number:"))
        self.name=input("enter a name: ")
        self.mark=int(input("enter a mark:"))
    def dis(self):
        print("roll number:",self.rno)
        print("name:",self.name)
        print("mark:",self.mark)
s1=student()
s1.dis()
"""
#argument constructor
"""
class student:
    def __init__(self,rno,name,mark):
        print("this is aargument constructor:")
        self.rno=rno
        self.name=name
        self.mark=mark
    def dis(self):
        print("roll number:",self.rno)
        print("name:",self.name)
        print("mark:",self.mark)
s1=student(101,"poo",99)
s1.dis()
"""
#copy constructor
"""
class student:
    def __init__(self,rno,name,mark):
        print("this is a copy constructor:")
        self.rno=rno
        self.name=name
        self.mark=mark
    def dis(self):
        print("roll number:",self.rno)
        print("name:",self.name)
        print("mark:",self.mark)
s1=student(12,"poo",99)
s2=student(15,"king",100)
s1.dis()
s2.dis()
s2=s1
s1.dis()
s2.dis()
"""
