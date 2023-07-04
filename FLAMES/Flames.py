def found(str1,a):
    for i in str1:
        if i==a:
            return 1
    return 0

def indexf(str1,a):
    num=len(str1)
    for i in range(0,num):
        if(str1[i]==a):
            return i
        
def Flamesfn(flam,num,s):
    n=len(flam)
    n1=num+s
    if(n>1):
        while(n1>n):
            n1=n1-n
        n1=n1-1
        print(flam[n1])
        list1=[]
        for i in range(0,n):
            if(i==n1):
                i=n1
            else:
                list1.append(flam[i])
        return Flamesfn(list1,num,n1)
    else:
        print("\nYou got ",flam[0],"!!!!!! It means that ",sep="",end="")
        return flam[0]

cha=1
while(cha!=0):
    print("\n\n-------------------------------------/# F L A M E S #/--------------------------------------\n\n\n")
    str1=input("Enter 1st person Name: ")
    str2=input("\nEnter 2nd person Name: ")
    str1=str1.upper()
    str2=str2.upper()
    #print(str1)
    #print(str2)
    num1=len(str1)
    num2=len(str2)
    Flames=["F","L","A","M","E","S",]
    count=0
    reduce=0
    print("\n")
    if(num1>=num2):
        for i in range(0,num2):
            if(found(str1,str2[i])):
                reduce=reduce+1
                index=indexf(str1,str2[i])
                if(index==0):
                    str1=str1[1:len(str1)+1]
                elif(index==1):
                    str1=str1[0]+str1[2:-1]
                elif(index==len(str1)-1):
                    str1=str1[0:-2]
                else:
                    str1=str1[0:(index-1)]+str1[(index-1):-1]
    else:
        for i in range(0,num1):
            if(found(str2,str1[i])):
                reduce=reduce+1
                index=indexf(str2,str1[i])
                if(index==0):
                    str2=str2[1:len(str2)+1]
                elif(index==1):
                    str2=str2[0]+str2[2:-1]
                elif(index==len(str2)-1):
                    str2=str2[0:-2]
                else:
                    str2=str2[0:(index-1)]+str2[(index-1):-1]
    for i in range(0,len(str1)):
        count=count+1
    for i in range(0,len(str2)):
        count=count+1
    count=count-reduce
    print("Count Value is:",count,end="\n\n")
    if(count==0):
        print("Not valid...")
    else:
        indexof=Flamesfn(Flames,count,0)
        if(indexof=="F"):
            print("you are Lucky to get a Best friend like him/her.")
            from turtle import *
            color('red')
            pensize(3)
            left(90)
            forward(75)
            right(90)
            forward(100)
            backward(100)
            right(90)
            forward(75)
            left(90)
            forward(100)
            backward(100)
            right(90)
            forward(75)
        elif(indexof=="L"):
            print("perfect Couple made for each other, Enjoy your Love.")
            from turtle import *
            color('red')
            pensize(3)
            begin_fill()
            left(50)
            forward(133)
            circle(50,200)
            right(140)
            circle(50,200)
            forward(133)
            end_fill()
        elif(indexof=="A"):
            print("well Affectionated.")
            from turtle import *
            color('red')
            pensize(3)
            forward(50)
            right(60)
            forward(100)
            right(180)
            forward(200)
            left(120)
            forward(200)
            backward(100)
            left(120)
            forward(50)
        elif(indexof=="M"):
            print("you guys are more likely to get Married.")
            from turtle import *
            color('red')
            pensize(3)
            left(45)
            forward(150)
            right(135)
            forward(200)
            backward(200)
            left(135)
            backward(150)
            left(90)
            forward(150)
            left(135)
            forward(200)
        elif(indexof=="E"):
            print("run far away since you guys are Enemies.")
            from turtle import *
            color('red')
            pensize(3)
            left(90)
            forward(75)
            right(90)
            forward(100)
            backward(100)
            right(90)
            forward(75)
            left(90)
            forward(100)
            backward(100)
            right(90)
            forward(75)
            left(90)
            forward(100)
        else:
            print("you don't worry you got a sister.")
            from turtle import *
            color('red')
            pensize(3)
            left(180)
            circle(50,180)
            forward(10)
            right(90)
            circle(50,180)
    cha=int(input("\nEnter any key to Play again, Enter 0(Zero) to stop: "))