import pickle
import os
import pathlib
class Account :
    accNo = 0
    name = &#39;&#39;
    deposit=0
    type = &#39;&#39;
   
    def createAccount(self):
        self.accNo= int(input(&quot;Enter the account no : &quot;))
        self.name = input(&quot;Enter the account holder name : &quot;)
        self.type = input(&quot;Ente the type of account [C/S] : &quot;)
        self.deposit = int(input(&quot;Enter The Initial amount(&gt;=500 for Saving
and &gt;=1000 for current&quot;))
        print(&quot;\n\n\nAccount Created&quot;)
   
    def showAccount(self):
        print(&quot;Account Number : &quot;,self.accNo)
        print(&quot;Account Holder Name : &quot;, self.name)
        print(&quot;Type of Account&quot;,self.type)
        print(&quot;Balance : &quot;,self.deposit)
   
    def modifyAccount(self):
        print(&quot;Account Number : &quot;,self.accNo)
        self.name = input(&quot;Modify Account Holder Name :&quot;)
        self.type = input(&quot;Modify type of Account :&quot;)
        self.deposit = int(input(&quot;Modify Balance :&quot;))
def depositAmount(self,amount):
        self.deposit += amount
   
    def withdrawAmount(self,amount):
        self.deposit -= amount
   
    def report(self):
        print(self.accNo, &quot; &quot;,self.name ,&quot; &quot;,self.type,&quot; &quot;, self.deposit)
   
    def getAccountNo(self):
        return self.accNo
    def getAcccountHolderName(self):
        return self.name
    def getAccountType(self):
        return self.type
    def getDeposit(self):
        return self.deposit
   
def intro():
    print(&quot;\t\t\t\t**********************&quot;)
    print(&quot;\t\t\t\tBANK MANAGEMENT SYSTEM&quot;)
    print(&quot;\t\t\t\t**********************&quot;)
    print(&quot;\t\t\t\tMade  By Harendra jangir:&quot;)
    print(&quot;\t\t\t\tPIET&quot;)
    input()

def writeAccount():
    account = Account()
    account.createAccount()
    writeAccountsFile(account)
def displayAll():
    file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        mylist = pickle.load(infile)
        for item in mylist :
            print(item.accNo,&quot; &quot;, item.name, &quot; &quot;,item.type, &quot; &quot;,item.deposit )
        infile.close()
    else :
        print(&quot;No records to display&quot;)
file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        mylist = pickle.load(infile)
        infile.close()
        found = False
        for item in mylist :
            if item.accNo == num :
                print(&quot;Your account Balance is = &quot;,item.deposit)
                found = True
    else :
        print(&quot;No records to Search&quot;)
    if not found :
        print(&quot;No existing record with this number&quot;)
def depositAndWithdraw(num1,num2):
    file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        mylist = pickle.load(infile)
        infile.close()
        os.remove(&#39;accounts.data&#39;)
        for item in mylist :
            if item.accNo == num1 :
                if num2 == 1 :
                    amount = int(input(&quot;Enter the amount to deposit : &quot;))
                    item.deposit += amount
                    print(&quot;Your account is updted&quot;)
                elif num2 == 2 :
                    amount = int(input(&quot;Enter the amount to withdraw : &quot;))
                    if amount &lt;= item.deposit :
                        item.deposit -=amount
                    else :
                        print(&quot;You cannot withdraw larger amount&quot;)
               
    else :
        print(&quot;No records to Search&quot;)
    outfile = open(&#39;newaccounts.data&#39;,&#39;wb&#39;)
    pickle.dump(mylist, outfile)
    outfile.close()
    os.rename(&#39;newaccounts.data&#39;, &#39;accounts.data&#39;)
   
def deleteAccount(num):
    file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        oldlist = pickle.load(infile)
infile.close()
        newlist = []
        for item in oldlist :
            if item.accNo != num :
                newlist.append(item)
        os.remove(&#39;accounts.data&#39;)
        outfile = open(&#39;newaccounts.data&#39;,&#39;wb&#39;)
        pickle.dump(newlist, outfile)
        outfile.close()
        os.rename(&#39;newaccounts.data&#39;, &#39;accounts.data&#39;)
     
def modifyAccount(num):
    file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        oldlist = pickle.load(infile)
        infile.close()
        os.remove(&#39;accounts.data&#39;)
        for item in oldlist :
            if item.accNo == num :
                item.name = input(&quot;Enter the account holder name : &quot;)
                item.type = input(&quot;Enter the account Type : &quot;)
                item.deposit = int(input(&quot;Enter the Amount : &quot;))
       
        outfile = open(&#39;newaccounts.data&#39;,&#39;wb&#39;)
        pickle.dump(oldlist, outfile)
        outfile.close()
        os.rename(&#39;newaccounts.data&#39;, &#39;accounts.data&#39;)
   
def writeAccountsFile(account) :
   
    file = pathlib.Path(&quot;accounts.data&quot;)
    if file.exists ():
        infile = open(&#39;accounts.data&#39;,&#39;rb&#39;)
        oldlist = pickle.load(infile)
        oldlist.append(account)
        infile.close()
        os.remove(&#39;accounts.data&#39;)
    else :
        oldlist = [account]
    outfile = open(&#39;newaccounts.data&#39;,&#39;wb&#39;)
    pickle.dump(oldlist, outfile)
    outfile.close()
    os.rename(&#39;newaccounts.data&#39;, &#39;accounts.data&#39;)
   
       
# start of the program
ch=&#39;&#39;
num=0
intro()
while ch != 8:
    #system(&quot;cls&quot;);
    print(&quot;\tMAIN MENU&quot;)
    print(&quot;\t1. NEW ACCOUNT&quot;)
    print(&quot;\t2. DEPOSIT AMOUNT&quot;)
    print(&quot;\t3. WITHDRAW AMOUNT&quot;)
    print(&quot;\t4. BALANCE ENQUIRY&quot;)
    print(&quot;\t5. ALL ACCOUNT HOLDER LIST&quot;)
    print(&quot;\t6. CLOSE AN ACCOUNT&quot;)
    print(&quot;\t7. MODIFY AN ACCOUNT&quot;)
    print(&quot;\t8. EXIT&quot;)
    print(&quot;\tSelect Your Option (1-8) &quot;)
    ch = input()
    #system(&quot;cls&quot;);
   
    if ch == &#39;1&#39;:
        writeAccount()
    elif ch ==&#39;2&#39;:
        num = int(input(&quot;\tEnter The account No. : &quot;))
        depositAndWithdraw(num, 1)
    elif ch == &#39;3&#39;:
        num = int(input(&quot;\tEnter The account No. : &quot;))
        depositAndWithdraw(num, 2)
    elif ch == &#39;4&#39;:
        num = int(input(&quot;\tEnter The account No. : &quot;))
        displaySp(num)
    elif ch == &#39;5&#39;:
        displayAll();
    elif ch == &#39;6&#39;:
        num =int(input(&quot;\tEnter The account No. : &quot;))
        deleteAccount(num)
    elif ch == &#39;7&#39;:
        num = int(input(&quot;\tEnter The account No. : &quot;))
        modifyAccount(num)
    elif ch == &#39;8&#39;:
        print(&quot;\tThanks for using bank managemnt system&quot;)
        break
    else :
        print(&quot;Invalid choice&quot;)
   
    ch = input(&quot;Enter your choice : &quot;)