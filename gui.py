from pathlib import Path
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, ttk, Label, StringVar, IntVar, OptionMenu, Listbox, messagebox, BooleanVar
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
currentFrame = 1
father_genre = "General"

"""
! Frame Numbers
? 0 = Loading Page
? 1 = Films
? 2 = Film Register
? 3 = Genres
? 4 = Genre Register  
"""

root = Tk()
root.title(title)
root.config(width=width, height=height)

frame0 = Frame(root)
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
frame4 = Frame(root)

#! GLOBAL VARIABLES
films_list = []
genres_list = []

films_list = libs.getFilms(messagebox)
genres_list = libs.getGenres(messagebox)

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

# CAMBIO DE PESTAÑA

def buttonFilm():
    global currentFrame
    currentFrame = 1
    switchFrame(currentFrame)

def buttonFilmRegister():
    global currentFrame
    currentFrame = 2
    switchFrame(currentFrame)

def buttonGenre():
    global currentFrame
    currentFrame = 3
    switchFrame(currentFrame)

def buttonGenreRegister():
    global currentFrame
    currentFrame = 4
    switchFrame(currentFrame)

#* FRAMES        
"""
! LOADING FRAME
"""
frame0.config(width=width, height=height)

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
frame1.config(width=width, height=height)

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
label_ventana.place(x = 20, y = 8)

#line_v
line_v_src = PhotoImage(file = f"{assets_path}/line_v.png")
label_v_logo = Label(frame1, image = line_v_src)
label_v_logo.place(x = 160, y = 0)

#line_h
line_h_src = PhotoImage(file = f"{assets_path}/line_h.png")
label_h_logo = Label(frame1, image = line_h_src)
label_h_logo.place(x = 0, y = 50)

#botones ventanas
button_1 = Button(frame1, text="Añadir Película", font=("Inter", 15), width=13, height=1, command=buttonFilmRegister)
button_1.place(x = 5, y = 60)
button_2 = Button(frame1, text="Ver Géneros", font=("Inter", 15), width=13, height=1, command=buttonGenre)
button_2.place(x = 5, y = 110)
button_3 = Button(frame1, text="Añadir Género", font=("Inter", 15), width=13, height=1, command=buttonGenreRegister)
button_3.place(x = 5, y = 160)
 

#texto búsqueda de películas
label_ventana = Label(frame1, text="Búsqueda de películas:", font=("Inter", 30))
label_ventana.place(x = 190, y = 30)

#! Búsqueda
query = StringVar()
score = IntVar();score.set(1)
filter = StringVar();filter.set("Filtros")
genre = StringVar();genre.set("Géneros")

result_films_list = []
searched_films = StringVar(value=result_films_list)

#for the first exc and cpu optimization, prevent loop
tempQuery = "first exc"
tempScore = 0
def search(*args):
    global tempQuery
    global films_list
    global result_films_list

    if (score.get() != 0): pass
    elif (tempQuery == query.get()): return

    searched_films_list = libs.search_film(films_list, genres_list, filter.get(), query.get(), genre.get(), score.get())
    tempQuery = query.get()
    
    if len(searched_films_list) < 1: pass#print("vacío")
    if len(result_films_list) > 0: result_films_list = []

    for i in range(len(searched_films_list)):    
        result_films_list.append(f"{i + 1}.- {searched_films_list[i][0]}, {searched_films_list[i][1]}, {searched_films_list[i][2]}, {searched_films_list[i][3]}, {searched_films_list[i][4]}.")

    searched_films.set(result_films_list)
    #print(filter.get(), query.get(), genre.get(), score.get())

#! OnInit
search()

#entry film
entry_film = Entry(frame1, textvariable=query , bd=4, font=("Inter"), justify="left", width=50)
entry_film.place(x = 190, y = 100)
query.trace("w", search)

#films
list_box = Listbox(frame1, listvariable=searched_films)
print(searched_films.get())
list_box.place(x = 190, y = 165, relwidth=0.575, relheight=0.5)

#texto filtro
label_filter = Label(frame1, text="Buscar por:", font=("Inter", 15), justify="center")
label_filter.place(x = 660, y = 165)

#option menu score
score_options = [1, 2, 3, 4 , 5]
op_menu_score = OptionMenu(frame1, score, *(score_options))
score.trace("w", search)

#option menu genre 
#? Map genres
genres = []
for i in range(len(genres_list)):
    if (genres_list[i][0] not in genres):
        genres.append(genres_list[i][0])
    elif (genres_list[i][1] not in genres):
        genres.append(genres_list[i][1])


