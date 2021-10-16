import time
import tkinter as tk
from tkinter import *
import tkinterDnD
import webbrowser
import pathlib
import pickle


ganz = 1
sitzung = 1
links = []
speicher = []
sort = []
print("sort anfang:",sort)
path = pathlib.Path('links.txt')
linkp= pathlib.Path("links.txt")
print(type(path))
print(path)
print("linkp existiert:",linkp.exists())




root = tkinterDnD.Tk()
root.title("InspirationsWerkzeug")
root.geometry("600x400")
root.resizable(width=False, height=False)

stringvar = tk.StringVar()
stringvar.set('Links hier rein')


def initial():
    global ganz
    global links
    while not linkp.exists():
        liste = open('links.txt','w')
        liste.close()
        with open('links.txt','wb') as fb:
            pickle.dump(links,fb)
    ganz = len(links)
    with open('links.txt','rb') as fp:
        links = pickle.load(fp)
    return links

initial()

def dialog():
    dialogF = Toplevel(root)
    dialogF.title("Duplikate löschen")
    dialogF.geometry("200x100")
    dialogF.resizable(width=False, height=False)
    Label(dialogF,text="Duplikate löschen?").place(x=50,y=10)
    Button(dialogF,text="Ja",width=10,command=duplikate).place(x=65,y=60)

def duplikate():
    print("Vorher:",links)
    sort = list(dict.fromkeys(links))
    print("Nachher:",sort)
    linkp.unlink
    liste = open('links.txt','w')
    with open('links.txt','wb') as fb:
        pickle.dump(sort,fb)

def drop(event):
    global sitzung
    global ganz
    global links
    ganz = len(links)
    sitzN = Label(root, text=sitzung).place(x=573,y=30)
    GesN = Label(root, text=(str(ganz+1))).place(x=573,y=10)
    labelL = Label(root, textvar=(event.data), relief="solid",height=25,width=70)
    sitzung += 1
    ganz += 1
    speicher.append(event.data)
    links.append(event.data)
    with open('links.txt','wb') as fp:
        pickle.dump(links,fp)
    return sitzung, ganz, links


nummer = StringVar(value=0)
Nummer = Spinbox(root, from_=0,to=10,width=11,textvar=nummer).place(x=513,y=140)

def inspiration():
    global links
    url= ""
    Number = int((nummer.get()))
    print(Number)
    dex = 0
    if not sort:
        print("links",links)
        for i in range(Number):
            url = links[dex]
            time.sleep(0.5)
            webbrowser.open_new_tab(url)
            dex +=1
    else:
        print("sort:",sort)
        for i in range(Number):
            url = sort[dex]
            time.sleep(0.5)
            webbrowser.open_new_tab(url)
            dex +=1

def anzeigen():
    global links
    i = 0
    newWindow = Toplevel(root)
    newWindow.title("Sitzungseinträge")
#    newWindow.geometry("400x200")
    Label(newWindow,text=("\n".join(speicher)),justify="left").pack()
#    Label.config(newWindow,)

def lloeschen():
    linkp.unlink
    liste = open('links.txt','w')
    links.clear()
    with open('links.txt','wb') as fb:
        pickle.dump(links,fb)


Links = Label(root, text="Speicher:").place(x=513,y=10)
Sitzung = Label(root, text="Sitzung:").place(x=513,y=30)
buttonI = Button(root, text="Inspiration",width=10,height=5,command=inspiration).place(x=513,y=165)
buttonD = Button(root, text="Duplikate",width=10,height=5, command=dialog).place(x=513,y=255)
buttonA = Button(root, text="Hinzugefügt",width=10,height=2,command=anzeigen).place(x=513,y=50)
buttonL = Button(root, text="Löschen",width=10,height=2,command=lloeschen).place(x=513,y=345)
labelD = tk.Label(root, textvar=stringvar, relief="solid",height=25,width=70)

labelD.place(x=10,y=10)

labelD.register_drop_target("*")
labelD.bind("<<Drop>>", drop)


root.mainloop()
