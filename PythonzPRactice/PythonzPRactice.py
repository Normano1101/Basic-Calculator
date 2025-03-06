import tkinter as tk 

def addNums():
    
    outVar.set(float(entry1.get())+float(entry2.get()))

def subNums():
    outVar.set(float(entry1.get())-float(entry2.get()))

def multNums():
    outVar.set(float(entry1.get())*float(entry2.get()))

def divNums():
    outVar.set(float(entry1.get())/float(entry2.get()))

window = tk.Tk()
window.geometry("400x400")
window.title("Simple Calculator")

outVar = tk.StringVar()
outVar.set("Output Variable")


button1 = tk.Button(window, text = "Add", command= addNums)
button1.grid(row = 0, column = 0)

button2 = tk.Button(window, text = "Subtract", command= subNums)
button2.grid(row = 1, column = 0)

button3 = tk.Button(window, text = "Multiply", command= multNums)
button3.grid(row = 2, column = 0)

button4 = tk.Button(window, text = "Divide", command= divNums)
button4.grid(row = 3, column = 0)

entry1 = tk.Entry(window)
entry1.grid(row = 4, column = 0)

entry2 = tk.Entry(window)
entry2.grid(row = 5, column = 0)


label =tk.Label(window, textvariable = outVar)
label.grid(row= 6, column=0, columnspan=2)

window.mainloop()