def mapGenre1():
    global op_menu_genre, genre, genres 
    genres_local = []
    for i in range(len(genres_list)):
        if (genres_list[i][0] not in genres_local):
            genres_local.append(genres_list[i][0])
        elif (genres_list[i][1] not in genres_local):
            genres_local.append(genres_list[i][1])
    op_menu_genre.place_forget()
    op_menu_genre = OptionMenu(frame1, genre, *(genres_local))
    if(op_menu_genre.winfo_ismapped()):
        genre.set("Géneros")
        op_menu_genre.place(x = 660, y = 300)
op_menu_genre = OptionMenu(frame1, genre, *(genres))
genre.trace("w", search)


filter_options = ["Nombre o Director", "Género", "Puntuación"]
def onChangeFilter(value):
    if (value == "filtro"):
        return
    else:
        if (value in filter_options and op_menu_genre.winfo_ismapped() and value != "Género"):
            op_menu_genre.place_forget()
        elif (value == "Género"):
            genre.set("Géneros")
            op_menu_genre.place(x = 660, y = 300)
        if (value in filter_options and op_menu_score.winfo_ismapped() and value != "Puntuación"):
            op_menu_score.place_forget()
        elif (value == "Puntuación"):
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
frame2.config(width=width, height=height)

# bg
label_bg_2 = Label(frame2, image=bg_src)
label_bg_2.place(x=0, y=0)

# logo
label_logo_min_2 = Label(frame2, image=logo_min_src)
label_logo_min_2.place(x=0, y=415)

# text window
label_window_2 = Label(frame2, text="Ventanas:", font=("Inter", 20))
label_window_2.place(x=20, y=8)

# line_v
label_v_logo_2 = Label(frame2, image=line_v_src)
label_v_logo_2.place(x=160, y=0)

# line_h
label_h_logo_2 = Label(frame2, image=line_h_src)
label_h_logo_2.place(x=0, y=50)

# window buttons
button_1 = Button(frame2, text="Buscar Película", font=(
    "Inter", 15), width=13, height=1, command=buttonFilm)
button_1.place(x=5, y=60)
button_2 = Button(frame2, text="Ver Géneros", font=(
    "Inter", 15), width=13, height=1, command=buttonGenre)
button_2.place(x=5, y=110)
button_3 = Button(frame2, text="Añadir Género", font=(
    "Inter", 15), width=13, height=1, command=buttonGenreRegister)
button_3.place(x=5, y=160)

# text film register
label_register_2 = Label(frame2, text="Registro de película:", font=("Inter", 30))
label_register_2.place(x=190, y=30)

#!Variables
film_name_2 = StringVar()
director_name_2 = StringVar()
genre_2 = StringVar();genre_2.set("Géneros")
year_2 = IntVar()
score_2 = IntVar();score_2.set(1)

genres_2 = []


# text film name
label_film_2 = Label(frame2, text="Nombre de película:", font=("Inter", 15))
label_film_2.place(x=190, y=125)
# entry film name 
entry_film_2 = Entry(frame2, textvariable=film_name_2 , bd=4, font=("Inter"), justify="center", width=25)
entry_film_2.place(x=450, y=125)

# text director name
label_director_2 = Label(frame2, text="Nombre del director:", font=("Inter", 15))
label_director_2.place(x=190, y=175)
# entry director name
entry_director_2 = Entry(frame2, textvariable=director_name_2 , bd=4, font=("Inter"), justify="center", width=25)
entry_director_2.place(x=450, y=175)

# text genre
label_genre_2 = Label(frame2, text="Género:", font=("Inter", 15))
label_genre_2.place(x=190, y=225)

temp_genres_2 = []
for i in range(len(genres_list)):
    if (genres_list[i][0] not in temp_genres_2):
        temp_genres_2.append(genres_list[i][0])
    if (genres_list[i][1] not in temp_genres_2 and genres_list[i][1] != father_genre):
        temp_genres_2.append(genres_list[i][1])
op_menu_genre_2 = OptionMenu(frame2, genre_2, *(temp_genres_2))
op_menu_genre_2.place(x = 540, y = 225)

#? Map genres
def mapGenre2():
    global genres_list, op_menu_genre_2, genre_2
    genres_local = []
    for i in range(len(genres_list)):
        #if for just see genres (NOT GENERAL)
        if(genres_list[i][0] not in genres_local):
            genres_local.append(genres_list[i][0])
        if (genres_list[i][1] not in genres_local and genres_list[i][1] != father_genre):
            genres_local.append(genres_list[i][1])

    op_menu_genre_2.place_forget()
    op_menu_genre_2 = OptionMenu(frame2, genre_2, *(genres_local))
    op_menu_genre_2.place(x = 540, y = 225)


# text year
label_year_2 = Label(frame2, text="Año:", font=("Inter", 15))
label_year_2.place(x=190, y=275)
#entry year
entry_year_2 = Entry(frame2, textvariable=year_2 , bd=4, font=("Inter"), justify="center", width=12)
entry_year_2.place(x=530, y=275)
once = True

