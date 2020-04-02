#https://github.com/Mayank18-dotcom/pyPiano.git
from Tkinter import *
from sqlite3 import *
from Tkinter import *
import sys
import pygame
import mp3play

pygame.init()
#Create a database and a cursor
conn = connect("Users.db")


curs = conn.cursor()


#Create a Table for the program 
sql_table = """ CREATE TABLE USERS10 (
                    username text,
                    password password
                    )            
            """
try:
    curs.execute(sql_table)
except OperationalError:
    pass
except:
    sys.exit()

def SignUp():
    #Create a database and a cursor
    conn = connect("Users.db")
    curs = conn.cursor()

    sql_table = """INSERT INTO 'USERS10'
                          ('username', 'password') 
                          VALUES (?, ?);"""
    data_tuple = (Username.get(),Password.get()) 
    #Commit Changes
    curs.execute(sql_table, data_tuple)
    conn.commit()
    #Close the database (Optional) since Sqlite3 does it automatically
    conn.close()
    signupSuccess()

    Username.delete(0, END)
    Password.delete(0, END)

def login():
    conn = connect("Users.db")
    curs = conn.cursor()

    sql_table=("SELECT * FROM USERS10 WHERE username = ? AND password = ?")
    curs.execute(sql_table,([(Username.get()),(Password.get())]))
    res=curs.fetchall()

    if res:
        loginSuccess()
        
    else:
        loginFailed()

    conn.commit()
    #Close the database (Optional) since Sqlite3 does it automatically
    conn.close()

def signupSuccess():
    top1=Toplevel()
    top1.geometry("400x200+200+200")
    top1.title("SUCCESS!")
    l=Label(top1,text="SIGN UP SUCCESSFULL!!!")
    l.pack(side=TOP)
    l=Label(top1,text="")
    l.pack(side=TOP)
    l=Label(top1,text="CLICK BELOW TO PLAY")
    l.pack(side=TOP)
    l=Label(top1,text="")
    l.pack(side=TOP)
    b=Button(top1, text="PLAY", command=validation ,width=10)
    b.pack(side=TOP)


def loginSuccess():
    top1=Toplevel()
    top1.geometry("400x200+200+200")
    top1.title("SUCCESS!")
    l=Label(top1,text="LOGIN SUCCESSFULL!!!")
    l.pack(side=TOP)
    l=Label(top1,text="")
    l.pack(side=TOP)
    l=Label(top1,text="CLICK BELOW TO PLAY")
    l.pack(side=TOP)
    l=Label(top1,text="")
    l.pack(side=TOP)
    b=Button(top1, text="PLAY", command=validation ,width=10)
    b.pack(side=TOP)
    
def loginFailed():
    top2=Toplevel()
    top2.geometry("400x200+200+200")
    top2.title("FAILED")
    l=Label(top2,text="LOGIN FAILED")
    l.pack(side=TOP)
    l=Label(top2,text="")
    l.pack(side=TOP)
    l=Label(top2,text="CLOSE THIS AND TRY AGAIN")
    l.pack(side=TOP)

