#function for get maximum
maximum=[0,-1]
def maxi(x,y): #indexnumber(x) and marks(y) order
    global maximum
    if y>maximum[1]:
            maximum[0]=x
            maximum[1]=y
#Get index number and assign into index and m
index_number=input("Enter Index Number : ")
index=[]
m=[]
index_number=index_number.upper()
while index_number != "END" :
    marks=float(input("Enter marks : "))
    index=index+[index_number]
    m=m+[marks]
    index_number=input("Enter Index Number : ")
    index_number=index_number.upper()
#access each value from list(index , m) and check prize type and check highest marks
print()
print("-------Final Report-------")
for i in range(0,len(index)):
    if m[i]>=75 and m[i]<=79:
        print(index[i]," : ","Merit")
        maxi(index[i],m[i])
    elif m[i]>=80 and m[i]<=84:
        print(index[i]," : ","Bronze")
        maxi(index[i],m[i])
    elif m[i]>=85 and m[i]<=89:
        print(index[i]," : ", "Silver")
        maxi(index[i],m[i])
    elif m[i]>=90 and m[i]<=100:
        print(index[i]," : ","Gold")
        maxi(index[i],m[i])
    else:
        print(index[i]," : ","No Prize")
        maxi(index[i],m[i])        
print()
print("-------Special Prize-------")
print(maximum[0],maximum[1])