def yearLength(*args):
    global once
    # validate just numbers
    if (not entry_year_2.get().isnumeric()):
        entry_year_2.delete(len(entry_year_2.get()) - 1, len(entry_year_2.get()))
    elif (once):
        entry_year_2.delete(0, 1)
        once = False
    elif len(entry_year_2.get()) > 4:
        entry_year_2.delete(4, 5)

    if (entry_year_2.get() == ""): pass
    elif (len(entry_year_2.get()) == 4 and not libs.validate_year(year_2.get())): 
        messagebox.showerror("Dato inválido", f"El año debe estar entre 1895 y {libs.getYear()}")
year_2.trace("w", yearLength)

# text score
label_score_2 = Label(frame2, text="Valoración:", font=("Inter", 15))
label_score_2.place(x=190, y=325)
#option menu score 1
score_options_2 = [1, 2, 3, 4 , 5]
op_menu_score_2 = OptionMenu(frame2, score_2, *(score_options_2))
op_menu_score_2.place(x = 560, y = 325)

# On Press Button Add Film
def buttonAddFilm():
    global films_list, genres_list, film_name_2, director_name_2, genre_2, year_2, score_2 
    res = libs.add_film(films_list.copy(), genres_list.copy(), film_name_2.get(), director_name_2.get(), genre_2.get(), year_2.get(), score_2.get())
    if (type(res) == tuple):
        messagebox.showerror("Error", res[1])
    else:
        films_list = res
        messagebox.showinfo("Mensaje", "La película se ha agregado correctamente.")

    # for update data in Search Films Frame
    search()
    libs.save_files(films_list, genres_list)
    


#add film
button_add_film_2 = Button(frame2, text="Agregar película", font=("Inter", 15), width=13, height=1, command=buttonAddFilm)
button_add_film_2.place(x=510, y=398)














"""
! GENRES FRAME
"""
#frame3
frame3.config(width=width, height=height)

# bg
label_bg_3 = Label(frame3, image=bg_src)
label_bg_3.place(x=0, y=0)

# logo
label_logo_min_3 = Label(frame3, image=logo_min_src)
label_logo_min_3.place(x=0, y=415)

# text window
label_window_3 = Label(frame3, text="Ventanas:", font=("Inter", 20))
label_window_3.place(x=20, y=8)

# line_v
label_v_logo_3 = Label(frame3, image=line_v_src)
label_v_logo_3.place(x=160, y=0)

# line_h
label_h_logo_3= Label(frame3, image=line_h_src)
label_h_logo_3.place(x=0, y=50)

# window buttons
button_1 = Button(frame3, text="Añadir Género", font=(
    "Inter", 15), width=13, height=1, command=buttonGenreRegister)
button_1.place(x=5, y=60)
button_2 = Button(frame3, text="Buscar Pélicula", font=(
    "Inter", 15), width=13, height=1, command=buttonFilm)
button_2.place(x=5, y=110)
button_3 = Button(frame3, text="Añadir Pélicula", font=(
    "Inter", 15), width=13, height=1, command=buttonFilmRegister)
button_3.place(x=5, y=160)

# text film register
label_register_3 = Label(frame3, text="Géneros:", font=("Inter", 30))
label_register_3.place(x=190, y=30)

tree_genres_3 = ttk.Treeview(frame3, show="tree")
tree_genres_3.place(x = 190, relwidth=0.6, relheight=0.6, rely=0.22)

def mapTreeView():
    dicc = {}
    item_father = tree_genres_3.insert('', 'end', text=father_genre, open=True)
    for g in genres_list:
        if(g[1] not in dicc.keys()):
            dicc[g[1]] = []
            for j in genres_list:
                if (j[1] == g[1] and j[0] not in dicc[g[1]]):
                    if (g[1] in dicc["General"] and libs.getSubGenre(genres_list, g[1])):
                        dicc["General"].remove(g[1])
                    dicc[g[1]].append(j[0])

    for key in dicc:
        if(key == father_genre):
            for genre in dicc[key]:
                item = tree_genres_3.insert(item_father, 'end', text=genre, open=True)
        else:
            item = tree_genres_3.insert(item_father, 'end', text=key, open=True)
            for genre in dicc[key]:
                tree_genres_3.insert(item, 'end', text=genre)
mapTreeView()

def deleteTreeView():
    global tree_genres_3
    for item in tree_genres_3.get_children():
        tree_genres_3.delete(item)














"""
! GENRES REGISTER FRAME
"""
#frame4
frame4.config(width=width, height=height)


# bg
label_bg_4 = Label(frame4, image=bg_src)
label_bg_4.place(x=0, y=0)

# logo
label_logo_min_4 = Label(frame4, image=logo_min_src)
label_logo_min_4.place(x=0, y=415)

