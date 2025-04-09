from tkinter import *
from tkinter import messagebox

def runwindow():
    messagebox.showinfo("Message","Submit Button is Clicked!")

root=Tk()

root.configure(background="lightblue")
root.geometry("600x300")

root.title("Simple GUI Application")
#root.resizable("False","False")

l1=Label(root,text="First GUI Application",padx=20,pady=20,font=("Arial",15,"bold"))
l1.grid(row=0,column=0)

l2=Label(root,text="Entre User Name",font=("Arial",12,"bold"))
l2.grid(row=1,column=0)

e1=Entry(root,font=("Arial",13,"bold"))
e1.grid(row=1,column=1,padx=20,pady=20)

l3=Label(root,text="Entre Password",font=("Arial",12,"bold"))
l3.grid(row=2,column=0)

e2=Entry(root,font=("Arial",13,"bold"),show="*")
e2.grid(row=2,column=1,padx=20,pady=20)

b1=Button(root,text="Submit",font=("Arial",15,"bold"),padx=50,command=runwindow)
b1.grid(row=3,column=1,padx=10,pady=20)

root.mainloop()