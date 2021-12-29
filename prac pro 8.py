import pickle

def pickling():
    f=open("emp.dat","wb")
    list=[]
    while True:
        ID=int(input("enter employee ID:"))
        Name=input(("Enter employee name:"))
        Desi=input("Enter employee designation")
        details=[ID,Name,Desi]
        list.append(details)
        reply=input("do you want to continue type y/n")
        if reply=='n':
            break
    pickle.dump(list,f)
    f.close()
    print("Pickling \ writing into binary files completed successfully")

def unpickling():
    f=open("emp.dat","rb")
    while True:
        try:
            reading=pickle.load(f)
            for i in reading:
                print(i)
        except EOFError:
            break
    f.close()
    print("Reading completed successfully")

pickling()
unpickling()
