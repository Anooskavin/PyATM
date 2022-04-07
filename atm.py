class Bank:
    accNo = [101, 102, 103, 104, 105]
    accHolder = ["Suresh", "Ganesh", "Magesh", "Naresh", "Harish"]
    pinNo = [2343, 5432, 7854, 2345, 1907]
    accBalance = [25234, 34123, 26100, 80000, 103400]
    Amount = [2000,500,100]
    Denominations =[0,0,0]
    input_denominations = [0, 0, 0]
    def loadMoney(self):
        loadMoneyFile = open('loadMoneyFile.txt', 'w')
        loadMoneyFile.write("                    ATM                \n")
        loadMoneyFile.write("Denominations      Number         Value\n")
        for i in range(len(self.Denominations)):
            inp=int(input())
            self.Denominations[i]+=inp*self.Amount[i]
            self.input_denominations[i]+=inp
            loadMoneyFile.write(str(self.Amount[i])+"                "+str(self.input_denominations[i])+"            "+str(self.Denominations[i])+"\n")
        loadMoneyFile.close()
        for j in range(len(self.Denominations)):
            print("-------------", end="")
        print()
        print("| {:<8} | {:<5} | {:<10} ".format('Denominations', 'Number', 'Value'), end=" |\n")
        for i in range(len(self.Denominations)):
            for j in range(len(self.Denominations)):
                print("-------------", end="")
            print()
            print("| {:<13} | {:<5} | {:<10} ".format((self.Amount[i]),str(self.input_denominations[i]),str(self.Denominations[i])),sep="|",end=" |\n")
        for j in range(len(self.Denominations)):
            print("-------------", end="")

        # print(self.Amount,self.Denominations)

    def customerDetails(self):
        customerFile=open('customerFile.txt','w')
        customerFile.write("AccNo      AccHolder         PinNo       AccBalance\n")
        for i in range(len(self.accNo)):
            customerFile.write(str(self.accNo[i])+'        '+self.accHolder[i]+'            '+str(self.pinNo[i])+'          '+str(self.accBalance[i])+'\n')
        customerFile.close()
    def printCustomerDetails(self):
        for j in range(len(self.accNo)):
            print("-----------", end="")
        print()
        print("| {:<8} | {:<15} | {:<10} | {:<10}".format('AccNo', 'AccHolder', 'PinNo', 'AccBalance'),end=" |\n")
        for i in range(len(self.accNo)):
            for j in range(len(self.accNo)):
                print("-----------",end="")
            print()
            print("| {:<8} | {:<15} | {:<10} | {:<10}".format(self.accNo[i],self.accHolder[i],self.pinNo[i],self.accBalance[i]),sep="|",end=" |\n")
        for j in range(len(self.accNo)):
            print("-----------", end="")
        # self.accNo[0]=111
        self.customerDetails()

    def cashierTransactions(self, cashier_accno,cashier_pin):
        for j in range(len(self.accNo)):
            if(self.accNo[j]==cashier_accno and self.pinNo[j]==cashier_pin):
                return True
        return False



ATM=Bank()
# ATM.customerDetails()
while(1):
    print('\n 1.Load Cash to ATM\n 2.Show Costumer Details\n 3.Show ATM Operations\n 4.Exit')
    input_user=int(input())
    if(input_user==1):
        ATM.loadMoney()
    elif(input_user==2):
        ATM.printCustomerDetails()
    elif(input_user==3):
        while(1):
            print("Account Number :  ")
            cashier_accno=int(input())
            print("Pin Number :  ")
            cashier_pin=int(input())
            if(ATM.cashierTransactions(cashier_accno,cashier_pin)):
                print('\n 1.Check Balance\n 2.Withdraw Money\n 3.Transfer Money\n 4.Check ATM Balance\n 5.Exit')
                cashier_inp=int(input())
                if (cashier_inp == 1):
                    ATM.checkBalance(cashier_accno)
                elif (cashier_inp == 2):
                    print()
                elif (cashier_inp == 3):
                    print()
                elif (cashier_inp == 4):
                    print()
                elif (cashier_inp == 5):
                    break
                else:
                    print("INAVLID TRANSACTIONS")
            else:
                print("oo")

    elif(input_user==4):
        print("EXIT")
        break
    else:
        print("INAVLID OPTIONS")
# ATM.printDetails()
# fight a= new seats
#done by AKG
