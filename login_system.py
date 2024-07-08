import json

# fetch user details if already exist
def fetch():
    try:
        with open("login_details.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


print("Hello User")
print("1. Login")
print("2. Register")
choice = input("Enter your choice: ")
info = fetch()
match choice:
    case "1":
        flag = False
        user_name = input("Enter Your Username: ")
        user_password = input("Enter Your Password: ")
        for name in info:
            if user_name in name:
                flag = True
                if name[user_name] == user_password:
                    print("\n")
                    print("\"Login Successful\"")
                    print("\n")
                    print("Here are your detals\n")
                    print(f"username - {user_name}")
                    print(f"password - {len(user_password) * "*"}")
        if not flag:
            print("User Not Found")
            print("\"Please Register\"")
    case "2":
        user_name = input("Create A Username: ")
        user_password = input("Create A Password: ")
        validation_password = input("Confirm Your Password: ")
        if user_password == validation_password:
            info.append({user_name: user_password})
        else:
            print("Password Does Not Match")
            exit()
        with open("login_details.txt", "w") as file:
            json.dump(info, file)
        print("\"Registered Successfully\"")
    case _:
        print("Invalid Choice Please Try Again")

