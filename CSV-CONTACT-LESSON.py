import csv

def main():
    print("This program creates a CSV file, allows you to modify it, and then displays the contents of the file.")
    print("1 - Create a new CSV file. This will overwrite any existing file.")
    print("2 - Add new contacts")
    print("3 - View all contacts")
    print("4 - Modify an existing contact")
    print("5 - Save and exit")
    if __name__ == "__main__":
        while True:
            choice = input("Enter your choice (1-5): ")
            if choice == "1":
                create_csv()
            elif choice == "2":
                add_contacts()
            elif choice == "3":
                view_contacts()
            elif choice == "4":
                modify_contact()
            elif choice == "5":
                print("Exiting the program.")
                print("Completed by, Gregary Coplan")
                break
            else:
                print("Invalid choice. Please try again.")

def create_csv():    
    with open("contacts.csv", "w", newline="") as csvfile:
        contacts = csv.writer(csvfile)
        contacts.writerow(["Name", "Phone", "Email"])
        print("File has been created successfully.")

def add_contacts():
    with open("contacts.csv", "a", newline="") as csvfile:
        while True:
            contacts = csv.writer(csvfile)
            name = input("Enter a name (or 'done' to finish): ")
            if name.lower() == 'done':
                print("Finished adding contacts.")
                break
            phone = input("Enter a phone number: ")
            email = input("Enter an email address: ")
            contacts.writerow([name, phone, email])
            print(f"Contact added: {name}, {phone}, {email}")
        

def view_contacts():       
    with open("contacts.csv", "r") as csvfile:
        contacts = csv.reader(csvfile)
        for row in contacts:
            print(f"{row[0]:<20} {row[1]:<15} {row[2]}") #learned this while researching how to make it look better in the terminal, stack overflow my goat
#it basically lets you format the output, so that the columns are aligned, and the numbers in the phone column are aligned to the right based on the numbers you choose


#so, i was really struggling with modifying the contact, as you can tell from my email
#but i did watch a few video on how to do it, with nothing being directly copied.
#i honestly don't know if this is the best way to do it, since the channel was some crappy AI slop channel, but it worked for me.
#i also can't completely remember if we learned about enumerating in class, but in case not, enumerating lets you loop through
#a list and get the index of the item, which is useful for modifying specific item in the list
#i also learned that you can use the else statement with a for loop, which is useful for checking if the item was found or not
#since i don't really use else statements as much as i do elifs with specific scenarios. 
#if you need me to explain any more about the code, please email me, and i can try to explain it better,
#sorry for the word dump

def modify_contact():
    with open("contacts.csv", "r") as csvfile:
        contacts = csv.reader(csvfile)
        for row in contacts:
            print(f"{row[0]:<20} {row[1]:<15} {row[2]}") #directly copied from above
        print("Enter the name of the contact you want to modify:")
        name_to_modify = input()
        with open("contacts.csv", "r") as csvfile:
            contacts = list(csv.reader(csvfile))
            for i, row in enumerate(contacts):
                if row[0] == name_to_modify:
                    print(f"Current details: {row[0]}, {row[1]}, {row[2]}")
                    new_name = input("Enter new name (or press enter to keep current): ")
                    new_phone = input("Enter new phone number (or press enter to keep current): ")
                    new_email = input("Enter new email address (or press enter to keep current): ")
                    if new_name:
                        contacts[i][0] = new_name
                    if new_phone:
                        contacts[i][1] = new_phone
                    if new_email:
                        contacts[i][2] = new_email
                    print(f"Contact updated: {contacts[i][0]}, {contacts[i][1]}, {contacts[i][2]}")
                    break
            else:
                print("Contact not found.")     
        with open("contacts.csv", "w", newline="") as csvfile:
            contacts_writer = csv.writer(csvfile)
            contacts_writer.writerows(contacts)
            print("Changes saved successfully.")        


if __name__ == "__main__":
    main()            