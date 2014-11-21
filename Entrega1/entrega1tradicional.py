from simpleai.search import SearchProblem, breadth_first, depth_first, astar, greedy, limited_depth_first
from simpleai.search.viewers import ConsoleViewer, WebViewer, BaseViewer

import math

#Diccionario de ciudades y posiciones en la imagen
city = {
        'san francisco': [100, 294],
        'chicago': [206, 265],
        'montreal': [288, 261],
        'new york': [352, 271],
        'atlanta': [236, 326],
        'washington': [324, 320],
        'los angeles': [118, 678],
        'mexico city': [193, 406],
        'miami': [289, 392],
        'bogota': [283, 477],
        'lima': [252, 566],
        'santiago': [263, 659],
        'sao paulo': [399, 579],
        'buenos aires': [350, 642],
        'madrid': [493, 303],
        'london': [505, 221],
        'paris': [568, 262],
        'essen': [588, 206],
        'milan': [623, 246],
        'st petersburg': [679, 190],
        'moscow': [726, 246],
        'istanbul': [658, 294],
        'algiers': [586, 350],
        'cairo': [647, 363],
        'baghdad': [718, 337],
        'tehran': [780, 285],
        'delhi': [858, 341],
        'karachi': [797, 363],
        'riyadh': [728, 412],
        'mumbai': [805, 424],
        'kolkata': [916, 359],
        'chennai': [869, 470],
        'lagos': [559, 461],
        'khartoum': [665, 446],
        'kinshasa': [611, 519],
        'johannesburg': [658, 603],
        'beijing': [962, 265],
        'seoul': [1037, 262],
        'tokyo': [1095, 294],
        'shanghai': [969, 323],
        'osaka': [1102, 357],
        'taipei': [1041, 383],
        'hong kong': [976, 394],
        'bangkok': [927, 430],
        'ho chi minh city': [979, 488],
        'manila': [1059, 484],
        'jakarta': [928, 540],
        'sydney': [1108, 653],
}

#Diccionario de ciudades fronterizas
border_city = {
                'san francisco': ['chicago', 'los angeles', 'tokyo', 'manila'],
                'chicago': ['san francisco', 'los angeles', 'mexico city', 'atlanta', 'montreal'],
                'montreal': ['chicago', 'washington', 'new york'],
                'new york': ['montreal', 'washington', 'madrid', 'london'],
                'atlanta': ['chicago', 'washington', 'miami'],
                'washington': ['montreal', 'new york', 'atlanta', 'miami'],
                'los angeles': ['san francisco', 'chicago', 'mexico city', 'sydney'],
                'mexico city': ['los angeles', 'chicago', 'miami', 'bogota', 'lima'],
                'miami': ['mexico city', 'atlanta', 'washington', 'bogota'],
                'bogota': ['miami', 'mexico city', 'lima', 'buenos aires', 'sao paulo'],
                'lima': ['mexico city', 'bogota', 'santiago'],
                'santiago': ['lima'],
                'sao paulo': ['bogota', 'buenos aires', 'madrid', 'lagos'],
                'buenos aires': ['bogota', 'sao paulo'],
                'madrid': ['new york', 'london', 'paris', 'algiers', 'sao paulo'],
                'london': ['new york', 'madrid', 'paris', 'essen'],
                'paris': ['london', 'madrid', 'algiers', 'essen', 'milan'],
                'essen': ['london', 'paris', 'milan', 'st petersburg'],
                'milan': ['paris', 'essen', 'istanbul'],
                'st petersburg': ['essen', 'istanbul', 'moscow'],
                'moscow': ['st petersburg', 'istanbul', 'tehran'],
                'istanbul': ['milan', 'algiers', 'cairo', 'baghdad', 'moscow'],
                'algiers': ['madrid', 'paris', 'istanbul', 'cairo'],
                'cairo': ['algiers', 'istanbul', 'baghdad', 'riyadh'],
                'baghdad': ['cairo', 'istanbul', 'tehran', 'karachi', 'riyadh'],
                'tehran': ['moscow', 'baghdad', 'karachi', 'delhi'],
                'delhi': ['tehran', 'karachi', 'mumbai', 'chennai', 'kolkata'],
                'karachi': ['delhi', 'tehran', 'riyadh', 'mumbai'],
                'riyadh': ['cairo', 'baghdad', 'karachi'],
                'mumbai': ['karachi', 'delhi', 'chennai'],
                'kolkata': ['delhi', 'chennai', 'bangkok', 'hong kong'],
                'chennai': ['mumbai', 'delhi', 'kolkata', 'bangkok', 'jakarta'],
                'lagos': ['sao paulo', 'kinshasa', 'khartoum'],
                'khartoum': ['cairo', 'lagos', 'kinshasa', 'johannesburg'],
                'kinshasa': ['lagos', 'khartoum', 'johannesburg'],
                'johannesburg': ['kinshasa', 'khartoum'],
                'beijing': ['seoul', 'shanghai'],
                'seoul': ['beijing', 'tokyo', 'shanghai'],
                'tokyo': ['seoul', 'shanghai', 'osaka', 'san francisco'],
                'shanghai': ['beijing', 'seoul', 'tokyo', 'taipei', 'hong kong'],
                'osaka': ['tokyo', 'taipei'],
                'taipei': ['osaka', 'shanghai', 'hong kong', 'manila'],
                'hong kong': ['shanghai', 'taipei', 'manila', 'bangkok'],
                'bangkok': ['kolkata', 'chennai', 'hong kong', 'ho chi minh city', 'jakarta'],
                'ho chi minh city': ['hong kong', 'manila', 'jakarta', 'bangkok'],
                'manila': ['taipei', 'hong kong', 'ho chi minh city', 'sydney', 'san francisco'],
                'jakarta': ['chennai', 'bangkok', 'ho chi minh city', 'sydney'],
                'sydney': ['jakarta', 'manila', 'los angeles'],
}

