#Banking Application
accountNo=0
CusName=" "
BCode =" "
Mobile=0
Bal =0
def createAccounts():
    accountNo = int(input("enter account number"))
    CusName = input("enter name")
    BCode = input("enter Branch Code")
    Mobile = int(input("enter Mobile Number"))
    global Bal
    Bal = int(input("enter current balance"))
    
def ShowAcntDetails():
    print("accountNo:",accountNo)
    print("customerName:",CusName)
    print("BCode:", BCode)
    print("Mobile:",Mobile)
    

def Deposit(amount):
    Bal = Bal+amount 
    chckbalance()

def Withdraw(amount):
    Bal = Bal - amount
    chckbalance()

def chckbalance():
    Bal = Bal
    print("current Balance:", Bal)

#_Main_#
ch1='y'
while(ch1=='y'):
     print("1.Create account\n  2.Withdraw \n 3.deposit \n 4.check balance")
     ch=int(input("select any option"))
     if (ch==1):
        createAccounts ()
     elif (ch==2): 
      amnt=int(input("enter amount to withdraw"))
      Withdraw(amnt)
     elif ch==3:
      amnt=int(input("enter amount to Deposit"))
     elif ch==4:
      chckbalance()
else:
        print ("please select any 4 options available above")
        print("do you want to continue...pres y")
        ch1=input()



