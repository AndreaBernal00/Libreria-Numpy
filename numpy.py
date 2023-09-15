import numpy as np

candidatos = 30
votantes = 5000

matriz_votos = np.zeros((candidatos, votantes), dtype=int)

for votante in range(votantes):
    candidato_elegido = np.random.randint(0, candidatos)
    matriz_votos[candidato_elegido][votante] = 1

sumas_filas = np.sum(matriz_votos, axis=1)

indice_orden = np.argsort(sumas_filas)[::-1]

for i, indice in enumerate(indice_orden):
    candidato = indice + 1
    suma = sumas_filas[indice]
    print(f"Posición {i + 1}: Candidato {candidato} con {suma} votos")
