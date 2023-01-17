"""for i in range(2): #0,1,2,3,4,5,6,7
    for j in range(0,i+1):#0+1
        print("*",end=" ")
    print()
"""
"""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
"""

for i in range(8):#row
    for j in range(i,8):#column=>i=0 to space j=>7
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
 
"""
                * 
              * * * 
            * * * * * 
          * * * * * * * 
        * * * * * * * * * 
      * * * * * * * * * * * 
    * * * * * * * * * * * * * 
  * * * * * * * * * * * * * * * 
"""
"""
for i in range(8):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,8-1):
        print("*",end=" ")
    for j in range(i,8):
        print("*",end=" ")
    print()
"""
              
