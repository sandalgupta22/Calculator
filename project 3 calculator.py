from tkinter import *

a = Tk()
a.geometry("360x240")
a.title("Calculator")
a.configure(bg="orange")


def cal():
    x = entry1.get()
    result = str(eval(x))
    labelres.configure(text=f"={result}",bg="white")


def one(m):
    if (m == 0):
        entry1.insert("end", "0")
    elif(m==1):
        entry1.insert("end","1")
    elif(m==2):
        entry1.insert("end","2")
    elif (m == 3):
        entry1.insert("end", "3")
    elif (m == 4):
        entry1.insert("end", "4")
    elif (m == 5):
        entry1.insert("end", "5")
    elif (m == 6):
        entry1.insert("end", "6")
    elif (m == 7):
        entry1.insert("end", "7")
    elif (m == 8):
        entry1.insert("end", "8")
    elif (m == 9):
        entry1.insert("end", "9")
    elif (m == "C"):
        entry1.delete(0,"end")
        labelres.configure(text="")
    elif (m == "Del"):
        entry1.delete(len(entry1.get())-1)
    elif (m == "+"):
        entry1.insert("end", "+")
    elif (m == "-"):
        entry1.insert("end", "-")
    elif (m == "%"):
        entry1.insert("end", "%")
    elif (m == "x"):
        entry1.insert("end", "*")
    elif (m == "/"):
        entry1.insert("end", "/")
    elif (m == 15):
        entry1.insert("end", ".")



num1 = StringVar()
entry1 = Entry(a,textvariable=num1)
labelres = Label(a)

button0 = Button(a,text="0",command=lambda : one(0),width=10)
buttonCal = Button(a,text="Calculate",command=cal,width=23)
button1 = Button(a,text="1",command=lambda : one(1),width=10)
button2 = Button(a,text="2",command=lambda : one(2),width=10)
button3 = Button(a,text="3",command=lambda : one(3),width=10)
button4 = Button(a,text="4",command=lambda : one(4),width=10)
button5 = Button(a,text="5",command=lambda : one(5),width=10)
button6 = Button(a,text="6",command=lambda : one(6),width=10)
button7 = Button(a,text="7",command=lambda : one(7),width=10)
button8 = Button(a,text="8",command=lambda : one(8),width=10)
button9 = Button(a,text="9",command=lambda : one(9),width=10)
buttondot = Button(a,text=".",command=lambda : one(15),width=10)
buttonC = Button(a,text="C",command=lambda : one("C"),width=10)
buttonDel = Button(a,text="🠔",command=lambda : one("Del"),width=10)
buttonplus = Button(a,text="+",command=lambda : one("+"),width=10)
buttonminus = Button(a,text="-",command=lambda : one("-"),width=10)
buttonpercent = Button(a,text="%",command=lambda : one("%"),width=10)
buttondivide = Button(a,text="/",command=lambda : one("/"),width=10)
buttonmul = Button(a,text="x",command=lambda : one("x"),width=10)






entry1.place(x=10,y=10,width=340,height=50)
buttonCal.place(x=180,y=200)
button0.place(x=0,y=200)
button1.place(x=0,y=170)
button2.place(x=90,y=170)
button3.place(x=180,y=170)
button4.place(x=0,y=140)
button5.place(x=90,y=140)
button6.place(x=180,y=140)
button7.place(x=0,y=110)
button8.place(x=90,y=110)
button9.place(x=180,y=110)
buttondot.place(x=90,y=200)
buttonC.place(x=0,y=80)
buttonDel.place(x=90,y=80)
buttonplus.place(x=270,y=170)
buttonminus.place(x=270,y=140)
buttonpercent.place(x=180,y=80)
buttondivide.place(x=270,y=80)
buttonmul.place(x=270,y=110)

labelres.place(x=310,y=35)
a.mainloop()