
import json
import random
import string
from pathlib import Path







class Bank:

    database='data.json'
    data=[]


    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read())

        else:
            print("no such file exists")

    except Exception as err:
        print(f"an exception occured as {err}")   

    @staticmethod
    def update():
        with open(Bank.database,'w')  as fs:
            fs.write(json.dumps(Bank.data)) 

    @classmethod
    def __accountgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        num=random.choices(string.digits,k=3)
        spchar=random.choices("!@#$%^&*",k=1)
        id=alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    
    def Createaccount(self):
        info={
            "name":input("Tell Your Name:-"),
            "age":int(input("Tell your age:-")),
            "email-id":input("Tell your email id:-"),
            "pin":int(input("Tell your 4-number pin:-")),
            "AccountNumber":Bank.__accountgenerate(),
            "balance":0
        }

        if info['age']<18 or len(str(info['pin']))!=4:
            print("Sorry you cannot create your account")
        else:
            print("Account has been created successfully")   
            for i in info:
                print(f"{i}:{info[i]}")
            print("Please note down your account number") 

            Bank.data.append(info)  

            Bank.update()  



    def depositedmoney(self):
        accnumber=input("please tell your account number:")
        pin=int(input("Please tell your pin as well"))     

        userdata=[i for i in Bank.data if i['AccountNumber']==accnumber and i['pin']==pin]

        if userdata==False:
            print("sorry no data found")

        else:
            amount=int(input("how much you want to deposit it:-"))
            if amount>10000 or amount<0:
                print("Sorry this amount is above its 0 and below 10000")
            else:
                print(userdata)
                userdata[0]['balance']+=amount

                Bank.update()
                print("amount deposited succesfully")         


    def Withdrawmoney(self):
        accnumber=input("please tell your account number:")
        pin=int(input("Please tell your pin as well"))     

        userdata=[i for i in Bank.data if i['AccountNumber']==accnumber and i['pin']==pin]

        if userdata==False:
            print("sorry no data found")

        else:
            amount=int(input("how much you want to withdraw it:-"))
            if userdata[0]['balance'] <amount:
                print("Sorry this amount is nit sufficient it")
            else:
                print(userdata)
                userdata[0]['balance']-=amount

                Bank.update()
                print("amount withdraw succesfully")         


    def showdetails(self):
        accnumber=input("please tell your account number:")
        pin=int(input("Please tell your pin as well"))

        userdata=[i for i in Bank.data if i['AccountNumber']==accnumber and i['pin']==pin]

        print("your information are \n\n")

        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber=input("please tell your account number:")
        pin=int(input("Please tell your pin as well"))

        userdata=[i for i in Bank.data if i['AccountNumber']==accnumber and i['pin']==pin]

        if userdata ==False:
            print("no such user found it")

        else:
            print("you cannot change your age, accountnumber, balance")

            print("Fill the details for change or leave it empty no change")

            newdata={
                "name":input("please tell your new name or press enter "),
                "email-id": input("Please tell your new email or press enter to skip"),
                "pin":input("Please enter a new pin or press enter to skip it ")
            }

            if newdata["name"]=="" :
                newdata["name"]=userdata[0]['name']

            if newdata["email-id"]=="" :
                newdata["email-id"]=userdata[0]['email-id']

            if newdata["pin"]=="" :
                newdata["pin"]=userdata[0]['pin']    

            newdata['age']=userdata[0]['age']
            newdata['AccountNumber']=userdata[0]['AccountNumber']
            newdata['balance']=userdata[0]['balance']

            if type(newdata['pin'])==str:
                newdata['pin']=int(newdata['pin'])

            for i in newdata:
                if newdata[i]==userdata[0][i]:
                    continue
                else:
                    userdata[0][i]=newdata[i]

            Bank.update()
            print("details updated successfully")

            


    def deletdeatils(self):
        accnumber=input("please tell your account number:")
        pin=int(input("Please tell your pin as well"))

        userdata=[i for i in Bank.data if i['AccountNumber']==accnumber and i['pin']==pin]
    
        if userdata==False:
            print("Sorry data will not be existed")

        else:
            check =input("press y if you actually want to delete the accouunt or press n:-")
            if check=='n' or check=='N':
                print("passed")
            else:
                index=Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted Successfully")

                Bank.update()



user=Bank()



print("Press 1 for Creating an Account")
print("Press 2 for Deposit the Money")
print("Press 3 for Withdraw the Money")
print("Press 4 for Details")
print("Press 5 for Updating the details")
print("Press 6 for deleting the Account")


check=int(input("Tell your response:-"))

if check==1:
    user.Createaccount()


if check==2:
    user.depositedmoney()

if check==3:
    user.Withdrawmoney()

if check==4:
    user.showdetails()


if check==5:
    user.updatedetails()


if check==6:
    user.deletdeatils()

