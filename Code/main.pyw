import UI.login as login

def main():
    try:
        login.avvio()  # Avvia server Flask + finestra con PyWebview
    except Exception as e:
        print("Error 01 - Contact assistance \n" + str(e))
    else:
        print("Login request sent correctly! ^^")

if __name__ == "__main__":
    main()
