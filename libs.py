def open_file(path):
    with open(path, "r", encoding = "utf-8") as file:
        text = file.read().splitlines()
        l1 = []
        for line in text:
            l2 = []
            text1 = line.split(",")
            for item in text1:
                try:
                    l2.append(int(item))
                except ValueError:
                    l2.append(item.replace('"', '').strip())
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
    return films_list.copy()

def getGenres():
    global genres_list
    return genres_list.copy()

def getSuperGenre(genre):
    for local_genre in genres_list.copy():
        if(local_genre[0] == genre):
            return local_genre[1]

def validate_genre(genre):
    global genres_list
    for i in range(len(genres_list)):
        if genres_list[i][0] == genre:
            return False
    return True

def validate_year(year): 
    if year >= 1895:
        return False
    return True

def validate_score(score):
    if (score < 1) or (score > 5):
        return True
    return False

def validate_repeat_film(name, director):
    global films_list
    for i in range (len(films_list)):
        if (films_list[i][0] == name) and (films_list[i][1] == director):
            return True
    return False

def validate_super_genre(super_genre):
    global genres_list
    for i in range(len(genres_list)):
        if genres_list[i][1] == super_genre:
            return False
    return True

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

def search_per_name_or_director(query):
    results = []
    for film in films_list.copy():
        if(film[0].lower().find(query.lower()) != -1 or film[1].lower().find(query.lower()) != -1):
            results.append(film)
    return results

def search_per_genre(genre):
    results = []
    genres = []
    for local_genre in genres_list.copy():
        if(local_genre[0] not in genres):
            genres.append(local_genre[0])
        elif(local_genre[1] not in genres):
            genres.append(local_genre[1])

    for film in films_list.copy():
        if(genre == "General"):
            if(film[2] == genre):
                results.append(film)
        else:
            if(film[2] == genre or film[2] == getSuperGenre(genre)):
                results.append(film)
    return results

def search_per_score(score):
    global films_list
    results = []

    for film in films_list.copy():
        if(score == film[4]):
            results.append(film)

    return results

def search_film(filter, query, genre, score):
    global films_list
    result = []

    if filter == "Nombre o Director":
        result.append(search_per_name_or_director(query))
    elif filter == "Género":
        result.append(search_per_genre(genre))
    elif filter == "Puntuación":
        result.append(search_per_score(score))
    try: return result[0]
    except: return films_list.copy()


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