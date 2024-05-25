#CHAT BOT USING PYTHON

from tkinter import*
root = Tk() 
root.title("Chat bot")
def send() :
    send = "You—>"+e.get()
    txt.insert(END,send)
    user = e.get().lower()
    if (user=='hello'):
        txt.insert(END,"\n",+"Bot—>Hello")
    elif(user=='hi' or user=='hii' or user=='hiii'):
        txt.insert(END,"\n",+"Bot—>Hello")
    elif(e.get()=="how are you"):
        txt.insert(END,"\n",+"Bot->fine! and you")
    elif(user=="fine" or user++"i am good" or user=="i am doing good"):
        txt.insert(END,"\n",+"Bot->great!how can i help you")
    elif(user=="what's your name"):
        txt.insert(END,"\n",+"Bot->My name is Siri")
    else :
        txt.insert(END,"\n",+"Bot—>Sorry! I didn't get you")
        e.delete(0,END)
    txt.Text(root)
    txt.grid(row=0,column=0,columnspan=2)
    e.Entry(root,width=100)
    e.grid(row=1,column=0)
    send = Button(root,text="send",command=send).grid(row=1,column=1)
    root.mainloop()
