from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี้คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมสักอย่าง') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี้คือขนาดโปรแกรม

B1 = ttk.Button(GUI,text='ข้าวเปล่า')
B1.pack(ipadx=20,ipady=20)

L1 = Label(GUI,text='ข้าว',font=('Angsana New',30),fg='pink')
L1.place(x=30,y=20)
############
def Button2 ():
    text = 'ตอนนี้ข้าวมันไก่หมด'
    messagebox.showwarning('ข้าวมันไก่',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=300)
B2 = ttk.Button(FB1,text='ข้าวมันไก่',command=Button2)
B2.pack(ipadx=20,ipady=20)
############

############
def Button3 ():
    text = 'ตอนนี้ข้าวขาหมาหมด'
    messagebox.showwarning('ข้าวขาหมา',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=300)
B3 = ttk.Button(FB1,text='ข้าวขาหมา',command=Button3)
B3.pack(ipadx=20,ipady=20)
############

############
def Button4 ():
    text = 'ตอนนี้ข้าวปลากระป๋องหมด'
    messagebox.showwarning('ข้าวปลากระป๋อง',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=300,y=300)
B3 = ttk.Button(FB1,text='ข้าวปลากระป๋อง',command=Button4)
B3.pack(ipadx=20,ipady=20)
############

GUI.mainloop()
