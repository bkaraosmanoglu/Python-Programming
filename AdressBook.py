PhoneNumber=[]
Names=[]
Emails=[]
option =0
while True:
    print("---------------------------------------")
    option = input("Enter the number of the Option you want:"+
                "\n----------------------------------------"+
                "\n| 1 | To Add Contact"+
               "\n| 2 | To search for the Contact by the Name\n| 3 | To search the Contact by the Phone Number"+
               "\n| 4 | To Edit the Contact\n| 5 | To delete the Contact\n| 6 | To print the Address book\n| 7 | To quit\n"+
                "----------------------------------------\n>")

    if option == "1":
        print("-------------")
        print("Add Contacts!\n-------------")
        name = input("Enter name :")
        Names.append(name)
        number = input("Enter number :")
        PhoneNumber.append(number)
        mail = input("Enter email :")
        Emails.append(mail)
     
    elif option == "2":
        print("\nSearch Contact by the Name\n--------------------")
     
        name = input("Enter the name :")
        if name in Names:
            print("The Contact are listed Below")
            print("-----------------------------")
            index = Names.index(name)
            print("Name   :", Names[index])
            print("Number : ", PhoneNumber[index])
            print("Email :", Emails[index])
         
         
        elif name not in Names:
            print("\nThis Contact Does Not Exist!!\n----------------------\n")
         
    elif option == "3":
        print("\nSearch Contact by the Number\n----------------------------")
        number = input("Enter the number :")
        if number in PhoneNumber:
            print("\n---------------------------")
            print("The Contact are listed Below")
            index = PhoneNumber.index(number)
            print("\nThe Number : ", PhoneNumber[index])
            print("Belongs to :", Names[index])
            print ("Belongs to :", Emails[index])
            print ("----------------------------")

        elif number not in PhoneNumber:
            print ("\nThis Contact Does Not Exist!!\n-------------------\n")
 
    elif option == "4":
        print ("\nEdit the Contact!\n------------------\n")

        name = input("Enter Contact Name to Edit:\n->")
        if name not in Names:
            print ("\nThis Name Does not exist!\n")
         
        elif name in Names:
            index = Names.index(name)
            Names.remove(name)
            del PhoneNumber[index]
            del Emails[index]

     
            print ("--------------------")
            print ("Entering New Contact\n------------------\n")
            name = input("Enter New Name :")
            Names.append(name)
            number =input("Enter New Number :")
            PhoneNumber.append(number)
            mail = input("Enter New Email :")
            Emails.append(mail)
            print ("\n----------------")
            print ("Contact Added!!\n--------------\n")
            
    elif option =="5":
        print("\nDelete the Contact!\n------------------\n")
        
        name = input("Enter the Contact Name to Delete:\n->")
        if name not in Names:
            print ("\nThis Name Does not exist!\n")
         
        elif name in Names:
            index = Names.index(name)
            Names.remove(name)
            del PhoneNumber[index]
            del Emails[index]
            print ("Deletion Succesfully !")
     
    elif option =="6":
        print ("----------------------------")
        print ("Printing the Address book\n-----------------------")

        for i in range(len(Names)):
            print (str(Names[i]) + "........"+ str(PhoneNumber[i]) + "........" + str(Emails[i]))
        print ("--------------------")
    elif option == "7":
        print ("Bye")
        break