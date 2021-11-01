import tkinter as tk
from tkinter import ttk


def create_output(name, id, blood_letter, rh_factor):
    out_string = f"Patient name: {name}\n"
    out_string += f"Rh Factor: {rh_factor}\n\n"


def design_window():
    def ok_buttom_cmd():
        # Get needed data from GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor = rh_data.get()

        # Call external function to do the work that can be tested
        answer = create_output(name, id, blood_letter, rh_factor)

        # Update GUI
        print(answer)

    def cancel_cmd():
        root.destroy()

    root = tk.Tk()
    root.title("Health Database GUI")
    # root.geometry("300x200")
    top_label = ttk.Label(root, text="Blood Donor Database", font=14)
    top_label.grid(column=0, row=0)

    name_label = ttk.Label(root, text="Name:", font=12)
    name_label.grid(column=0, row=1, pad_y=10, sticky="e")
    # If you know you will never use this label again
    # ttk.Label(root, text="Name").grid(column=0, row=1)

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(root, width=50, textvariable=name_data)
    name_entry_box.grid(column=1, row=1)

    id_label = ttk.Label(root, text="ID:", font=12)
    id_label.grid(column=0, row=2, pad_y=10)

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(root, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2)

    blood_letter_data = tk.StringVar()
    ttk.RadioButton(root,
                    text="A",
                    variable=blood_letter_data,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.RadioButton(root,
                    text="B",
                    variable=blood_letter_data,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.RadioButton(root,
                    text="AB",
                    variable=blood_letter_data,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.RadioButton(root,
                    text="O",
                    variable=blood_letter_data,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_data = tk.StringVar()
    rh_checkbox = ttk.Checkbutton(root, text="Rh Positive",
                                  variable=rh_data, on_value="+",
                                  offvalue="-")

    rh_checkbox.grid(column=1, row=4)

    ok_button = ttk.Button(root, text="OK", command=ok_buttom_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_cmd)
    cancel_button.grid(column=2, row=6)

    root.mainloop()


if __name__ == '__main__':
    design_window()
