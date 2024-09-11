class Restaurant:
    menu = []
    book_tables = {}
    order = {}
    
    def add_item_to_menu(self,item):
        self.menu.append(item)
        
    def booked_tables(self,TableNum):
        if book_tables["Table " + str(TableNum)] == "booked" :
            print("Table is already booked !!")
        else:
            self.book_tables["Table " + str(TableNum)] = "booked"
        
    def customer_order(self,item,quantity):
        self.order[item] = quantity
        
    def Print_Menu(self):
        print(f"Menu : {self.menu}")
        
    def Print_Booked_table(self):
        print(f"Reserved Table : {self.book_tables}")
        
    def Print_Customer_Order(self):
        print(f"Order: {self.order}")
        
cus1 = Restaurant()
cus1.add_item_to_menu("Burger")
cus1.add_item_to_menu("Pizza")
cus1.add_item_to_menu("Shawarma")
cus1.add_item_to_menu("Biryani")
cus1.add_item_to_menu("Pilao")

cus1.booked_tables(2)
cus1.booked_tables(3)


cus1.customer_order("Pizza",2)
cus1.customer_order("Burgers",6)

cus1.Print_Menu()
cus1.Print_Booked_table()
cus1.Print_Customer_Order()
