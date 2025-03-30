import tkinter as tk 

def show_text():
    user_text = entry.get()
    label.config(text = f'You typed: {user_text}')

#create the main window
root = tk.Tk()
root.title("My First GUI")
root.geometry("400x300") #width x height

#taking input
entry = tk.Entry(root, font = ("Arial", 14))
entry.pack(pady = 10)

#create a button
button = tk.Button(root, text="Submit", command = show_text, font = ("Arial", 14))
button.pack()

#create a label
label = tk.Label(root, text = "Type something above!", font = ("Arial", 16))
label.pack(pady = 20)


#run the application
root.mainloop()
