#nomal
a=1
b=2
sum = a + b
minus = b-a
mulltiply=a*b
divide=b/a

#OOP

def SUM(a,b,c):
    sum =int(a)+int(b)+int(c)
    return sum
def MINUS(a,b):
    sum =int(a)-int(b)
    return sum
def MULLTIPLY(a,b):
    sum =int(a)*int(b)
    return sum
def DIVIDE(a,b):
    sum =int(a)/int(b)
    return sum

operate = input("1=Sum,2=Minus,3=Mulltiply,4=Divide : ")
if(operate=="1"):
    inp1 =input("A : ")
    inp2 =input("B : ")
    inp3 =input("C : ")
    print("SUM =",SUM(inp1,inp2,inp3))
elif(operate=="2"):
    inp1 =input("A : ")
    inp2 =input("B : ")
    print("MINUS =",MINUS(inp1,inp2))
elif(operate=="3"):
    inp1 =input("A : ")
    inp2 =input("B : ")
    print("MULLTIPLY =",MULLTIPLY(inp1,inp2))
elif(operate=="4"):
    inp1 =input("A : ")
    inp2 =input("B : ")
    print("DIVIDE =",DIVIDE(inp1,inp2))
else:
    print("Not Found")




#print("SUM =",SUM(11,12,13))
#print("MINUS =",MINUS(100,12))
#print("MULLTIPLY =",MULLTIPLY(100,12))
#print("DIVIDE =",DIVIDE(100,12))