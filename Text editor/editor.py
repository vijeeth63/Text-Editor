import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    if confirm_clear():
        text_area.delete("1.0", tk.END)

def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt",
                                           filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            text_area.delete("1.0", tk.END)
            text_area.insert("1.0", content)

def save_file():

    filepath = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filepath:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(text_area.get("1.0", tk.END))
        messagebox.showinfo("Saved", "File saved successfully!")

def confirm_clear():
    return messagebox.askokcancel("New File", "Clear current text?")

def undo():
    try:
        text_area.edit_undo()
    except tk.TclError:
        pass

def redo():
    try:
        text_area.edit_redo()
    except tk.TclError:
        pass

def clear_all():
    if confirm_clear():
        text_area.delete("1.0", tk.END)


root = tk.Tk()
root.title("Simple Text Editor")
root.geometry("700x500")
root.config(bg="#ffe9b3")  


toolbar = tk.Frame(root, bg="#fff2cc", height=40)
toolbar.pack(side=tk.TOP, fill=tk.X)

btn_new = tk.Button(toolbar, text="New", command=new_file, bg="#ffad60", fg="black")
btn_open = tk.Button(toolbar, text="Open", command=open_file, bg="#f9dc5c", fg="black")
btn_save = tk.Button(toolbar, text="Save", command=save_file, bg="#a3de83", fg="black")
btn_undo = tk.Button(toolbar, text="Undo", command=undo, bg="#7fcd91", fg="black")
btn_redo = tk.Button(toolbar, text="Redo", command=redo, bg="#6dd3ce", fg="black")
btn_clear_all = tk.Button(toolbar, text="Clear", command=clear_all, bg="#ffaaa5", fg="black")


for btn in [btn_new, btn_open, btn_save, btn_undo, btn_redo, btn_clear_all]:
    btn.pack(side=tk.LEFT, padx=4, pady=5)


text_area = tk.Text(root, wrap=tk.WORD, undo=True, font=("Consolas", 12), bg="white")
text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)


root.mainloop()
