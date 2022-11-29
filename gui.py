from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk, Label
import time
import threading


#? Global Values
title = "Tkinter Test"
loading_time = 3
loading_frame = 0
first_frame = 1
assets_path = "./assets"
width = 800
height = 480


root = Tk()
root.title(title)
root.config(width=width, height=height)

frame0 = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)


def clearFrames():
    frame0.pack_forget()
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    frame4.pack_forget()



#* FRAMES        
"""
! LOADING FRAME
"""
frame0.config(width=width, height=height)
        
#bg
bg_src = PhotoImage(file = f"{assets_path}/bg.png")
label_bg = Label(frame0, image = bg_src, width=width, height=height)
label_bg.place(x = 0, y = 0)

#logo
logo_src = PhotoImage(file = f"{assets_path}/logo.png")
label_logo = Label(frame0, image = logo_src)
label_logo.place(x = 106, y = 152)

#logo
logo_u_src = PhotoImage(file = f"{assets_path}/logo_u.png")
label_u_logo = Label(frame0, image = logo_u_src)
label_u_logo.place(x = 0, y = 0)



"""
! FILMS FRAME
"""
#tree_view = ttk.Treeview()
#item = tree_view.insert("", tk.END, text="Elemento 1")
#tree_view.insert(item, tk.END, text="Sub-elemento 1")
#tree_view.pack()
frame1.config(bg="white", width=width, height=height)

#bg
bg_src = PhotoImage(file = f"{assets_path}/bg.png")
label_bg = Label(frame1, image = bg_src)
label_bg.place(x = 0, y = 0)
label_bg.pack()

#logo
logo_min_src = PhotoImage(file = f"{assets_path}/logo_min.png")
label_logo_min = Label(frame1, image = logo_min_src)
label_logo_min.place(x = 0, y = 415)

#line_v
line_v_src = PhotoImage(file = f"{assets_path}/line_v.png")
label_v_logo = Label(frame1, image = line_v_src)
label_v_logo.place(x = 160, y = 0)

#line_h
line_h_src = PhotoImage(file = f"{assets_path}/line_h.png")
label_h_logo = Label(frame1, image = line_h_src)
label_h_logo.place(x = 0, y = 50)
    


"""
! FILMS REGISTER FRAME
"""
#frame2



"""
! GENRES FRAME
"""
#frame3



"""
! GENRES REGISTER FRAME
"""
#frame4




"""
? Frame Numbers
0 = Loading Page
1 = Films
2 = Film Register
3 = Genres
4 = Genre Register  
"""
def switchFrame(number):
    clearFrames()
    if (number == 0): 
        frame0.pack(fill='both', expand=1)
    elif (number == 1):
        frame1.pack(fill='both', expand=1)
    elif (number == 2):
        frame2.pack(fill='both', expand=1)
    elif(number == 3):
        frame3.pack(fill='both', expand=1)
    elif(number == 4):
        frame4.pack(fill='both', expand=1)

def waiting(frame, s):
    time.sleep(s)
    switchFrame(frame)

def loading(ff, sf, s):
    #ff = first frame
    #cf = change frame
    #s = seconds
    threading_emails = threading.Thread(target=waiting, args=(sf, s))
    threading_emails.start()
    switchFrame(ff)


def main():
    loading(loading_frame, first_frame, loading_time)
    root.mainloop()
    

if __name__ == "__main__":
    main()