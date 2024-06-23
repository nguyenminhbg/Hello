import tkinter as tk
from Main import greet, method2
root = tk.Tk()
root.title("The simple UI")
root.geometry('500x500')
root['bg']='gray'
label=tk.Label(root,text="Hello, this is sample example")
label.place(x=250,y=250)
count = 1
def on_button_click():
    global count
    print(count)
    label.config(text="You already clicked on button")
    if count%2==0:
        label.config(text="The content is empty")
    else:
        label.config(text="The label content is changed")
    count +=1
    greet("Minh Nguyen")
    method2(35)
    label1=tk.Label(root,text="Add more")
    label1.pack()
    print("Add git")
button=tk.Button(root,text="Click here", command=on_button_click)
button.pack(pady=20)
root.mainloop()