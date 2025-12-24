import json
import os

FILE_NAME = "passwords.json"
def check_master_password():
    with open("master.txt", "r") as file:
        saved_password = file.read().strip()

    entered = input("enter master password: ")

    if entered != saved_password:
        print("wrong master password")
        exit()

# ---------------- LOAD PASSWORDS ----------------
def load_passwords():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# ---------------- SAVE PASSWORDS ----------------
def save_passwords(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ---------------- ADD PASSWORD ----------------
def add_password():
    website = input("enter website/app name: ")
    username = input("enter username: ")
    password = input("enter password: ")

    data = load_passwords()
    data[website] = {
        "username": username,
        "password": password
    }

    save_passwords(data)
    print("password saved successfully")

# ---------------- VIEW PASSWORDS ----------------
def view_passwords():
    data = load_passwords()
    if not data:
        print("📭 no passwords saved")
        return

    print("\n saved Passwords:")
    for site, creds in data.items():
        print(f"- {site} | {creds['username']} | {creds['password']}")

# ---------------- SEARCH PASSWORD ----------------
def search_password():
    website = input("enter website name to search: ")
    data = load_passwords()

    if website in data:
        creds = data[website]
        print(f"\n {website}")
        print(f"username: {creds['username']}")
        print(f"password: {creds['password']}")
    else:
        print("no password found")
def delete_password():
    website = input("enter website to delete: ")
    data = load_passwords()

    if website in data:
        del data[website]
        save_passwords(data)
        print("password deleted successfully")
    else:
        print("website not found")

def update_password():
    website = input("enter website to update: ")
    data = load_passwords()

    if website in data:
        username = input("enter new username: ")
        password = input("enter new password: ")

        data[website]["username"] = username
        data[website]["password"] = password

        save_passwords(data)
        print("password updated successfully")
    else:
        print("website not found")


# ---------------- MAIN MENU ----------------
def main():
    check_master_password()

    while True:
        print("\n PASSWORD MANAGER")
        print("1. add password")
        print("2. view passwords")
        print("3. search password")
        print("4. update password")
        print("5. delete password")
        print("6. exit")

        choice = input("choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            search_password()
        elif choice == "4":
            update_password()
        elif choice == "5":
            delete_password()
        elif choice == "6":
            print("exiting....")
            break
        else:
            print("invalid choice")



if __name__ == "__main__":
    main()
