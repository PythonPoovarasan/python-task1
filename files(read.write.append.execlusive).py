#read method
"""
f=open("C:/Users/Ganesh/Desktop/poovarasan Python/try.py")
print(f.read())
"""
#write method
"""
f=open("C:/Users/Ganesh/Desktop/poovarasan Python/files(read.write.append.execlusive).py","w")
data=input("enter a data :")
f.write(data)
f.close()
"""
#append methoid
"""
f=open("C:/Users/Ganesh/Desktop/poovarasan Python/files(read.write.append.execlusive).py","a")
data=input("enter a data :")
f.write("\n"+data)
f.close()
"""

#execlusive method=>new TAP OPEN RUN PROGRAM ONLY ONE TIME RUN AGAIN RUN THE AGAIN NEW FILE SAVE
"""
f=open("C:/Users/Ganesh/Desktop/poovarasan Python/files(read.write.append.execlusive).py","x")
data=input("enter a data :")
f.append("\n"+data)
f.close()
"""