#Diccionario de infecciones para pruebas
#Infecciones = {
                #'los angeles': 1,
                #'tokyo': 3,
                #'seoul': 2,
                #'san francisco': 0,
                #'chicago': 0,
                #'montreal': 0,
                #'new york': 0,
                #'atlanta': 0,
                #'washington': 0,
                #'mexico city': 0,
                #'miami': 0,
                #'bogota': 0,
                #'lima': 0,
                #'santiago': 0,
                #'sao paulo': 0,
                #'buenos aires': 0,
                #'madrid': 0,
                #'london': 0,
                #'paris': 0,
                #'essen': 0,
                #'milan': 0,
                #'st petersburg': 0,
                #'moscow': 0,
                #'istanbul': 0,
                #'algiers': 0,
                #'cairo': 0,
                #'baghdad': 0,
                #'tehran': 0,
                #'delhi': 0,
                #'karachi': 0,
                #'riyadh': 0,
                #'mumbai': 0,
                #'kolkata': 0,
                #'chennai': 0,
                #'lagos': 0,
                #'khartoum': 0,
                #'kinshasa': 0,
                #'johannesburg': 0,
                #'beijing': 0,
                #'shanghai': 0,
                #'osaka': 0,
                #'taipei': 0,
                #'hong kong': 0,
                #'bangkok': 0,
                #'ho chi minh city': 0,
                #'manila': 0,
                #'jakarta': 0,
                #'sydney': 0,
#}

# Diccionario de ciudades sin infecciones
global VIRUS
VIRUS = {}

def dic2tuple(dic):
    a=[]
    for i in dic.keys():
        if (dic[i]>0):
            a.append((i,dic[i]))
    return tuple(a)

def tuple2dic(tup):
    a={}
    for i in tup:
        a[i[0]]=i[1]
    return a


def cantVirus(data):
    virus = 0
    for city in data.keys():
        virus = virus + data[city]
    return virus


def distancia(ciudad1, ciudad2):
    dist = math.sqrt((abs(city[ciudad1][0] - city[ciudad2][0])) ** 2 +
    (abs(city[ciudad1][1] - city[ciudad2][1])) ** 2)
    return round(dist)


class Problem(SearchProblem):
    def is_goal(self, state):
        return len(state[1]) == 0

    def cost(self, state1, action, state2):
        return 1

    def actions(self, state):
        acciones = []
        inf = tuple2dic(state[1])
        #calculo la accion de restar un virus
        if state[0] in inf.keys():
            acciones.append("Restar")
        else:
        #calculo la accion de moverme a alguna ciudad limitrofe
            for cit in border_city[state[0]]:
                acciones.append(cit)
        return (acciones)

    def result(self, state, action):
        inf = tuple2dic(state[1])
        ciu=state[0]
        if action == "Restar":
            inf[ciu] = inf[ciu] - 1
        else:
            ciu = action
        estado = (ciu , dic2tuple(inf))
        return estado

    def heuristic(self, state):
        inf=tuple2dic(state[1])
        ciu=state[0]
        a=0
        for i in inf.values():
        	a=a+i
        for i in inf.keys():
        	a=a+1
        if ciu in inf.keys():
        	a=a-1
        return a


def resolver(metodo_busqueda, ciudad, infecciones):
    #visor = WebViewer()
    visor = BaseViewer()
    #visor = ConsoleViewer()
    numerovirus = cantVirus(infecciones)
    estado = (ciudad,dic2tuple(infecciones))
    if metodo_busqueda == 'limited_depth_first':
        result = limited_depth_first(Problem(estado), depth_limit=10, viewer=visor, graph_search=False)
    else:
        result = eval(metodo_busqueda + '(Problem(estado), viewer=visor, graph_search=True)')
    #print visor.stats
    return result