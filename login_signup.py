print("Create Your Account:")

user_name = input("Enter Username: ")
password = input("Enter Your password: ")

print("Your Account has been created successfully")
print("Login Now: ")

user_name2 = input("Enter Your Username: ")
password2 = input("Enter Your password: ")

if user_name == user_name2 and password == password2:
    print("Logged in successfully.")
else:
    print("Invalid Credentials")