def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def validation():
    top=Toplevel()
    top.geometry("800x400+200+200")
    def value_Cs():
        num1.set("C#")
        sound=pygame.mixer.Sound("./Music_Notes/C_s.wav")
        sound.play()
        return num1

    def value_Ds():
        num1.set("D#")
        sound=pygame.mixer.Sound("./Music_Notes/D_s.wav")
        sound.play()
        return num1

    def value_Fs():
        num1.set("F#")
        sound=pygame.mixer.Sound("./Music_Notes/F_s.wav")
        sound.play()
        return num1

    def value_Gs():
        num1.set("G#")
        sound=pygame.mixer.Sound("./Music_Notes/G_s.wav")
        sound.play()
        return num1

    def value_Bb():
        num1.set("Bb#")
        sound=pygame.mixer.Sound("./Music_Notes/Bb.wav")
        sound.play()
        return num1

    def value_Cs1():
        num1.set("C#1")
        sound=pygame.mixer.Sound("./Music_Notes/C_s1.wav")
        sound.play()
        return num1

    def value_Ds1():
        num1.set("D#1")
        sound=pygame.mixer.Sound("./Music_Notes/D_s1.wav")
        sound.play()
        return num1

    def value_C():
        num1.set("C")
        sound=pygame.mixer.Sound("./Music_Notes/C.wav")
        sound.play()
        return num1

    def value_D():
        num1.set("D")
        sound=pygame.mixer.Sound("./Music_Notes/D.wav")
        sound.play()
        return num1

    def value_E():
        num1.set("E")
        sound=pygame.mixer.Sound("./Music_Notes/E.wav")
        sound.play()
        return num1

    def value_F():
        num1.set("F")
        sound=pygame.mixer.Sound("./Music_Notes/F.wav")
        sound.play()
        return num1

    def value_G():
        num1.set("G")
        sound=pygame.mixer.Sound("./Music_Notes/G.wav")
        sound.play()
        return num1

    def value_A():
        num1.set("A")
        sound=pygame.mixer.Sound("./Music_Notes/A.wav")
        sound.play()
        return num1

    def value_B():
        num1.set("B")
        sound=pygame.mixer.Sound("./Music_Notes/B.wav")
        sound.play()
        return num1

    def value_C1():
        num1.set("C1")
        sound=pygame.mixer.Sound("./Music_Notes/C1.wav")
        sound.play()
        return num1

    def value_D1():
        num1.set("D1")
        sound=pygame.mixer.Sound("./Music_Notes/D1.wav")
        sound.play()
        return num1

    def value_E1():
        num1.set("E1")
        sound=pygame.mixer.Sound("./Music_Notes/E1.wav")
        sound.play()
        return num1

    def value_F1():
        num1.set("F1")
        sound=pygame.mixer.Sound("./Music_Notes/F1.wav")
        sound.play()
        return num1
    
    def melody1():
        num1.set("Melody 1")
        sound=pygame.mixer.Sound("./Music_Notes/fur.wav")
        sound.play()
        return num1
    
    def melody2():
        num1.set("Melody 2")
        sound=pygame.mixer.Sound("./Music_Notes/rondo.wav")
        sound.play()
        return num1

    frame=Frame(top)
    frame.pack()

    top.title('pyPiano')

    num1=StringVar()

    topframe=Frame(top)
    topframe.pack(side=TOP)

    f = mp3play.load('./Music_Notes/drum1.mp3'); play = lambda: f.play()
    button100=Button(frame,height=2,width=15,text="Drums 1",command = play)
    button100.pack(side=LEFT)

    f1 = mp3play.load('./Music_Notes/drum2.mp3'); play1 = lambda: f1.play()
    button100=Button(frame,height=2,width=15,text="Drums 2",command = play1)
    button100.pack(side=LEFT)

    i=0
    while i<1:
        button22=Button(frame,state=DISABLED,height=2,width=5,padx=0,pady=0,relief=RIDGE,border=0)
        button22.pack(side=LEFT)
        i+=1
    f2 = mp3play.load('./Music_Notes/ave.mp3'); play2 = lambda: f2.play()
    button101=Button(frame,height=2,width=15,text="Melody 2",command = play2)
    button101.pack(side=RIGHT)
    i=0

    f3 = mp3play.load('./Music_Notes/fur.mp3'); play3 = lambda: f3.play()
    button101=Button(frame,height=2,width=15,text="Melody 1",command = play3)
    button101.pack(side=RIGHT)
    i=0
    while i<1:
        button22=Button(frame,state=DISABLED,height=2,width=5,padx=0,pady=0,relief=RIDGE,border=0)
        button22.pack(side=RIGHT)
        i+=1

    txtDisplay=Entry(frame,textvariable=num1,bd=20,insertwidth=1,font=30,justify='center',width=8)
    txtDisplay.pack(side=TOP)
    

    

    #************************************************************************************************
    button1=Button(topframe,padx=8,height=7,pady=8,text="C#",bg="black",fg="white",command=value_Cs)
    button1.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE,border=0)
    button22.pack(side=LEFT)

    button2=Button(topframe,padx=8,height=7,pady=8,text="D#",bg="black",fg="white",command=value_Ds)
    button2.pack(side=LEFT)

    i=0
    while i<12:
        button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
        button22.pack(side=LEFT)
        i=i+1

    
    

    button1=Button(topframe,padx=8,height=7,pady=8,text="C#",bg="black",fg="white",command=value_Cs)
    button1.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE,border=0)
    button22.pack(side=LEFT)

    button2=Button(topframe,padx=8,height=7,pady=8,text="D#",bg="black",fg="white",command=value_Ds)
    button2.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
    button22.pack(side=LEFT)

    button3=Button(topframe,padx=8,height=7,pady=8,text="F#",bg="black",fg="white",command=value_Fs)
    button3.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
    button22.pack(side=LEFT)

    button4=Button(topframe,padx=8,height=7,pady=8,text="G#",bg="black",fg="white",command=value_Gs)
    button4.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
    button22.pack(side=LEFT)

    i=0
    while i<12:
        button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
        button22.pack(side=LEFT)
        i=i+1    

    button3=Button(topframe,padx=8,height=7,pady=8,text="F#",bg="black",fg="white",command=value_Fs)
    button3.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
    button22.pack(side=LEFT)

    button4=Button(topframe,padx=8,height=7,pady=8,text="G#",bg="black",fg="white",command=value_Gs)
    button4.pack(side=LEFT)
    button22=Button(topframe,state=DISABLED,height=8,width=1,padx=0,pady=0,relief=RIDGE, border=0)
    button22.pack(side=LEFT)
    #************************************************************************************************
    frame1=Frame(top)
    frame1.pack(side=TOP)
    #************************************************************************************************
    button1=Button(frame1,padx=16,height=7,pady=16,bd=8,text="C",bg="white",fg="grey",command=value_C)
    button1.pack(side=LEFT)

    button2=Button(frame1,padx=16,height=7,pady=16,bd=8,text="D",bg="white",fg="grey",command=value_D)
    button2.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="E",bg="white",fg="grey",command=value_E)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="F",bg="white",fg="grey",command=value_F)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="G",bg="white",fg="grey",command=value_G)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="A",bg="white",fg="grey",command=value_A)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="B",bg="white",fg="grey",command=value_B)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="C1",bg="white",fg="grey",command=value_C1)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="D1",bg="white",fg="grey",command=value_D1)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="E1",bg="white",fg="grey",command=value_E1)
    button3.pack(side=LEFT)

    button3=Button(frame1,padx=16,height=7,pady=16,bd=8,text="F1",bg="white",fg="grey",command=value_F1)
    button3.pack(side=LEFT)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = Tk()

root.geometry("400x200+200+200")


#Create Label and Entries
l1 = Label(root, text="Username")
l1.grid(row=1, column=0)
Username = Entry(root, width=50)
Username.grid(row=1, column= 1, padx=10)

l2 = Label(root, text="Password")
l2.grid(row=2, column=0)
Password = Entry(root, width=50)
Password.grid(row=2, column= 1, padx=10)
#command = combine_funcs(validation, SignUp)
#Create Buttons
Insert_Button = Button(root, text="Sign Up",command=SignUp ,width=10)
Insert_Button.grid(row=6, column=1)

Select_Button = Button(root, text="Login", command=login ,width=10)
Select_Button.grid(row=10, column=1)
#Commit Changes
conn.commit()
#Close the database (Optional) since Sqlite3 does it automatically
conn.close()

mainloop()