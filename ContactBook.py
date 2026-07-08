import json

class ContactListMethod:

    def __init__(self) -> None:
        
        try:
            with open("contactBase.json") as Contactjson:
                self.CONTACT = json.load(Contactjson)
        except FileNotFoundError:
            self.CONTACT = []
            print("Creating A File")



    def addContact(self)  -> None:
        self.CONTACT.append({"Name": input("Name: "), "Phone" : int(input("Phone: ")), "Email" : input("Email: ")})
        with open("contactBase.json", "w") as contactAdd:
            json.dump(self.CONTACT, contactAdd, indent=4)

    def SearchCon(self)  -> None:  
        Search = input("Search Name: ")

        for contact in self.CONTACT:
            if contact["Name"] == Search:
                print(contact)
            else:
                print("No Contact")
    
    def SearchALL(self)  -> None:
        with open("contactBase.json") as searchall:
            all = json.load(searchall)
            for llsearch in all:
                print(llsearch)
    
    def DeleteCon(self)  -> None:
        Search = input("Search Name: ")

        for contact in self.CONTACT:
            if contact["Name"] == Search:
                self.CONTACT.remove(contact)
                with open("contactBase.json", "w") as deletejson:
                    json.dump(self.CONTACT, deletejson)
                    print("Contact Succefully Deleted!!")

MyList = ContactListMethod()
while True:


    print("==================================================")
    print("===========      CONTACT BOOK       ==============")
    print("==================================================")

    print("==================================================")
    print("===========   1. Add Contact        ==============")
    print("===========   2. Search Contact     ==============")
    print("===========   3. Show all Contact   ==============")
    print("===========   4. Delete  A Contact  ==============")
    print("==================================================")

    choice1 = int(input("Select: "))

    match choice1:
        case 1:
            MyList.addContact()
        case 2:
            MyList.SearchCon()
        case 3:
            MyList.SearchALL()
        case 4:
            MyList.DeleteCon()
        case _:
            print("!!ERROR!!")