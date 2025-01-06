from kivymd.uix.screenmanager import ScreenManager


def change_screen(obj, screen_name, btn=None):
    # ! We have to get to the MainScreen object to change the current screen
    if screen_name == "second":
        obj.parent.parent.parent.parent.manager.current = screen_name
    elif screen_name == "edit_spending_screen" or screen_name == "edit_income_screen":
        obj.parent.parent.parent.parent.parent.parent.parent.parent.manager.current = (
            screen_name
        )
        with open("btn_ID.txt", "w") as file:
            file.write(obj.id.strip("btn"))
    # TODO Button error Maybe temporary files solution
    else:
        obj.parent.parent.parent.parent.parent.manager.current = screen_name
