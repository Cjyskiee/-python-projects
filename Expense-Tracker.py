import json
import datetime


class ExpenseMethods:
    
    def __init__(self) -> None:
        
        
        try:
            with open("ExpenseBase.json") as Expensejson:
                self.Data = json.load(Expensejson) 

                currentWeek = datetime.date.today().isocalendar().week
                if self.Data.get("Week", None) != currentWeek:
                    self.Data["Transaction"] = []
                    self.Data["Week"] = currentWeek
                    with open("ExpenseBase.json", "w") as Timejson:
                        json.dump(self.Data, Timejson, indent=4)

        except (FileNotFoundError,json.JSONDecodeError):
            self.Data = {"Budget" : 0.0, "Transaction" : [], "Week" : datetime.date.today().isocalendar().week}
            print("Creating A File")

    def setBudget(self) -> None:
        print(f"- {self.Data["Week"]} | {datetime.date.today().strftime("%A")} -")
        print("------ Set Your Budget ------")
        print("-----------------------------")

        self.Data["Budget"] = float(input("Budget: "))
        if self.Data["Budget"] < 0:
            print("You cannot Put negative Numbers:")
            self.Data["Budget"] = 0.0
        else:
            with open("ExpenseBase.json", "w") as BudgetBase:
                json.dump(self.Data, BudgetBase, indent=4)

    
    def TransFunc(self) -> None:
        if self.Data["Budget"] == 0:
            print("No Budget!!\n Put Budget First!!")
        else:
            print(f"- {self.Data["Week"]} | {datetime.date.today().strftime("%A")} -")
            item = input("Item: ")      
            bill = float(input("Bill: "))
            if bill > self.Data["Budget"]:
                print("The amount exceeds the remaining Budget!!")
            else:  
                self.Data["Transaction"].append({"Item": item, "Bill": bill})
                self.Data["Budget"] -= bill
                with open("ExpenseBase.json", "w") as TransBase:
                    json.dump(self.Data, TransBase, indent=4)        
        
    def SeeTrans(self) -> None:
        if self.Data["Transaction"] == []:
            print("No Transaction to see yet!")
        else:
            print(f"- {self.Data["Week"]} | {datetime.date.today().strftime("%A")} -")
            for item  in self.Data["Transaction"]:
                print(f"Item: {item['Item']} | Bill: ₱{item['Bill']:.2f}")
    
    def OverExpense(self) -> None:
        total = 0
        PlusTotal = 0

        for overBills in self.Data["Transaction"]:
            total = total + overBills["Bill"]
        PlusTotal = total + self.Data["Budget"]

        print(f"- {self.Data["Week"]} | {datetime.date.today().strftime("%A")} -")
        print(f"Total Amount Spent: ₱{total:.2f}")
        print(f"Total Budget: ₱{PlusTotal:.2f}")
        print(f"Budget left: ₱{self.Data["Budget"]:.2f}")



            
            
            

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
            exit()
        case _:
            print("Invalid Choice!!")