def validar_dna_sequence(secuencia):
    """Valida si una secuencia contiene solo caracteres de ADN (A, T, C, G)."""
    return all(nucleotido in "ATCG" for nucleotido in secuencia)

def validar_fasta(file_path):
    """Valida si un archivo tiene formato FASTA."""
    with open(file_path, 'r') as file:
        primera_linea = file.readline().strip()
        return primera_linea.startswith('>')