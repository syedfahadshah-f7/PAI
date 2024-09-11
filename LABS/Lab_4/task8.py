class Account:
    def setData(self,AC_Num, AC_Bal, Security_Code ) -> None:
        self.__AC_Num = AC_Num
        self.__AC_Bal = AC_Bal
        self.__Security_Code =Security_Code
        
    def PrintData(self):
        print(f"Account Num: {self.__AC_Num}  Account Balance: {self.__AC_Bal} Security Code: {self.__Security_Code}")
        
A1 = Account()
A1.setData(12345,50000,9999)
A1.PrintData()