import pyttsx3
import time  # Import time module for delays
import pyfiglet
# import sys
import subprocess
# import socket
from datetime import datetime
import getpass
# import yagmail


ascii_banner = pyfiglet.figlet_format("Alok Sharma")
print(ascii_banner)
'''
logo = """
##################
#░█▀█░█░░░█▀█░█░█#
#░█▀█░█░░░█░█░█▀▄#
#░▀░▀░▀▀▀░▀▀▀░▀░▀#
##################
""" 

Agar kabhi pasand aaya then i will use this 

print(logo) '''

admin_name = "admin"
admin_password = "admin"


class SpeechAccess:
    def __init__(self):
        self.speaks = pyttsx3.init()

    def speak_logic(self, text):
        voices = self.speaks.getProperty('voices')  # Changed speaks to self.speaks
        self.speaks.setProperty('voice', voices[1].id)
        self.speaks.say(text)
        self.speaks.runAndWait()


class Service:
    def __init__(self):
        self.says = SpeechAccess()

    def get_valid_name(self):
        while True:
            name = input("Enter your name: ").strip()
            if name.isalpha():
                return name
            print("Please enter a valid name without any numbers or special characters.")
            self.says.speak_logic("Please enter a valid name without any numbers or special characters.")

    def welcome(self):
        name = self.get_valid_name()
        welcome_message = f"Welcome {name} to the program."
        print(welcome_message)  # Print the welcome message
        self.says.speak_logic(welcome_message)  # Speak the welcome message

        return name

    def authenticate_user(self):
        """Authenticate the user with admin name and password."""
        # names = "Enter your admin name"
        # self.says.speak_logic(names)
        name = input("Enter your admin name: ")
        # passwords = "Enter your admin password"
        # self.says.speak_logic(passwords)
        password = getpass.getpass("Enter your admin password: ")
        if name == admin_name and password == admin_password:
            return True
        else:
            print("Invalid credentials. Access denied.")
            return False

    def option_choice(self, name):
        while True:
            service_1 = 'Please Select a service :'
            print("Select a service : ")
            self.says.speak_logic(service_1)
            print("1. Encrypt/Decrypt Files/Messages")
            print("2. Payload Creation")  # This part is done
            print("3. Malware Detection in Pictures")
            print("4. Port Scanner ")
            print("5. Keylogger")  # This part is done
            print("6. Exit")  # This part is done
            choice = input("Enter your choice: ")

            if choice == "1":
                if self.authenticate_user():
                    message_1 = f"{choice} Selected"
                    self.says.speak_logic(message_1)
                    print("Placeholder for Encrypt/Decrypt functionality.")
                    self.says.speak_logic("Placeholder for Encrypt and Decrypt functionality.")
                    subprocess.run(['python', r'Alok/Medusa_E_D_cryption_.py'])
                else:
                    print("Access Denied")

            elif choice == "2":
                message_1 = f"{choice} Selected"
                self.says.speak_logic(message_1)
                print("Placeholder for Payload Creation functionality.")
                self.says.speak_logic("Placeholder for Payload Creation functionality.")
                subprocess.run(['python', r'./Alok/Medusa_Password_option_.py'])

            elif choice == "3":
                if self.authenticate_user():
                    message_1 = f"{choice} Selected"
                    self.says.speak_logic(message_1)
                    print("Placeholder for Malware Detection functionality.")
                    self.says.speak_logic("Placeholder for Malware Detection functionality.")
                else:
                    print("Access Denied")

            elif choice == "4":
                if self.authenticate_user():
                    message_1 = f"{choice} Selected"
                    self.says.speak_logic(message_1)
                    print("Placeholder for Port Scanner functionality.")
                    self.says.speak_logic("Placeholder for Port Scanner functionality.")
                else:
                    print("Access Denied")

            elif choice == "5":
                if self.authenticate_user():
                    message_1 = f"{choice} Selected"
                    self.says.speak_logic(message_1)
                    print("Placeholder for Keylogger functionality.")
                    self.says.speak_logic("Placeholder for Keylogger functionality.")
                    subprocess.run(['python', r'./Alok/Medusa_Keylogger_.py'])
                else:
                    print("Access Denied")

            elif choice == "6":
                message_1 = f"{choice} Selected"
                self.says.speak_logic(message_1)
                exit_message = f"{name}, Thank you for using the program"
                print(exit_message)
                self.says.speak_logic(exit_message)
                break

            else:
                invalid_message = f"{name}, Please make a valid choice."
                print(invalid_message)
                self.says.speak_logic(invalid_message)


if __name__ == "__main__":
    service = Service()
    user_name = service.welcome()
    service.option_choice(user_name)
