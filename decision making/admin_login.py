user=input()
password=input()
if user=="Admin":
    if password=="12345":
        print("Login Success")
    else:
        print("Invalid password")
else:
    print("Invalid username")