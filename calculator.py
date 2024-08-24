from tkinter import*
def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
       if scvalue.get(). isdigit():
           value= int(scvalue.get())
       else:
           value= eval(screen.get())

           scvalue.set(value)
           screen.update()

    elif text =="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update() 

vanshi_vats=Tk()
#Width X height
vanshi_vats.geometry("400x200")
vanshi_vats.title("CALCULATOR")

scvalue = StringVar()
scvalue.set("")
screen = Entry(vanshi_vats, textvar= scvalue, font="lucida 30 bold")
screen.pack(fill=X, ipadx=5, pady=5, padx=5)

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="9", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="8", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="7", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)
f.pack()

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="6", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="5", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="4", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)
f.pack()

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="3", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="2", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="1", font="lucida 20 bold")
b.pack(side = LEFT,padx=10,pady=11)
b.bind("<Button-1>", click)
f.pack()

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="0", font="lucida 20 bold")
b.pack(side = LEFT,padx=11,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="+", font="lucida 20 bold")
b.pack(side = LEFT,padx=11,pady=11)
b.bind("<Button-1>", click)

b= Button(f,text="-", font="lucida 20 bold")
b.pack(side = LEFT,padx=11,pady=11)
b.bind("<Button-1>", click)
f.pack()

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="*", font="lucida 20 bold")
b.pack(side = LEFT,padx=8,pady=10)
b.bind("<Button-1>", click)

b= Button(f,text="C", font="lucida 20 bold")
b.pack(side = LEFT,padx=8,pady=10)
b.bind("<Button-1>", click)

b= Button(f,text="%", font="lucida 20 bold")
b.pack(side = LEFT,padx=8,pady=10)
b.bind("<Button-1>", click)
f.pack()

f= Frame(vanshi_vats,bg= "black")
b= Button(f,text="=", font="lucida 20 bold")
b.pack(side = LEFT,padx=6,pady=8)
b.bind("<Button-1>", click)
f.pack()

b= Button(f,text="/", font="lucida 20 bold")
b.pack(side = LEFT,padx=6,pady=8)
b.bind("<Button-1>", click)
f.pack()

b= Button(f,text="log", font="lucida 20 bold")
b.pack(side = LEFT,padx=6,pady=8)
b.bind("<Button-1>", click)
f.pack()



vanshi_vats.mainloop()
