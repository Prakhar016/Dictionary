from PyDictionary import PyDictionary
import tkinter as tk
from tkinter import messagebox
from tkinter import *
class user_interface(Frame):
    def __init__ (self,root):
        super().__init__(root)
        self.root = root
        self.wordlist=[]
        self.heading=Label(self.root,text="Dictionary",bg="#25CCF7",fg="black",font=("Courier 20 bold"))
        self.heading.place(x=10,y=10,width=600,height=50)
        self.word_enter= Label(self.root, text="enter word : ",fg="black", font=("Time 15 bold"))
        self.word_enter.place(x=15, y=60)
        self.entry = Entry(self.root)
        self.entry.place(x=150,y=60, width=300, height=30)
        self.nxt_btn = Button(self.root, text="Search", width=10,bg="#ffcccc", fg="black",command= lambda: self.next_click())
        self.nxt_btn.place(x=400,y=60, width=200, height=30)
        self.word_enter = Label(text="Designed & developed by Prakhar Jagnani", fg="black", font=("Time 15 bold"))
        self.word_enter.place(x=90, y=360)
    def next_click(self):
        a=''
        word1=self.entry.get()
        dictionary = PyDictionary()
        a=dictionary.meaning(word1)
        str1=""
        if a is None:
            messagebox.showerror("Error Message", 'not found')
        else:
            for i in a["Noun"]:
                str1 += str(i) + " , "
            self.label = Label(self.root, wraplength=600, text=str1)
            self.label.place(x=0, y=100)
