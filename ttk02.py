from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('600x400+700+250')
GUI.title('ไม่มีแฟน - Cocoa')

FONT1 = ('Angsana New',30)
FONT2 = ('Angsana New',25)


L1 = ttk.Label(GUI,text='จะมีแฟนไหม',font=FONT1)
L1.pack()

v_จะมีแฟนไหม = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_จะมีแฟนไหม,font=FONT2,width=30)
E1.pack()
#L1.place(x=50,y=200)

#########ไม่มีแฟน#######
L2 = ttk.Label(GUI,text='คำตอบ',font=FONT1)
L2.pack()

v_คำตอบ = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_คำตอบ,font=FONT2,width=30)
E2.pack()

#####BUTON########
def SaveVocab(evant=None):
    จะมีแฟนไหม = v_จะมีแฟนไหม.get()
    คำตอบ = v_คำตอบ.get()
    print('V: {} M: {}'. format(จะมีแฟนไหม,คำตอบ))
    v_จะมีแฟนไหม.set('')
    v_คำตอบ.set('')
    E1.focus()
    print('-------------')






B1 = ttk.Button(GUI,text='Save ไม่มีแฟน',command=SaveVocab)
B1.pack(ipadx=40,ipady=20,pady=20)

E2.bind('<Return>',SaveVocab)





GUI.mainloop()
