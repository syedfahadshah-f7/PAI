class BankAccount:            
    def __init__(self,accountNum, balance, openingDate, customerName ) -> None:
        self.AC = accountNum
        self.Balance = balance
        self.ODate = openingDate
        self.CustomerName = customerName
        
    def Deposit(self, amnt):
        self.Balance += amnt
    def WithDraw(self,amnt):
        if amnt > self.Balance :
            print("Not Enough Money to With draw")
        else:
            self.Balance -= amnt
    
    def Check_Balance(self):
        print(f"Account NO: {self.AC}  Balance : {self.Balance}")
        
        
B1 = BankAccount(12345,10000,"11-9-2024","FAHAD")
B1.Deposit(40000)
print("Balance After Deposit : ")
B1.Check_Balance()
print("Balance After WithDraw : ")
B1.WithDraw(20000)
B1.Check_Balance()
    
    
    