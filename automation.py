import filecmp
import re

#Define gloal variables
found_contacts = []
text = ""

def get_data():
    file="potential-contacts.txt"
    
    #Define pattern
    num_pattern = re.compile(r"\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
    email_pattern = '\S+@\S+'
    unique = []

    #Extract phone numbers
    with open(file) as file:
        text = file.read().rstrip()
        found_contacts = re.findall(num_pattern, text)
    
    file.close()


    res = [] # Used for trcking numbers

    dest = open("phone_numbers.txt","a")
    for number in found_contacts:

        #Reformat the number
        number = re.sub(r"[^a-zA-Z0-9]","",number)
        formatted_number = '-'.join([number[:3], number[4:6], number[6:10]])
        print(number, formatted_number)
        
        #Write to destination file
        if number not in res:
            dest.writelines(str(f'{formatted_number}\n'))
            res.append(number)
            
    dest.close()

    #Write to destination file
    emails = [] 

  #Change destination
    dest = open("emails.txt","a") # change file destionation
    with open("potential-contacts.txt") as file:
     emails = re.findall(email_pattern, text)
    for email in emails:
        if email not in res:
            dest.writelines(str(f'{email}\n'))
            res.append(email)
    dest.close()
get_data()