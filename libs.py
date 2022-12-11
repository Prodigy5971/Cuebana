import datetime

def open_file(path, box):
    global error
    try:
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
    except FileNotFoundError:
        box.showerror("Error", f"El archivo \"{path}\" no existe.")



#! paths
films_path = "peliculas.csv"
genres_path = "generos.csv"
    

def getFilms(box):
    return open_file(films_path, box)

def getGenres(box):
    return open_file(genres_path, box)

def getYear():
    today = datetime.datetime.now()
    return today.year 

def isSuperGenre(genres_list, genre):
    for local_genre in genres_list.copy():
        if(local_genre[1] == genre):
            return True
    return False

def getSuperGenre(genres_list, genre):
    for local_genre in genres_list.copy():
        if(local_genre[0] == genre):
            return local_genre[1]

def getSubGenre(genres_list, genre):
    for local_genre in genres_list.copy():
        if(local_genre[1] == genre):
            return local_genre[0]

def validate_genre(genres_list, genre):
    if(genre == "General"): return True
    for i in range(len(genres_list)):
        if genres_list[i][0] == genre:
            return True
    return False

def validate_year(year):
    this_year = getYear()
    if (year <= this_year and year >= 1895):
        return True
    return False

def validate_score(score):
    if (score >= 1 or score <=5 ):
        return True
    return False

def validate_repeat_film(films_list, name, director):
    for i in range(len(films_list)):
        if (films_list[i][0] == name and films_list[i][1] == director):
            return True
    return False

def validate_super_genre(genres_list, super_genre):
    for i in range(len(genres_list)):
        if genres_list[i][1] == super_genre:
            return True
    return False

def add_film(*args):
    #films_list, genres_list, name, director, genre, year, score 
    args_keys = ("films_list", "genres_list", "Nombre de Película", "Nombre del Director", "Género", "Año", "")
    films_list = args[0]; genres_list = args[1]; name = args[2].strip(); director = args[3].strip(); genre = args[4]; year = args[5]; score = args[6]
    #print("genre:", genre, "score:", score)
    for i in range(2, len(args)-2):
        if(type(args[i]) == str and (len(args[i]) == 0 or args[i].isspace())):
            if(args_keys[i] == "Género"):
                return (0, f"Debe seleccionar un\"{args_keys[i]}\".")
            else:
                return (0, f"No se puede ingresar \"{args_keys[i]}\" vacío.")

    if(genre == "Géneros"): return (1, "Debe seleccionar un \"Género\".")
    x1 = validate_genre(genres_list, genre)
    if (not x1): return (1, "No se pudo agregar la película, el género no es valido.")

    x2 = validate_year(year)
    if (not x2): return (2, "No se pudo agregar la película, el año no es valido.")

    x3 = validate_score(score)
    if (not x3): return (3, "No se pudo agregar la película, la valoración no es valida.")

    x4 = validate_repeat_film(films_list, name, director)
    if (x4): return (4, "La película ya existe")

    film = [name, director, genre, year, score]
    films_list.append(film)
    return films_list

def add_genre(*args):
    genres_list = args[0]; super_genre = args[1]; name = args[2].strip()
    args_keys = ("genres_list", "Género Padre", "Sub-Género")

    if(super_genre == "Géneros"): return (1, "Debe seleccionar un \"Género\".")
    for i in range(1, len(args)):
        if(type(args[i]) == str and (len(args[i]) == 0 or args[i].isspace())):
            if(args_keys[i] == "Género Padre"):
                return (0, f"Debe seleccionar un \"{args_keys[i]}\".")
            else:
                return (0, f"No se puede ingresar un \"{args_keys[i]}\" vacío.")

    x1 = validate_genre(genres_list, super_genre)
    if (not x1): return(1, "Género Padre no existente.")

    genre = [name, super_genre]
    genres_list.append(genre) 
    return genres_list


#! SEARCH 
def search_per_name_or_director(films_list, query):
    query = query.strip()
    results = []
    for film in films_list.copy():
        if(film[0].lower().find(query.lower()) != -1 or film[1].lower().find(query.lower()) != -1):
            results.append(film)
    return results

def search_per_genre(films_list, genres_list, genre):
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
            if(isSuperGenre(genres_list, genre)):
                if(film[2] == genre or film[2] == getSubGenre(genres_list, genre)):
                    results.append(film)
            else:
                if(film[2] == genre):
                    results.append(film)
    return results


def search_per_score(films_list, score):
    results = []

    for film in films_list.copy():
        if(score == film[4]):
            results.append(film)
    return results


def search_film(films_list, genres_list, filter, query, genre, score):
    #films_list and genres_list are arguments, not using global value
    result = []
    if filter == "Nombre o Director":
        result.append(search_per_name_or_director(films_list, query))
    elif filter == "Género":
        result.append(search_per_genre(films_list, genres_list, genre))
    elif filter == "Puntuación":
        result.append(search_per_score(films_list, score))
        
    try: return result[0]
    except: return films_list.copy()


def save_files(films, genres):#films_path
    with open(films_path, "w", encoding = "utf-8") as films_file:
        for film in films:
            f = f"\"{film[0]}\", \"{film[1]}\", \"{film[2]}\", {film[3]}, {film[4]}"
            films_file.write(f)
            films_file.write('\n')
    
    with open(genres_path, "w", encoding = "utf-8") as genres_file:
        for genre in genres:
            f = f"\"{genre[0]}\", \"{genre[1]}\""
            genres_file.write(f)
            genres_file.write('\n')