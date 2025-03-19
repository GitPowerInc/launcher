#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 5 13:24:00 2025

@author: V
"""

import customtkinter as t

running=False
work=1500
br=300
left=work


def main():
    win=t.CTk()
    win.geometry("400x500")
    win.title("Porro Modorro")
    win.configure(bg="#1A1B26")
    win.configure(fg_color="#1A1B26")
    return win

def guiu(win):
    global timer,startb,resetb,canva
    canva= t.CTkCanvas(win, width=300,height=300, bg="#1A1B26", highlightthickness=0)
    canva.pack(pady=20)
    timer= t.CTkLabel(canva,text="",font=("Helvetica",45),text_color="white",bg_color="#1A1B26")
    timer.place(x=150, y=150,anchor="center")
    butn= t.CTkFrame(win,fg_color="#1A1B26")
    butn.pack(pady=10, fill="x")
    startb= t.CTkButton(butn,text="Start",command=toggle,fg_color="#565f89", hover_color="#414868")
    startb.pack(pady=10)
    resetb= t.CTkButton(butn,text="Reset",command=reset,fg_color="#565f89", hover_color="#414868")
    resetb.pack(pady=10)
    update()
    cercle()

def cercle():
    r=100
    x,y,xb,yb= 150-r,150-r,150+r,150+r
    canva.create_oval(x,y,xb,yb, outline="#FF6F91", width=5)
def toggle():
    global running
    running=not running
    startb.configure(text="Stop" if running else "Start")
    if running:
        start()

def start():
    global left, running
    if running==True and left>0:
        m=left//60
        s=left%60
        txt='{:02d}:{:02d}'.format(m, s)
        timer.configure(text=txt)
        left-=1
        win.after(1000,start)
    elif left==0:
        running = False
        timer.configure(text="TIMES UP BUDDY")
        startb.configure(text="Start")
        pause()
def pause():
    global left, running
    left=br
    running = True
    start()
def reset():
    global running, left
    running=False
    left=work
    update()
    resetb.configure(text="Start")
def update():
    m=left//60
    s=left%60
    txt='{:02d}:{:02d}'.format(m, s)
    timer.configure(text=txt)

if __name__ == "__main__":
    t.set_appearance_mode("dark")
    t.set_default_color_theme("blue")
    win = main()
    win.configure(fg_color="#1A1B26")
    guiu(win)
    win.mainloop()
