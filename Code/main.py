import extention.login as L
import extention.home_page as hp

def main():
    print("main() currently running...")

    try:
        L.login()
    except Exception as e:
        print("erro 01\n" +str(e))
        return
    else:
        print("login successfull!")
        hp()


    print("main() terminated...")

main()

# last line