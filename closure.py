# closure
"""
def poo():
    def king():
        print("this is closure concepts")
    return king
myna=poo()
myna()
saran=myna
saran()
"""
# closure argument pasing
"""
def poo():
    def king(k):
        for i in range(1,k+1):
            print("this is closure concepts",i)
    return king                                                           
myna=poo()
myna(10)
"""
#advance type closure

def poo():
    def king(k):
        for i in range(1,k+1):
            print("this is closure concepts",i)
    def priya(s):
        for i in range(s):
            print("\n flower",i)
        king(5)
    return priya                                                          
myna=poo()
myna(5)
