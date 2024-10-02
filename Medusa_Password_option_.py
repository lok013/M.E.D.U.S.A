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
        elif len(voices) == 0:
            print("No available voices.")
            return  # Early exit if no voice is found
        self.speaks.say(text)
        self.speaks.runAndWait()

class Main:
    def __init__(self):
        self.speech_access = SpeechAccess()

    def generate_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    def validate_password_length(self, length_str):
        try:
            length = int(length_str)
            if length <= 0:
                raise ValueError("Length must be greater than 0.")
            return length
        except ValueError as e:
            print(f"Invalid input: {e}")
            return None

    def handle_password(self):
        password_length_str = input("Enter the length of the password: ").strip()
        password_length = self.validate_password_length(password_length_str)
        if password_length is not None:
            password = self.generate_password(password_length)
            message = f'Your generated password is: {password}'
            print(message)
            self.speech_access.speak_logic(message)

    def handle_injection(self):
        message = "Injection payload generated."
        injections = "' OR '1'='1'; --"
        print(message)
        print(injections)
        self.speech_access.speak_logic(message)

    def main(self):
        while True:
            user_input = input("Enter the type of payload (password, injection) or 'exit' to quit: ").strip().lower()
            
            if user_input == 'exit':
                message = ("Exiting...")
                print(message)
                self.speech_access.speak_logic(message)
                break
            
            elif user_input == 'password':
                self.handle_password()
            
            elif user_input == 'injection':
                self.handle_injection()

            else:
                print("Invalid option. Please enter 'password', 'injection', or 'exit'.")

if __name__ == "__main__":
    Main().main()
