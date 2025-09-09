from pywinauto import Application, Desktop
import time


def find_available_icon_and_click(teams_window):
    for rb in teams_window.descendants(control_type="RadioButton"):
        if "Available" in rb.window_text():
            print(f" (3) Clicking Available status: {rb.window_text()}")
            rb.click_input()
            break


def find_status_button_and_click(teams_window):
    for item in teams_window.descendants(control_type="MenuItem"):
        if "change status" in item.window_text():
            print(f" (2) Clicking status option: {item.window_text()}")
            item.click_input()
            break


def find_teams_profile_status_button_and_click(teams_window):
    for btn in teams_window.descendants(control_type="Button"):
        if "Your profile, status" in btn.window_text():
            print(f" (1) Clicking Profile status button: {btn.window_text()}")
            btn.click_input()
            break


if __name__ == '__main__':
    print("[Log] Program start!!!")
    try:
        print("[Log] Trying to find Teams process..")

        Application(backend="uia").connect(path="Teams.exe")

        teams_window_spec = Desktop(backend="uia").window(title_re=".*Microsoft Teams")
        teams_window = teams_window_spec.wrapper_object()

        print("[Log] Found teams!")

        iteration = 1

        while True:
            print(f"[Log] Start to click the available Icon - iteration {iteration}")
            try:
                find_teams_profile_status_button_and_click(teams_window)
                time.sleep(0.5)  # delay for the subsequent elements appearing
                find_status_button_and_click(teams_window)
                time.sleep(0.5)
                find_available_icon_and_click(teams_window)
                time.sleep(0.5)
                find_teams_profile_status_button_and_click(teams_window)  # Initialize the screen
                time.sleep(0.5)
                time.sleep(10)  # Delay 10 secs
                iteration += 1
            except Exception as e:
                print(f"[Error] {e}")
                input("Press Enter to exit...")

    except Exception as e:
        print(f"[Error] {e}")
        input("Press Enter to exit...")

    input("Press Enter to exit...")
