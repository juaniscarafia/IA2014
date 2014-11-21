from simpleai.search import CspProblem, backtrack, min_conflicts, MOST_CONSTRAINED_VARIABLE, LEAST_CONSTRAINING_VALUE, HIGHEST_DEGREE_VARIABLE

piezas = ['reina', 'rey', 'alfil1', 'alfil2', 'caballo1', 'caballo2', 'torre1', 'torre2']
casilleros = [(columna, fila) for columna in range(1,9) for fila in range(1,9)]
dominios = dict((pieza, casilleros)
                 for pieza in piezas)

def diferentes(variables, valores):
    valor1,valor2 = valores
    return not valor1 == valor2

def restriccion_alfiles(variables, valores):
    columna1, fila1 = valores[0]
    columna2, fila2 = valores[1]

    return abs(columna1 - columna2) != abs(fila1 - fila2)

def restriccion_torres(variables, valores):

    columna1, fila1 = valores[0]
    columna2, fila2 = valores[1]

    return (columna1 != columna2) and (fila1 != fila2)

def restriccion_reina(variables, valores):

    columna1, fila1 = valores[0]
    columna2, fila2 = valores[1]

    diagonal = abs(columna1 - columna2) != abs(fila1 - fila2)
    lineaRecta = (columna1 != columna2) and (fila1 != fila2)

    return diagonal and lineaRecta

def restriccion_caballos(variables, valores):

    columna1, fila1 = valores[0]
    columna2, fila2 = valores[1]

    distanciaColumna = abs(columna1 - columna2)
    distanciaFila = abs(fila1 - fila2)
    distanciaTotal = distanciaColumna + distanciaFila

    return not (distanciaTotal == 3) and (distanciaColumna != 0) and (distanciaFila != 0)


def restriccion_rey(variables, valores):

    columna1, fila1 = valores[0]
    columna2, fila2 = valores[1]

    distanciaColumna = abs(columna1 - columna2)
    distanciaFila = abs(fila1 - fila2)

    return not (distanciaColumna == 1) or (distanciaFila == 1)


restricciones = []

for pieza in piezas:
    if pieza != 'reina':
        restriccion= ['reina', pieza]
        restricciones.append((restriccion, restriccion_reina))
    if pieza != 'rey':
        restriccion= ['rey', pieza]
        restricciones.append((restriccion, restriccion_rey))
    if pieza != 'alfil1':
        restriccion= ['alfil1', pieza]
        restricciones.append((restriccion, restriccion_alfiles))
    if pieza != 'alfil2':
        restriccion= ['alfil2', pieza]
        restricciones.append((restriccion, restriccion_alfiles))
    if pieza != 'caballo1':
        restriccion= ['caballo1', pieza]
        restricciones.append((restriccion, restriccion_caballos))
    if pieza != 'caballo2':
        restriccion= ['caballo2', pieza]
        restricciones.append((restriccion, restriccion_caballos))
    if pieza != 'torre1':
        restriccion= ['torre1', pieza]
        restricciones.append((restriccion, restriccion_torres))
    if pieza != 'torre2':
        restriccion= ['torre2', pieza]
        restricciones.append((restriccion, restriccion_torres))

problema = CspProblem(piezas, dominios, restricciones)

def resolver(metodo_busqueda, heuristica_variable, heuristica_valor):
    if metodo_busqueda == 'min_conflicts':
        result = min_conflicts(problema, initial_assignment=None, iterations_limit=1000)
    else:
        result = backtrack(problema, variable_heuristic= heuristica_variable, value_heuristic=heuristica_valor, inference=False)
    return result
