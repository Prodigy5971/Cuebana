def add_film(name, director, genre, year, score):
    global films_list
    x1 = validate_genre(genre)
    if x1 == True:
        return print("No se pudo agregar la pelicula, el genero no es valido")
    x2 = validate_year(year)
    if x2 == True:
        return print("No se pudo agregar la película, el año no es valido")
    x3 = validate_score(score)
    if x3 == True:
        return print("No se pudo agregar la pelicula, la valoración no es valida")
    x4 = validate_repeat_film(name, director)
    if x4 == True:
        return  print("La película ya existe")
    film = [name, director, genre, year, score]
    films_list.append(film)
    return print("La película se ha agregado exitosamente") 

def add_genre(name, super_genre):
    global genres_list
    x1 = validate_genre(name)
    if x1 == True:
        print("Nombre de género no válido")
    x2 = validate_super_genre(super_genre)
    if x2 == True:
        print("Nombre de género no válido")
    genre = [name, super_genre]
    genres_list.append(genre) 
    return print("El género  se ha agregado exitosamente")

def search_film(search_base):
    global films_list
    result = []
    if search_per_genre(search_base) not in result:
        result.append(search_per_genre(search_base))
    if search_per_name_or_director(search_base) != (([]) and ([[]])):
        result.append(search_per_name_or_director(search_base))
    if search_per_score(search_base) != (([]) and ([[]])) and ([[], []]):
        result.append(search_per_score(search_base))
    return result

def open_file(paht):
    file = open(path, "w", ecoding = "utf-8")  #No estoy seguro si esta vien escrito path
    #text ←(file.Leer()).Separarlineas()
    l1 = []
    for line in text:
        l2 = []
        text1 = line.split(",")
    for item in text1:
        if type(item) == str:
            # l2.Agregar((item.Reemplazar(‘”’, ’’)).strip())
        else:
            l2.append(item)
    return l1

def save_files (films, genres):
    films_file = open("peliculas.csv", "w")
    films_file.write(films)
    genres_files = open("generos.csv", "w")
    genres_files.write(genres)
    films_file.close()
    genres_files.close()

def main():
    films_list = open_file("peliculas.csv", "r")
    genres_list =  open_file("generos.csv", "r")

    #cuando el programa se cierre ejecutar save_files()
    save_files(films_list, genres_list)