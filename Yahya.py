import os
from tkinter import *  
root=Tk()

def calculate():
    Chicken=e1.get()
    Kabali_Polao=e2.get()
    Chicken_Biryani=e3.get()
    Kebab=e4.get()
    Burger=e5.get()
    Tea=e6.get()
    print(type(Kebab))
    total=((int(Chicken)*700)+(int(Kabali_Polao)*300)+(int(Chicken_Biryani)*500)+(int(Kebab)*450)+(int(Burger)*200)+(int(Tea)*50))
    k=Label(root,text=total,font="times 36")
    k.place(x=200,y=500)
                                                                                                                      
   
t=Label(root,text="IMScience Cafeteria",font="time 34 bold")
t.place(x=500,y=30)

#----MENU-SECTION-----#

t=Label(root,text="MENU",font="time 24 bold")
t.place(x=1100,y=120)

u1=Label(root, text="Chicken                 Rs 700",font="time 18")
u1.place(x=1000,y=190)

v2=Label(root, text="Kabali Polao          Rs 300  ",font="time 18")
v2.place(x=1000,y=230)


w3=Label(root, text="Chicken Biryani     Rs 500 ",font="time 18")
w3.place(x=1000,y=270)

x4=Label(root,text="Kebab                   Rs 450  ",font="time 18")
x4.place(x=1000,y=310)

y5=Label(root,text="Burger                   Rs 200  ",font="time 18")
y5.place(x=1000,y=350)

z6=Label(root,text="Tea                        Rs 50  ",font="time 18")
z6.place(x=1000,y=390)


# ------Billing section----------#

a=Label(root,text="Select the item ",font="time 20 bold")
a.place(x=200,y=120)

u1=Label(root, text="Chicken",font="time 18")
u1.place(x=80,y=170)

e1=Entry(root)
e1.place(x=80,y=200)

v2=Label(root, text="Kabali Polao",font="time 18")
v2.place(x=340,y=170)

e2=Entry(root)
e2.place(x=340,y=200)

w3=Label(root, text="Chicken Biryani ",font="time 18")
w3.place(x=80,y=240)

e3=Entry(root)
e3.place(x=80,y=270)

x4=Label(root,text="Kebab",font="time 18")
x4.place(x=340,y=240)

e4=Entry(root)
e4.place(x=340,y=270)

y5=Label(root,text="Burger",font="time 18")
y5.place(x=80,y=300)

e5=Entry(root)
e5.place(x=80,y=340)

z6=Label(root,text="Tea",font="time 18")
z6.place(x=340,y=310)

e6=Entry(root)
e6.place(x=340,y=340)

#-------for Button-------#

b4=Button(root,text="Bill",width=18,command=calculate,font=" time 16 bold")
b4.place(x=140,y=400)

root.mainloop()