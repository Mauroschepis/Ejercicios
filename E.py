print("introduce el valor de X")
x=int(input(""))
e=1
Num=1
Den=1
l=1
while not Num/Den<0.000001:
    Num=x**l
    Den=Den*l
    l=l+1
    e = e + Num / Den
print ("el valor de X es",e)
