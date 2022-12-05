from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk, Label, StringVar, IntVar, Radiobutton, OptionMenu, Listbox
import time
import threading
import libs


#? Global Values
title = "Tkinter Test"
loading_time = 1
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

#logo
logo_min_src = PhotoImage(file = f"{assets_path}/logo_min.png")
label_logo_min = Label(frame1, image = logo_min_src)
label_logo_min.place(x = 0, y = 415)

#texto ventana
label_ventana = Label(frame1, text="Ventanas:", font=("Inter", 20))
label_ventana.place(x = 20, y = 16)

#line_v
line_v_src = PhotoImage(file = f"{assets_path}/line_v.png")
label_v_logo = Label(frame1, image = line_v_src)
label_v_logo.place(x = 160, y = 0)

#line_h
line_h_src = PhotoImage(file = f"{assets_path}/line_h.png")
label_h_logo = Label(frame1, image = line_h_src)
label_h_logo.place(x = 0, y = 50)

#botones ventanas
button_1 = Button(frame1, text="Añadir Película", font=("Inter", 15), width=13, height=1, command=switchFrame(2))
button_1.place(x = 5, y = 60)
button_2 = Button(frame1, text="Ver Géneros", font=("Inter", 15), width=13, height=1, command=switchFrame(3))
button_2.place(x = 5, y = 110)
button_1 = Button(frame1, text="Añadir Género", font=("Inter", 15), width=13, height=1, command=switchFrame(4))
button_1.place(x = 5, y = 160)
 

#texto búsqueda de películas
label_ventana = Label(frame1, text="Búsqueda de películas:", font=("Inter", 30))
label_ventana.place(x = 190, y = 30)

#! Búsqueda
query = StringVar()
score = IntVar();score.set(1)
filter = StringVar();filter.set("Filtros")
genre = StringVar();genre.set("Géneros")

genres = []

searched_films_list = []
searched_films = StringVar(value=searched_films_list)

#for the first exc and cpu optimization, prevent loop
tempQuery = "first exc"
tempScore = 0
def search(*args):
    global tempQuery
    global searched_films_list
    global genres

    if(score.get() != 0): pass
    elif(tempQuery == query.get()): return

    films_list = libs.search_film(filter.get(), query.get(), genre.get(), score.get())
    tempQuery = query.get()
    
    if len(films_list) < 1: print("vacío")
    if len(searched_films_list) > 0: searched_films_list = []

    for i in range(len(films_list)):    
        searched_films_list.append(f"{i + 1}.- {films_list[i][0]}, {films_list[i][1]}, {films_list[i][2]}, {films_list[i][3]}, {films_list[i][4]}.")

    searched_films.set(searched_films_list)
    print(filter.get(), query.get(), genre.get(), score.get())

#! OnInit
search()

#entry film
entry_film = Entry(frame1, textvariable=query ,bd=4, font=("Inter"), justify="left", width=50)
entry_film.place(x = 190, y = 100)
query.trace("w", search)

#films
list_box = Listbox(frame1, listvariable=searched_films)
print(searched_films.get())
list_box.place(x = 190, y = 165, relwidth=0.575, relheight=0.5)

#texto filtro
label_filtro = Label(frame1, text="Buscar por:", font=("Inter", 15), justify="center")
label_filtro.place(x = 660, y = 165)

#option menu score
score_options = [1, 2, 3, 4 , 5]
op_menu_score = OptionMenu(frame1, score, *(score_options))
score.trace("w", search)

#option menu genre 
#? Map genres
genres_list = libs.getGenres()
for i in range(len(genres_list)):
    if(genres_list[i][0] not in genres):
        genres.append(genres_list[i][0])
    elif(genres_list[i][1] not in genres):
        genres.append(genres_list[i][1])

op_menu_genre = OptionMenu(frame1, genre, *(genres))
genre.trace("w", search)

filter_options = ["Nombre o Director", "Género", "Puntuación"]
def onChangeFilter(value):
    if(value == "filtro"):
        return
    else:
        if(value in filter_options and op_menu_genre.winfo_ismapped()):
            op_menu_genre.place_forget()
        elif(value == "Género"):
            genre.set("Géneros")
            op_menu_genre.place(x = 660, y = 300)
        if(value in filter_options and op_menu_score.winfo_ismapped()):
            op_menu_score.place_forget()
        elif(value == "Puntuación"):
            score.set(1)
            op_menu_score.place(x = 660, y = 300)

#option menu filter
op_menu_filter = OptionMenu(frame1, filter, *(filter_options), command=onChangeFilter)
op_menu_filter.place(x = 660, y = 220)
filter.trace("w", search)





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
    root.geometry(f"{width}x{height}+300-150")
    #root.protocol("WM_DELETE_WINDOW", libs.onClose())
    root.mainloop()
    

if __name__ == "__main__":
    main()