from tkinter import *

window=Tk()
window.title('CALCULATOR')
window.geometry('400x400')
window.configure(bg='grey')

def calculate_interest():
    p=float(principal.get())
    r=float(rate.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest=round(i,2)
    result.destroy()

    message= Label(frame,text='Interest '+str(p)+ ' at rate of interest '+str(r)+ ' for'+str(t)+ 'years is Rs'+str(interest),bg='white',font=('Calibri',12),width=45)
    message.place(x=20,y=40)
    message.pack()


headinglabel=Label(window,text='Calculator',fg='black',bg='grey',font=('Calibri',30),bd=5)
headinglabel.place(x=140,y=10)


principal=Label(window,text='Principal',fg='black',font=('Calibri',20),bg='grey',bd=3)
principal.place(x=80,y=70)

principal=Entry(window,text='',bd=4,width=22,fg='white',bg='black')
principal.place(x=185,y=80)

rate=Label(window,text='Rate',fg='black',font=('Calibri',20),bg='grey',)
rate.place(x=80,y=110)

rate=Entry(window,text='',bd=4,width=22,fg='white',bg='black')
rate.place(x=185,y=120)

time=Label(window,text='Time',fg='black',font=('Calibri',20),bg='grey')
time.place(x=80,y=150)

time=Entry(window,text='',bd=4,width=22,fg='white',bg='black')
time.place(x=185,y=160)

button=Button(window,text='Calculate',fg='black',bg='red',bd=4,command=calculate_interest)
button.place(x=150,y=250)


frame=LabelFrame(window,text='CALCULATION',bg='white',font=('Calibri',12))
frame.pack(padx=20,pady=20)
frame.place(x=20,y=300)

result=Label(frame,text='',bg='white',font=('Calibri',12),width=30)
result.place(x=20,y=20)
result.pack()

window.mainloop()
