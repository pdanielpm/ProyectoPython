'''
NAME
CODON_FRECUENCY

VERSION
1.0

AUTHOR
Pineda Martinez Pedro Daniel & Palafox Collado Dara Jahzeel

DESCRIPTION

Este programa calcula la frecuencia de cada codón en una secuencia de ADN.

CATEGORY

Bioinformática

USAGE
    
      % python codon_frecuency.py archivo.txt
    

ARGUMENTS

archivo: Archivo que contiene la secuencia de ADN.


METHOD

1. El progama lee la secuencia de ADN desde un archivo de texto.
2. Despues cuenta la frecuencia de cada codón en la secuencia.
3. Se calcula la frecuencia de cada codón. Se divide el número de veces que aparece un codón entre el total de codones.
4. Imprimir la frecuencia de cada codón.

SEE ALSO


        
'''

# ===========================================================================
# =                            imports
# ===========================================================================

import argparse
from collections import defaultdict

# ===========================================================================
# =                            functions
# ===========================================================================

# Esta función lee una secuencia de ADN desde un archivo de texto.


def leer_secuencia(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip().replace('\n', '')

# Esta función cuenta la frecuencia de cada codón en la secuencia de ADN.


def contar_codones(secuencia):
    codones = defaultdict(int)
    total_codones = 0

    for i in range(0, len(secuencia) - 2, 3):
        codon = secuencia[i:i+3]
        if len(codon) == 3:  # Asegurarse de que sea un codón completo
            codones[codon] += 1
            total_codones += 1

    return codones, total_codones

# Esta función calcula la frecuencia de cada codón.


def calcular_frecuencias(codones, total_codones):
    frecuencias = {codon: count /
                   total_codones for codon, count in codones.items()}
    return frecuencias

# ===========================================================================
# =                            main
# ===========================================================================


def main():
    # Parsear argumentos de línea de comandos
    parser = argparse.ArgumentParser(
        description="Calcular la frecuencia de codones en una secuencia de ADN.")
    parser.add_argument(
        "file", help="Archivo que contiene la secuencia de ADN.")

    args = parser.parse_args()

    secuencia = leer_secuencia(args.file)
    codones, total_codones = contar_codones(secuencia)
    frecuencias = calcular_frecuencias(codones, total_codones)

    # Imprimir la frecuencia de cada codón
    for codon, freq in frecuencias.items():
        print(f"Codón: {codon}, Frecuencia: {freq:.4f}")


# Llamar a la función main
if __name__ == "__main__":
    main()
