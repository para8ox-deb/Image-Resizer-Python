''' IMAGE RESIZER PROGRAM '''

from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk

def openimg():
    global img
    file=filedialog.askopenfilename(filetypes=[('JPG Images','*.jpg'),('PNG Images','*.png'),('All Images','*.*')])
    img=Image.open(file)
    
def saveimg():
    global img,newheight,newwidth
    width=int(newwidth.get())
    height=int(newheight.get())
    newwidth.set('')
    newheight.set('')
    img=img.resize((width,height),Image.ANTIALIAS)
    file=filedialog.asksaveasfilename(defaultextension='.jpg',filetypes=[('JPG Images','.jpg'),('PNG Images','.png')])
    img.save(file)

#Events Binding Functions
def enter1(event):
    impimg.config(bg='black',fg='white')
def leave1(event):
    impimg.config(bg='white',fg='black')

def enter2(event):
    saveimg.config(bg='black',fg='white')
def leave2(event):
    saveimg.config(bg='white',fg='black')

    

root=Tk()
root.geometry('450x500')
root.title('Image Resizer')
root.wm_iconbitmap('Images/icon.ico')
root.config(bg='#FFBA37')
root.minsize(450,500)


newheight=StringVar()
newwidth=StringVar()

#Bg Image
bgimg=Image.open('Images/bg.png')
bgimg=bgimg.resize((80,80),Image.ANTIALIAS)
#bgimg.putalpha(100) #To change opacity of image
bgpic=ImageTk.PhotoImage(bgimg)
bglabel=Label(image=bgpic)
bglabel.place(x=362,y=388)

#Heading:

f1=Frame(root,bg='#5300C6')
head=Label(f1,text='Image Resizer',font='Helvetica 25 bold',fg='white',bg='#5300C6',relief=SUNKEN,pady=3,padx=5)
head.pack(pady=15)
f1.pack(fill=X)


# Importing Image 
f2=Frame(root)
impimg=Button(f2,text='   Import Image   ',font='Arial 16 bold',command=openimg)
impimg.bind('<Enter>',enter1)
impimg.bind('<Leave>',leave1)
impimg.pack()
f2.pack(pady=40)

# Showing New Width and height options
f3=Frame(root,bg='black')
newh=Label(f3,text='New Height: ',font='lucida 16',bg='white')
newh.grid(row=0,column=0,padx=15)
hentry=Entry(f3,textvar=newheight,font='lucida 16',width=10,justify=CENTER)
hentry.grid(row=0,column=1,pady=15,padx=15)

neww=Label(f3,text='New Width: ',font='lucida 16',bg='white')
neww.grid(row=1,column=0)
wentry=Entry(f3,textvar=newwidth,font='lucida 16',width=10,justify=CENTER)
wentry.grid(row=1,column=1,pady=15)
f3.pack(pady=15)

#Save Image:
f4=Frame(root)
saveimg=Button(f4,text='Save New Image',font='Arial 16 bold',command=saveimg)
saveimg.pack()
saveimg.bind('<Enter>',enter2)
saveimg.bind('<Leave>',leave2)
f4.pack(pady=40)

#Status Bar:
sbar=Label(text='Image Resizer',relief=SUNKEN,anchor='w',pady=2,padx=10,font='lucida 10 italic')
sbar.pack(side=BOTTOM,fill=X)


root.mainloop()
