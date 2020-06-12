passw = input("What is your password?\n")
passwords = {}

def main():
    print("\nWELCOME TO YOUR SAFE!")
    print("********CHOICES********")
    print(":sp --> Store Password ")
    print(":q --> Quit            ")
    print(":vps --> View Passwords")
    print(":gp --> Get Password   ")
    print("***********************")

    choice = input("What would you like to do today? \n:")
    if choice == "q":
        with open('/Users/sathwikdoddi/Documents/Python/Passwords/safe.py', 'r') as oldboy, open('/Users/sathwikdoddi/Documents/Python/Passwords/safe2.py', 'w') as new:
            old = oldboy.readlines()
            old[1] = f'passwords = {passwords}\n'

            new.writelines(old)
        exit()
    elif choice == "sp":
        service = input("What is the name of your service?\n")
        password = input("What is the password for this service?\n")
        passwords.update({service:password})
        main()
    elif choice == "gp":
        service = input("What is the name of your service?\n")
        print(f'The password for the service {service} is {passwords[service]}')
        main()
    elif choice == "vps":
        for item in passwords:
            print(f'{item}\n')
        main()
    else:
        print("Invalid Choice")
        main()


if passw == "sathwikdoddi":
    main()
else:
    exit()