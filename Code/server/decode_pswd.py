import hashlib

TARGET = "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f"

def hash_pswd(p: str) -> str:
    return hashlib.sha256(p.encode()).hexdigest()

def test(pwd: str):
    return hash_pswd(pwd) == TARGET


def start():
    i = input("test password hasing (1) or new password hash (2)? ")
    if i =="1":
        while True:
            p = input("Enter password to test: ")
            if test(p):
                #print("Password is correct!")
                break
            else:
                print("Incorrect password, try again.")
            if p.lower() == "exit":
                print("Exiting password tester.")
                break
    elif i == "2":
        p = input("Enter password to hash: ")
        #print(f"Hashed password: \n{hash_pswd(p)}")

start()

# Giovanna_Ameli