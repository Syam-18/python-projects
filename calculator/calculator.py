import tkinter as tk


def on_button_click(value):
    entry.insert(tk.END, value)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")   

def clear_entry():
    entry.delete(0, tk.END)

#Intialize the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("600x500") #width x height


#Entry field to display inputs and results
entry = tk.Entry(root, justify="right",font=("Arial", 20), bd = 10)
entry.pack(fill = "both", padx = 10, pady = 10)

#Button layout 
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

#create buttons and add them to the window
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(fill = "both", expand = True)
    for char in row:
        btn = tk.Button(frame, font=("Arial", 20), text = char, padx = 20, pady = 20)
        btn.pack(side="left", fill="both", expand = True)

        if char == "=":
            btn.config(command = calculate_result)
        elif char == "C":
            btn.config(command = clear_entry)
        else:
            btn.config(command = lambda ch=char:on_button_click(ch))
        
root.mainloop()
