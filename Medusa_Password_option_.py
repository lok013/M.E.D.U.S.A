import secrets
import string
import pyttsx3

class SpeechAccess:
    def __init__(self):
        self.speaks = pyttsx3.init()

    def speak_logic(self, text):
        voices = self.speaks.getProperty('voices')
        if len(voices) > 1:
            self.speaks.setProperty('voice', voices[1].id)
        self.speaks.say(text)
        self.speaks.runAndWait()


class Main:
    def __init__(self):
        self.speech_access = SpeechAccess()

    def generate_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    def main(self):
        while True:
            user_input = input("Enter the type of payload (password, injection) or 'exit' to quit: ").strip().lower()
            
            if user_input == 'exit':
                message = ("Exiting...")
                print(message)
                self.speech_access.speak_logic(message)
                break
            
            elif user_input == 'password':
                password_length_str = input("Enter the length of the password: ").strip()

                if not password_length_str.isdigit():
                    print("Invalid input. Please enter a valid integer.")
                    continue
                password_length = int(password_length_str)

                if password_length <= 0:
                    print("Password length must be greater than 0.")
                    continue
                
                password = self.generate_password(password_length)
                message = f'Your generated password is: {password}'
                print(message)
                self.speech_access.speak_logic(message)
            
            elif user_input == 'injection':
                message = "Injection payload generated."
                injections = "' OR '1'='1'; --"
                print(message)
                print(injections)
                self.speech_access.speak_logic(message)

            else:
                print("Invalid option. Please enter 'password', 'injection', or 'exit'.")
                continue

if __name__ == "__main__":
    Main().main()
