from tkinter import *
root = Tk()
root.geometry("644x444") #widthxheight
# root.minsize(200,400)#witdh,height
# root.maxsize(400,400)
root.title("Fun with tk")
label1 = Label(root,text="KFlsakflkkslkg")
# label1.pack()
label2 = Label(root,text = " safsdgasgahagda")
label1.grid(row=0,column=0)
label2.grid(row=1,column=0)

mybutton = Button(root,text="FRame sfd",state="disabled")
mybutton.grid(row= 1, column=4)
root.mainloop()