import random
import math
from simpleai.search import SearchProblem, hill_climbing, beam, hill_climbing_random_restarts, hill_climbing_stochastic, simulated_annealing
from simpleai.search.viewers import ConsoleViewer, WebViewer, BaseViewer

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

border_city = {
                'san francisco': ['chicago', 'los angeles'],
                'chicago': ['san francisco', 'los angeles', 'mexico city', 'atlanta', 'montreal'],
                'montreal': ['chicago', 'washington', 'new york'],
                'new york': ['montreal', 'washington', 'madrid', 'london'],
                'atlanta': ['chicago', 'washington', 'miami'],
                'washington': ['montreal', 'new york', 'atlanta', 'miami'],
                'los angeles': ['san francisco', 'chicago', 'mexico city'],
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
                'tokyo': ['seoul', 'shanghai', 'osaka'],
                'shanghai': ['beijing', 'seoul', 'tokyo', 'taipei', 'hong kong'],
                'osaka': ['tokyo', 'taipei'],
                'taipei': ['osaka', 'shanghai', 'hong kong', 'manila'],
                'hong kong': ['shanghai', 'taipei', 'manila', 'bangkok'],
                'bangkok': ['kolkata', 'chennai', 'hong kong', 'ho chi minh city', 'jakarta'],
                'ho chi minh city': ['hong kong', 'manila', 'jakarta', 'bangkok'],
                'manila': ['taipei', 'hong kong', 'ho chi minh city', 'sydney'],
                'jakarta': ['chennai', 'bangkok', 'ho chi minh city', 'sydney'],
                'sydney': ['jakarta', 'manila'],
}

#Infecciones = {
                #'san francisco': 1,
                #'chicago': 1,
                #'montreal': 1,
                #'new york': 1,
                #'atlanta': 1,
                #'washington': 1,
                #'los angeles': 1,
                #'mexico city': 0,
                #'miami': 0,
                #'bogota': 0,
                #'lima': 0,
                #'santiago': 0,
                #'sao paulo': 0,
                #'buenos aires': 0,
                #'madrid': 0,
                #'london': 0,
                #'paris': 6,
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
                #'seoul': 0,
                #'tokyo': 0,
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

#Infecciones = {
    #'cairo': 1,
    #'riyadh': 3,
    #'seoul': 14,
    #'moscow': 2,
    #'chicago': 17,
    #'london': 2,
#}

VIRUS = {}

INITIAL = 'miami'

class pandemicProblem(SearchProblem):
    def actions(self, state):
        estado = state.split(",")
        acciones = []

        for cit in border_city[estado[0]]:
                acciones.append(cit)
        return (acciones)

    def result(self, state, action):
        state
        state = action
        return state

    def value(self, state):
        maldad = 0
        OrigenX = city[state][0]
        OrigenY = city[state][1]

        for ciudad in VIRUS:
            if VIRUS[ciudad] != 0:
                maldad += math.sqrt(abs(OrigenX - city[ciudad][0]) +
                abs(OrigenY - city[ciudad][1])) * VIRUS[ciudad]
        return -maldad

    def generate_random_state(self):
        listaRandom = []
        for ciudad in city:
            listaRandom.append(ciudad)
        resultado = random.choice(listaRandom)
        return resultado


def resolver(metodo_busqueda, infecciones):
    visor = BaseViewer()
    #visor = WebViewer()
    #visor = ConsoleViewer()
    global VIRUS
    VIRUS = infecciones
    INITIAL = 'san francisco'
    if metodo_busqueda == 'hill_climbing':
        result = eval(metodo_busqueda + '(pandemicProblem(INITIAL), iterations_limit=1000, viewer=visor)')
    elif metodo_busqueda == 'beam':
            result = eval(metodo_busqueda + '(pandemicProblem(), beam_size=20, iterations_limit=1000, viewer=visor)')
    elif metodo_busqueda == 'hill_climbing_random_restarts':
        result = eval(metodo_busqueda + '(pandemicProblem(), restarts_limit=100, iterations_limit=1000, viewer=visor)')
    print visor.stats
    return result

# comandos para pruebas
#visor = BaseViewer()
#visor = WebViewer()
#visor = ConsoleViewer()
#result = hill_climbing_random_restarts(pandemicProblem(), 1000, visor)
#result = hill_climbing(pandemicProblem(INITIAL), viewer=visor)
#result = hill_climbing_stochastic(pandemicProblem('santiago'), viewer=visor)
#result = beam(pandemicProblem(), beam_size=5, viewer=visor)
#result = simulated_annealing(pandemicProblem(INITIAL), iterations_limit=20, viewer=visor)

#print visor.stats