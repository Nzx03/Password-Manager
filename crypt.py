from cryptography.fernet import Fernet

def load_key():
     file=open("key.key","rb")
     key=file.read()
     file.close()
     return key
         
        

def write_key():
    key=Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)



key=load_key()
fer=Fernet(key)

def view():
    try:

     with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            if "|" in data:
              user,passw=data.split("|")
              print("User:",user,"password",fer.decrypt(passw.encode()).decode())
    except FileNotFoundError:
        print("Error: passwords.txt not found.")



           

def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    with open('passwords.txt', 'a') as f:
        encrypted_pwd = fer.encrypt(pwd.encode()).decode()
        f.write(name + "|" + encrypted_pwd + "\n")


while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue