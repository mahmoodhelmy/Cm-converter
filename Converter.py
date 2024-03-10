import tkinter as tk

root = tk.Tk()

window = root.geometry('250x100')
Tl = root.title("converter")
labfeet = tk.Label(root,text="Enter Feet")
labfeet.grid(row=1,column=1)
enfeet = tk.Entry(root,textvariable=tk.IntVar())
enfeet.grid(row=1,column=2)
labin = tk.Label(root,text="Enter inch")
labin.grid(row=2,column=1)
enin = tk.Entry(root,textvariable=tk.IntVar())
enin.grid(row=2,column=2)

def con():
    x= int(enfeet.get())
    enfeet.delete
    y= int(enin.get())
    enin.delete
    z= x*30 + y*2.5
    labcon =tk.Label(root,text=z)
    labcon.grid(row=3,column=2)



conbut =tk.Button(root,text="Convert",command=con)
conbut.grid(row=3,column=1)
root.mainloop()