from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key" , 'wb') as key_file:
    key_file.write(key)
    


def load_key():
    with open("key.key" , 'rb') as key_file:
        key = key_file.read()
        return Fernet(key)
        
fernet = load_key()



def view():
    try:
        with open('pass_store.txt', 'r') as f:
            for line in f.readlines():
                data = line.rstrip()
                user, pwd = data.split("||")
                
                decrypt_pass = fernet.decrypt(pwd.encode()).decode()
                
                
                print("Username: " + user)
                print("Password: " + decrypt_pass)
    except:
        print("Currently there is no username ans password in file")

def add():
    user = input('User: ')
    password = input('Password: ')
    encrypted_pass = fernet.encrypt(password.encode()).decode()
    
    with open('pass_store.txt', 'a') as f:
        f.write(user + "||" + encrypted_pass + "\n")
    print("User added successfully!")


while True:
    check = input("Do you want to view existing passwords or use a new one? (view/add/exit): ").strip().lower()

    if check == 'view':
        view()
    elif check == 'add':
        add()
    elif check == 'exit':
        print("Exiting program.")
        break
    else:
        print("Please enter a valid option ('view', 'add', 'exit').")
