
import re

def already_exists(email,filename):
    with open(filename, 'r+') as file:
        existing_emails = file.readlines() 
        if email + '\n' in existing_emails:
            return True

def suggest_alternate_mail(email, filename):
    username, domain = email.split('@')
    username = ''.join(filter(str.isalpha, username))
    count = 1  
    new_email = f"{username}{count}@{domain}"
    
    while already_exists(new_email, filename):
        count += 1
        new_email = f"{username}{count}@{domain}"
    return new_email

def valid_email(email):
    email_regex = ( r"^[a-zA-Z0-9._%+-]+" r"@[a-zA-Z0-9.-]+" r"\.[a-zA-Z]{2,}$")
    return re.match(email_regex, email) is not None

def store_email(email, filename):
    with open(filename, 'a+') as file:
        file.write(email + '\n')
        print(f"Email '{email}' is valid and has been stored.")
 
def create_storage_file(storage_file):
    with open(storage_file, 'w') as file:
        pass
    return storage_file

def prompt_user():
    email = input('Please enter an email address: ')
    return email

def add_more_emails():
    while True:
        more_emails_response = input('Do you want to enter any more emails? Y/N: ').strip().lower()
        if more_emails_response == 'n':
            print('Exiting the program')
            return False
        elif more_emails_response == 'y':
            return True  
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            
def main():
    storage_file = create_storage_file('emails.txt')

    while True:
        email = prompt_user()   
        if valid_email(email):
            if already_exists(email,storage_file):
                print(f"Email '{email}' is already in the file.")
                print(f"Please consider using an alternative such as: {suggest_alternate_mail(email,storage_file)}")
                continue
            else:
                store_email(email,storage_file)
        else:
            print("The email is not valid. Please try again!")
            continue
    
        if not add_more_emails():
            break

         
main() #start point of the program   


