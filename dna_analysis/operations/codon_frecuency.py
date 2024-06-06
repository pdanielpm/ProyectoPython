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


# Función para extraer la secuencia de un archivo FASTA
def extraer_secuencia_fasta(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''
        for line in lines:
            if line.startswith('>'):  # Ignorar líneas de descripción
                continue
            sequence += line.strip()
        return sequence

# Función para contar la frecuencia de cada codón en la secuencia de ADN
def contar_codones(secuencia):
    codones = defaultdict(int)
    total_codones = 0

    for i in range(0, len(secuencia) - 2, 3):
        codon = secuencia[i:i+3]
        if len(codon) == 3:  # Asegurarse de que sea un codón completo
            codones[codon] += 1
            total_codones += 1

    return codones, total_codones

# Función para calcular la frecuencia de cada codón
def calcular_frecuencias(codones, total_codones):
    frecuencias = {codon: count / total_codones for codon, count in codones.items()}
    return frecuencias
