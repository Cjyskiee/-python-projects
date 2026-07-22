
import datetime
import sqlite3




class ExpenseMethods:
    
    def __init__(self) -> None:
        self.currentWeek = datetime.date.today().isocalendar().week
        

        self.conn = sqlite3.connect("expense.db")
        self.cur = self.conn.cursor()

        self.conn.execute(""" CREATE TABLE IF NOT EXISTS expenses(
                   id INTEGER PRIMARY KEY,
                   item TEXT,
                   amount REAL,
                   date TEXT
                   )""" )
        
        self.conn.execute("""CREATE TABLE IF NOT EXISTS budget (
                   id INTEGER PRIMARY KEY,
                   amount REAL,
                   week INTEGER
                   ) """)
        
        self.cur.execute("SELECT week FROM budget WHERE week = ?", (self.currentWeek,))
        result = self.cur.fetchone()

            
        if result is None:
            self.cur.execute("DELETE FROM expenses")
            self.conn.commit()

        
        self.conn.commit()

    def setBudget(self) -> None:
        print(f"- {self.currentWeek} | {datetime.date.today().strftime("%A")} -")
        print("------ Set Your Budget ------")
        print("-----------------------------")
        
        Budget = float(input("Budget: "))
        if Budget < 0:
            print("You cannot Put negative Numbers:")
            Budget = 0.0
        else:
            self.conn.execute("INSERT INTO budget (amount, week) VALUES (?, ?)", (Budget, self.currentWeek))
        
        self.conn.commit()
    
    def TransFunc(self) -> None:    

        self.cur.execute("SELECT SUM(amount) FROM budget WHERE week = ?", (self.currentWeek,))
        originalBudget = self.cur.fetchone()

        if originalBudget[0] is None:
            print("No Budget!!\n Put Budget First!!")
            return
        
        self.cur.execute("SELECT SUM(amount) FROM expenses WHERE date = ?", (datetime.date.today().strftime("%c"),))
        totalSpent = self.cur.fetchone()

        remaining = originalBudget[0] - (totalSpent[0] or 0)
        
        print(f"- {self.currentWeek} | {datetime.date.today().strftime("%A")} -")
        item = input("Item: ")      
        bill = float(input("Bill: "))
        if bill > remaining:
            print("The amount exceeds the remaining Budget!!")
        else:  
            self.conn.execute("INSERT INTO expenses (item, amount, date) VALUES (?, ?, ?)", (item, bill, datetime.date.today().strftime("%c")))
        
        self.conn.commit()
        
    def SeeTrans(self) -> None:
        self.cur.execute("SELECT * FROM expenses")
        transaction = self.cur.fetchall()

        if len(transaction) == 0:
            print("No Transaction to see yet!")
        else:
            print(f"- {self.currentWeek} | {datetime.date.today().strftime("%A")} -")
            for row in transaction:
                print(f"Item: {row[1]} | Amount: ₱{row[2]:.2f} | Date: {row[3]}")

        self.conn.commit()

    def OverExpense(self) -> None:
        self.cur.execute("SELECT SUM(amount) FROM budget WHERE week = ?", (self.currentWeek,))
        originalBudget = self.cur.fetchone()

        self.cur.execute("SELECT SUM(amount) FROM expenses WHERE date = ?", (datetime.date.today().strftime("%c"),))
        totalSpent = self.cur.fetchone()


        remaining = originalBudget[0] - (totalSpent[0] or 0)

        print(f"- {self.currentWeek} | {datetime.date.today().strftime("%A")} -")
        print(f"Total Amount Spent: ₱{totalSpent[0] or 0:.2f}")
        print(f"Total Budget: ₱{originalBudget[0] or 0:.2f}")
        print(f"Budget left: ₱{remaining:.2f}")

        self.conn.commit()


            
            
            

ClassCall = ExpenseMethods()

while True:




    print("----------------------------------------------------")
    print("---------------   EXPENSE TRACKER    ---------------")
    print("------------------------------------------------------")
    print("---------------  1. Add Budget         ---------------")
    print("---------------  2. Transaction        ---------------")
    print("---------------  3. See Transaction    ---------------")
    print("---------------  4. See All Expenses   ---------------")
    print("---------------  5. Exit               ---------------")

    choice = int(input("CHOOSE 1-4: "))

    match choice:
        case 1:
            ClassCall.setBudget()
        case 2:
            ClassCall.TransFunc()
        case 3:
            ClassCall.SeeTrans()
        case 4:
            ClassCall.OverExpense()
        case 5:
            ClassCall.conn.close()
            exit()
        case _:
            print("Invalid Choice!!")
            
            

