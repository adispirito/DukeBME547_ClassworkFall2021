import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk

# from health_db_client import add_patient_to_server


def create_output(name, id, blood_letter, rh_factor, center):
    out_string = f"Patient name: {name}\n"
    out_string += f"Rh Factor: {rh_factor}\n"
    out_string += f"Center: {center}\n\n"
    # answer = add_patient_to_server(name, id)
    return out_string, answer


def load_and_resize_image(adj_factor):
    filepath = filedialog.askopenfilename(initialdir = "./images")
    if filepath == "":
        messagebow.showinfo("Cancel", "You cancelled the image load")
        return
    pil_image = Image.open(filepath)
    original_size = pil_image.size
    new_size = [int(round(dim * adj_factor, 0)) for dim in original_size]
    resized_image = pil_image.resize(new_size)
    tk_image = ImageTk.PhotoImage(resized_image)
    return tk_image


def design_window():
    def ok_buttom_cmd():
        # Get needed data from GUI
        name = name_data.get()
        id = id_data.get()
        blood_letter = blood_letter_data.get()
        rh_factor = rh_data.get()
        center=donation_cneter_data.get()

        # Call external function to do the work that can be tested
        answer = create_output(name, id, blood_letter, rh_factor, center)

        # Update GUI
        print(answer)

        output_string.configure(text=str(answer)) # update GUI with response from server

    def cancel_cmd():
        root.destroy()

    def change_pic_cmd():
        filename = "images/duke_campus.jpg"
        pil_image = Image.open(filename)
        tk_image = ImageTk.PhotoImage(pil_image)
        image_labelk.configure(image=tk_image)
        image_label.image = tk_image

    root = tk.Tk()
    root.title("Health Database GUI")
    # root.geometry("300x200")
    top_label = ttk.Label(root, text="Blood Donor Database", font=14)
    top_label.grid(column=0, row=0, columnspan=2, sticky="w")

    name_label = ttk.Label(root, text="Name:", font=12)
    name_label.grid(column=0, row=1, pady=10, sticky="e")
    # If you know you will never use this label again
    # ttk.Label(root, text="Name").grid(column=0, row=1)

    name_data = tk.StringVar()
    name_entry_box = ttk.Entry(root, width=25, textvariable=name_data)
    name_entry_box.grid(column=1, row=1, sticky="w")

    id_label = ttk.Label(root, text="ID:", font=12)
    id_label.grid(column=0, row=2, pady=10, sticky="w")

    id_data = tk.StringVar()
    id_entry_box = ttk.Entry(root, width=10, textvariable=id_data)
    id_entry_box.grid(column=1, row=2)

    blood_letter_data = tk.StringVar()
    blood_letter_data.set("AB")
    ttk.Radiobutton(root,
                    text="A",
                    variable=blood_letter_data,
                    value="A").grid(column=0, row=3, sticky=tk.W)
    ttk.Radiobutton(root,
                    text="B",
                    variable=blood_letter_data,
                    value="B").grid(column=0, row=4, sticky=tk.W)
    ttk.Radiobutton(root,
                    text="AB",
                    variable=blood_letter_data,
                    value="AB").grid(column=0, row=5, sticky=tk.W)
    ttk.Radiobutton(root,
                    text="O",
                    variable=blood_letter_data,
                    value="O").grid(column=0, row=6, sticky=tk.W)

    rh_data = tk.StringVar()
    rh_data.set('-')
    rh_checkbox = ttk.Checkbutton(root, text="Rh Positive",
                                  variable=rh_data, onvalue="+",
                                  offvalue="-")

    rh_checkbox.grid(column=1, row=4)

    ok_button = ttk.Button(root, text="OK", command=ok_buttom_cmd)
    ok_button.grid(column=1, row=6)

    cancel_button = ttk.Button(root, text="Cancel", command=cancel_cmd)
    cancel_button.grid(column=2, row=6)

    ttk.Label(root, text="Nearest Donation Center").grid(column=2, row=0)

    donation_cneter_data = tk.StringVar
    combo_box = ttk.Combobox(root, textvariable=donation_cneter_data)
    combo_box["values"] = ("Durham", "Raleigh", "Cary", "Apex")
    combo_box.state(["readonly"])
    combo_box.grid(column=3, row=1)

    output_string = ttk.Label(root)

    adj_factor = 0.5
    filepath = "images/duke_chapel.jpg"
    tk_image = load_and_resize_image(adj_factor)
    image_label = ttk.Label(root, image=tk_image)
    image_label.grid(column=0, row=7)


    root.mainloop()


if __name__ == '__main__':
    design_window()
