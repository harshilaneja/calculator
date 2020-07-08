
from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"


        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("644x970")
root.title("Calculator ")

scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)
f = Frame(root)
f.pack(side=TOP)

temp= 1
for i in range(0,3):
    for j in range(0,3):
        btn= Button(f,text= str(temp),font= "lucida 30 bold",width= 5)
        btn.grid(row= i,column= j,padx= 5,pady= 5)
        temp= temp+1
        btn.bind("<Button-1>", click)

b = Button(f, text="0",font="lucida 30 bold",width=5)
b.grid(row=3,column=0,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="*",font="lucida 30 bold",width=5)
b.grid(row=3,column=1,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="-",font="lucida 30 bold",width=5)
b.grid(row=3,column=2,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="/",font="lucida 30 bold",width=5)
b.grid(row=4,column=0,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="%",font="lucida 30 bold",width=5)
b.grid(row=4,column=1,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="=",font="lucida 30 bold",width=5)
b.grid(row=4,column=2,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="c",font="lucida 30 bold",width=5)
b.grid(row=5,column=0,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text=".",font="lucida 30 bold",width=5)
b.grid(row=5,column=1,padx=5,pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="00",font="lucida 30 bold",width=5)
b.grid(row=5,column=2,padx=5,pady=5)
b.bind("<Button-1>", click)

root.mainloop()