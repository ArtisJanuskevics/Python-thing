import csv
from datetime import datetime
date=[]
time=""
y=0
z=0

def remove():
    x=0
    b=0
    print("which date you want to clear ?")
    dates=input()
    date=dates.split(';')
    with open("data.csv", "r") as file:
        cs = file.readlines()
        fail = [line.strip() for line in cs]
        for line in fail:
            lin=line.split(';')
            if(date[0]==lin[0] and date[1]==lin[1] and date[2]==lin[2]):
                b=1
                break
            x=x+1
    if(b==1):
        del fail[x]
        print("done")
    else:
        print("no matching dates found")
    with open("data.csv","w") as file:
        file.write("\n".join(fail))
    choose()

def check():
    z=0
    print("about what date you want to know ?(year;month;day)")
    time=input().split(";")
    with open("data.csv") as file:
        for line in file:
            lin=line.split(";")
            if(lin[0]==time[0] and lin[1]==time[1] and lin[2]==time[2]):
                print(lin[3])
                z=1
                break
        if(z==0):
            print("nothing")
    choose()
    

def choose():
    
    print("what do you want to do ?")
    choice=input()
    

    if(choice=="check"):
        check()
    elif(choice=="add"):
        add()
    elif(choice=="remove"):
        remove()
    elif(choice=="exit"):
        return
    else:
        print("incorrect command, try again")
        choose()




def add():
    addtext=""
    print("at what date would you like to add ?(year;month;day)")
    dates=input()
    print("what do you want to add ?")
    txt=input()
    date=dates.split(";")
    x=0
    y=0
    with open("data.csv", "r") as file:
        cs = file.readlines()
        fail = [line.strip() for line in cs]
        for line in fail:
            lin=line.split(";") 
            if(int(date[0])<int(lin[0]) or  int(date[1])<int(lin[1]) and int(date[0])==int(lin[0]) or int(date[2])<int(lin[2])and int(date[0])==int(lin[0]) and int(date[1])==int(lin[1])):
                print(x)
                break   
            x=x+1
            print(date[0]+"     "+lin[0])
        addtext=dates+";"+txt
        fail.insert(x,addtext)
        print(fail)

    with open("data.csv","w") as file:
        file.write("\n".join(fail))
    choose()



time=str(datetime.now().date()).split("-")
print("today in my schedule: ")
with open("data.csv") as file:
    for line in file:
        lin=line.split(";")
        if(lin[0]==time[0] and lin[1]==time[1] and lin[2]==time[2]):
            print(lin[3])
            z=1
    if(z==0):
        print("nothing")
choose()


































