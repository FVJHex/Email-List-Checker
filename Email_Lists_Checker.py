import tkinter as tk
from tkinter import ttk
import os
from datetime import datetime


# region Functions
def lists_calc():
    calc_reset()

    old_list = (old_list_tb.get(1.0, "end").lower().split("\n"))
    new_list = (new_list_tb.get(1.0, "end").lower().split("\n"))

    if len(old_list) != 2 and len(new_list) != 2:
        for email in new_list:
            if email not in old_list:
                to_add.append(email)

        for email in old_list:
            if email not in new_list:
                to_remove.append(email)

        if len(to_add) != 0 and len(to_remove) != 0:
            lists_state_change()

            for email in to_add:
                add_list_tb.insert("end", f"{email}\n")

            for email in to_remove:
                remove_list_tb.insert("end", f"{email}\n")

            lists_state_change()

        if len(to_add) != 0 and len(to_add) != 0:
            save_bt["state"] = "normal"


def csv_save():
    for address in to_add:
        with open(f"{cwd}/Email_Addresses_To_Add_{dateformat}.csv", "a") as f:
            f.write(address)
            f.write('\n')

    for address in to_remove:
        with open(f"{cwd}/Email_Addresses_To_Remove_{dateformat}.csv", "a") as f:
            f.write(address)
            f.write('\n')


def reset_press():
    to_add.clear()
    to_remove.clear()
    lists_state_change()
    old_list_tb.delete(1.0, "end")
    new_list_tb.delete(1.0, "end")
    add_list_tb.delete(1.0, "end")
    remove_list_tb.delete(1.0, "end")
    lists_state_change()
    save_bt["state"] = "disabled"


def calc_reset():
    to_add.clear()
    to_remove.clear()
    lists_state_change()
    add_list_tb.delete(1.0, "end")
    remove_list_tb.delete(1.0, "end")
    lists_state_change()


def save_state_change():
    if save_bt["state"] == "disabled":
        save_bt["state"] = "normal"
    else:
        save_bt["state"] = "disabled"


def lists_state_change():
    if add_list_tb["state"] == "disabled":
        add_list_tb["state"] = "normal"
    else:
        add_list_tb["state"] = "disabled"

    if remove_list_tb["state"] == "disabled":
        remove_list_tb["state"] = "normal"
    else:
        remove_list_tb["state"] = "disabled"


# endregion

# region Root
root = tk.Tk()
root.title("Email Lists Checker: Created By FVJHex")
root.resizable(False, False)
root.configure(bg="black")
w = 1600
h = 900
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (w / 2)
y = (screen_height / 2) - (h / 2) - 35
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# endregion

# region Frames
lists_frame = tk.Frame(root, bg="black")

buttons_frame = tk.Frame(root, bg="black")
# endregion

# region Labels
old_list_label = ttk.Label(
    lists_frame,
    text="PASTE OLD EMAIL LIST BELOW",
    font=("Helvetica", 15, "underline"),
    foreground="white",
    background="black"
)

new_list_label = ttk.Label(
    lists_frame,
    text="PASTE NEW EMAIL LIST BELOW",
    font=("Helvetica", 15, "underline"),
    foreground="white",
    background="black"
)

add_list_label = ttk.Label(
    lists_frame,
    text="ADDED EMAILS",
    font=("Helvetica", 15, "underline"),
    foreground="green",
    background="black"

)

remove_list_label = ttk.Label(
    lists_frame,
    text="REMOVED EMAILS",
    font=("Helvetica", 15, "underline"),
    foreground="red",
    background="black"
)
# endregion

# region TextBoxes
old_list_tb = tk.Text(lists_frame, width=47, height=45)

new_list_tb = tk.Text(lists_frame, width=47, height=45)

add_list_tb = tk.Text(lists_frame, width=47, height=45)
add_list_tb["state"] = "disabled"

remove_list_tb = tk.Text(lists_frame, width=47, height=45)
remove_list_tb["state"] = "disabled"
# endregion

# region Buttons
run_bt = ttk.Button(
    buttons_frame,
    text="Run",
    command=lists_calc
)

save_bt = ttk.Button(
    buttons_frame,
    text="Save Results",
    command=csv_save
)
save_bt["state"] = "disabled"

reset_bt = ttk.Button(
    buttons_frame,
    text="Reset",
    command=reset_press
)
# endregion

# region Grid Settings
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)

lists_frame.grid(column=0, row=1)
buttons_frame.grid(column=0, row=2)

old_list_label.grid(column=0, row=0, pady=(0, 30))
new_list_label.grid(column=1, row=0, pady=(0, 30))
add_list_label.grid(column=2, row=0, pady=(0, 30))
remove_list_label.grid(column=3, row=0, pady=(0, 30))

old_list_tb.grid(column=0, row=1)
new_list_tb.grid(column=1, row=1)
add_list_tb.grid(column=2, row=1)
remove_list_tb.grid(column=3, row=1)

run_bt.grid(column=0, row=0, padx=50, pady=(0, 15))
save_bt.grid(column=1, row=0, padx=50, pady=(0, 15))
reset_bt.grid(column=2, row=0, padx=50, pady=(0, 15))
# endregion

# region Variables
to_add = []
to_remove = []
username = os.environ.get("USERNAME")
dateformat = datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
cwd = os.getcwd()
# endregion

root.mainloop()
