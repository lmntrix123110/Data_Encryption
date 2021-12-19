def Signup():
    f = open("password.txt", "a")
    f = open("password.txt", "r")

    Username= input("Create Username: ")
    Password1= input("Create Password: ")
    Password2= input("Reenter Password: ")

    u=[]
    p=[]
    for i in f:
        a,b= i.split(", ")
        b= b.strip()
        u.append(a)
        p.append(b)
    data= dict(zip(u, p))

    if(Password1!=Password2):
        print("Password don't match, reenter")
        Signup()
    else:
        if(len(Password1)<=6):
            print("Password too short, reenter")
            Signup()
        elif Username in u:
            print("Username Exists, reenter")
            Signup()
        else:
            f= open("password.txt", "a")
            f.write(Username+", "+Password1+"\n")
            print("Signup successful!")

            f = open("data.txt", "a")
            f.write(str(Username) + " ")

            a = str(input("College Fee(47000/45000): "))
            f.write(str(a) + " ")

            a = str(input("Semister(in number): "))
            f.write(str(a) + " ")

            a = str(input("Hostel Fee(amount/nil): "))
            f.write(str(a) + " ")

            a = str(input("Bus pass status(yes/no): "))
            f.write(str(a) + " ")
            f.write("\n")

def Login():
    f= open("password.txt", "r")

    Username = input("Enter Username: ")
    Password1 = input("Enter Password: ")

    if not len(Username or Password1)<1:
        u = []
        p = []
        for i in f:
            a, b = i.split(", ")
            b = b.strip()
            u.append(a)
            p.append(b)
        data = dict(zip(u, p))
        if not Username in data:
            print("Username or Password incorrect, reenter")
            Login()
        else:
            if Password1 == data[Username]:
                print("Login successful!")
                print("Hi", Username)

                f1 = open("data.txt", "r")
                print("Name|College Fee|Semister|Hostel Fee|Bus Fee Status\n")
                cont = f1.readlines()
                n = len(cont)
                i = 0
                for i in range(0, n):
                    a = cont[i]
                    h = a.split(" ")
                    if (Username == h[0]):
                        print(cont[i])

            else:
                print("Username or Password incorrect, reenter")
                Login()
    else:
        print("Login Error!, reenter")
        Login()

def base():
    n=1
    while(n!=3):
        print("1.Login\n2.Signup\n3.Exit")
        n = int(input("Choose from above: "))
        if(n==1):
            Login()
        if(n==2):
            Signup()

base()
