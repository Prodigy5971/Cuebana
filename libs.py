def open_file(path):
    with open(path, "r", encoding = "utf-8") as file:
        text = file.read().splitlines()
        l1 = []
        for line in text:
            l2 = []
            text1 = line.split(",")
            for item in text1:
                if type(item) == str:
                    l2.append(item.replace('"', '').strip())
                else:
                    l2.append(item)
            l1.append(l2)
        return l1


#! paths
films_path = "peliculas.csv"
genres_path = "generos.csv"

films_list = open_file(films_path)
genres_list =  open_file(genres_path)


#beta
def updateData():
    global films_list, genres_list
    films_list = open_file(films_path)
    genres_list =  open_file(genres_path)
    
#for testing
def getFilms():
    global films_list
    return films_list


def validate_genre(genre):
    pass

def validate_year(year):
    pass

def validate_score(score):
    pass

def validate_repeat_film(name, director):
    pass

def validate_super_genre(super_genre):
    pass

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

def search_per_name_or_director(search_base):
    pass

def search_per_genre(genre):
    pass

def search_per_score(search_base):
    pass

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

def open_file(path):
    file = open(path, "w", encoding = "utf-8")
    text = file.read().splitlines() 
    l1 = []
    for line in text:
        l2 = []
        text1 = line.split(",")
    for item in text1:
        if type(item) == str:
            l2.append(item.replace('"', '').strip())
        else:
            l2.append(item)
    return l1

def save_files(films, genres):
    films_file = open(films_path, "w")
    films_file.write(films)
    genres_files = open(genres_path, "w")
    genres_files.write(genres)
    films_file.close()
    genres_files.close()

#not yet done
def onClose():
    #save_files(films_list, genres_list)
    print("cerrado")

