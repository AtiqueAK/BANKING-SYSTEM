import mysql.connector as a
mydb=a.connect(host="localhost",user="root",password="1234",database="Gawde bank")
print(mydb)
print("Connection Done")

A=open("project.txt","w+")
print("File saved succesfully")

def OpenAccount():
    n=input("Enter Name:")
    ac=input("Enter Account No:")
    pin=input("Enter Account pin.no:")
    dob=input("Enter D.O.B:")
    ph=input("Enter Phone:")
    add=input("Enter Address:")
    ob=input("Enter opening balance:")
    table1=(n,ac,dob,ph,add,ob)
    table2=(n,ac,ob)
    sql1='insert into account values(%s,%s,%s,%s,%s,%s)'
    sql2='insert into amount valves(%s,%s,%s)'
    main()

def Deposite():
    ac=int(input("Enter Account No:"))
    pin=int(input("Enter account pin.no:"))
    amt=int(input("Enter Amount:"))
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchonel()
    tam=myresult[0]+am
    sql="Update amount set balance=%s where acno=%s"
    d=(tam.ac)
    c.execute(sql,d)
    mydb.commit()
    main()

def withdraw():
    ac=int(input("Enter Account No:"))
    pin=int(input("Enter account pin.no:"))
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchonel()
    tam=myresult[0]-am
    sql="Update amount set balance=%s where acno=%s"
    d=(tam.ac)
    c.execute(sql,d)
    mydb.commit()
    main()

def balance():
    ac=int(input("Enter Account No:"))
    pin=int(input("Enter account pin.no:"))
    a="select balance from amount where acno=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchonel()
    print("Balance for Amount:",ac,"is",myresult[0])
    main()

def dispacc():
    ac=int(input("Enter Account No:"))
    pin=int(input("Enter account pin.no:"))
    a="select*from account where acno=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(a,data)
    myresult=c.fetchonel()
    for i in myresult:
        print(i,end=" ")
    main()

def closeacc():
    ac=input("Enter Account No:")
    pin=int(input("Enter account pin.no:"))
    sql1="delete from acccount where acno=%s"
    sql2="delete from acccount where acno=%s"
    data=(ac,)
    c=mydb.cursor()
    c.execute(sql1,data)
    c.execute(sql2,data)
    mydb.commit()
    main()

def main():
    print("""
    1.OPEN NEW ACCOUNT
    2.DEPOSITE AMOUNT
    3.WITHDRAW AMOUNT
    4.BALANCE ENQUIRY
    5.DISPLAY CUSTOMER DETAILS
    6.CLOSEAN ACCOUNT
    """)
    choice=input("Enter Task No:")
    if(choice=='1'):
        OpenAccount()
    elif(choice=='2'):
        Deposite()
    elif(choice=='3'):
        withdraw()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        dispacc()
    elif(choice=='6'):
        closeacc()
    else:
        print("wrong choice.....")
        main()
main()
