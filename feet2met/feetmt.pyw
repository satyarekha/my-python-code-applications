from tkinter import Tk,Button,Label,DoubleVar,Entry

window =Tk()
window.title("Feet to meter conversion")
window.configure(background="red")
window.geometry("320x320")
window.resizable(width=False,height=False)

def convert():
    value=float(ft_entry.get())
    meter=value*0.3048
    mt_value.set("%.4f"  % meter)

def clear():
    mt_value.set("")
    ft_value.set("")





ft_lbl =Label(window,text="feet",bg="purple",fg="white",width=14)
ft_lbl.grid(column=0,row=0,padx=15,pady=15)

ft_value=DoubleVar()
ft_entry=Entry(window,textvariable=ft_value,width=14)
ft_entry.grid(column=1,row=0)
ft_entry.delete(0,'end')
mt_lbl=Label(window,text="meter",bg="pink",fg="blue",width=14)
mt_lbl.grid(column=0,row=1,padx=15,pady=15)
mt_value= DoubleVar()
mt_entry=Entry(window,textvariable=mt_value,width=14)
mt_entry.grid(column=1,row=1,pady=30)
mt_entry.delete(0,'end')
convert_btn=Button(window,text="convert",bg="purple",fg="white",width=14,command=convert)
convert_btn.grid(column=0,row=3,padx=15)
clear_btn=Button(window,text="clear",bg="pink",fg="white",width=14,command=clear)
clear_btn.grid(column=1,row=3,padx=15)

window.mainloop()
