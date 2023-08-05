import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

while True:
    username=input("Enter your Email Address : ")
    if pattern.search(username):
        pattern2 =re.compile(r"([A-Za-z0-9@$%^&*!/\|.]{8,})")
        password=input("Enter your password : ")
        if pattern2.search(password):
            print("your are logged in")
            break
        else:
            print("Passwrod is invalid")
    else:
        print("Email address is invalid.")
        