# texto ventana
label_window_4 = Label(frame4, text="Ventanas:", font=("Inter", 20))
label_window_4.place(x=20, y=8)

# line_v
label_v_logo_4 = Label(frame4, image=line_v_src)
label_v_logo_4.place(x=160, y=0)

# line_h
label_h_logo_4= Label(frame4, image=line_h_src)
label_h_logo_4.place(x=0, y=50)

# botones ventanas
button_1 = Button(frame4, text="Ver Géneros", font=(
    "Inter", 15), width=13, height=1, command=buttonGenre)
button_1.place(x=5, y=60)
button_2 = Button(frame4, text="Buscar Pélicula", font=(
    "Inter", 15), width=13, height=1, command=buttonFilm)
button_2.place(x=5, y=110)
button_3 = Button(frame4, text="Añadir Pélicula", font=(
    "Inter", 15), width=13, height=1, command=buttonFilmRegister)
button_3.place(x=5, y=160)

# Text Genre Register
label_register_4 = Label(frame4, text="Registro de Géneros:", font=("Inter", 30))
label_register_4.place(x=190, y=30)

# Variables
genre_4 = StringVar();genre_4.set("Géneros")
sub_genre_name_4 = StringVar()

genres_4 = []

# text genre
label_genre_4 = Label(frame4, text="Genero al que pertenece:", font=("Inter", 15))
label_genre_4.place(x=190, y=125)

temp_genres_4 = []
for i in range(len(genres_list)):
    if (genres_list[i][1] not in temp_genres_4):
        temp_genres_4.append(genres_list[i][1])
    if (genres_list[i][1] == father_genre):
        temp_genres_4.append(genres_list[i][0])
op_menu_genre_4 = OptionMenu(frame4, genre_4, *(temp_genres_4))
op_menu_genre_4.place(x = 550, y = 125)

#? Map genres
def mapGenre4():
    global genres_list, op_menu_genre_4, genre_4
    genres_local = []

    for i in range(len(genres_list)):
        if (genres_list[i][1] not in genres_local):
            genres_local.append(genres_list[i][1])
        if (genres_list[i][1] == father_genre):
            genres_local.append(genres_list[i][0])

    op_menu_genre_4.place_forget()
    op_menu_genre_4 = OptionMenu(frame4, genre_4, *(genres_local))
    op_menu_genre_4.place(x = 550, y = 125)


# texto del subgenre
label_sub_genres_4 = Label(frame4, text="Nombre del sub genero:", font=("Inter", 15))
label_sub_genres_4.place(x=190, y=190)
entry_sub_genres_4 = Entry(frame4, textvariable=sub_genre_name_4 , bd=4, font=("Inter"), justify="center", width=25)
entry_sub_genres_4.place(x=450, y=190)


# Validate if new genre not have numbers
def genreType(*args):
    if(len(entry_sub_genres_4.get()) == 0): pass
    elif (not entry_sub_genres_4.get()[len(entry_sub_genres_4.get()) - 1].isspace()): pass
    elif (entry_sub_genres_4.get()[len(entry_sub_genres_4.get()) - 1] == " "): pass
    elif (not entry_sub_genres_4.get().isalpha()):
        entry_sub_genres_4.delete(len(entry_sub_genres_4.get()) - 1, len(entry_sub_genres_4.get()))
        
sub_genre_name_4.trace("w", genreType)


# On Press Button Add genre
def buttonAddGenres():
    global films_list, genres_list, genre_4, sub_genre_name_4
    res_4 = libs.add_genre(genres_list.copy(), genre_4.get(), sub_genre_name_4.get())
    if (type(res_4) == tuple):
        messagebox.showerror("Error", res_4[1])
    else:
        genres_list = res_4
        messagebox.showinfo("Mensaje", "El genero se ha agregado correctamente.")

    #update Genres in others frames
    mapGenre1()
    mapGenre2()
    mapGenre4()
    deleteTreeView()
    mapTreeView()

#add genre
button_add_genre_4 = Button(frame4, text="Agregar genero", font=("Inter", 15), width=13, height=1, command=buttonAddGenres)
button_add_genre_4.place(x=468, y=272)



def onClosing():
    question = messagebox.askokcancel("Cerrando", "¿Quieres salir del programa?\n todos tus cambios serán guardados.")
    if(question): 
        libs.save_files(films_list, genres_list)
        root.destroy()
   
root.protocol("WM_DELETE_WINDOW", onClosing)


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


def error(name, err):
    messagebox.showerror(name, err)


def main():
    loading(loading_frame, first_frame, loading_time)
    root.geometry(f"{width}x{height}+300-150")
    root.resizable(False,False)
    root.mainloop()
    

if __name__ == "__main__":
    main()