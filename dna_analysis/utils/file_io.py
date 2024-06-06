def read_dna_sequence(file_path):
    """Lee una secuencia de ADN desde un archivo."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def write_dna_sequence(file_path, sequence):
    """Escribe una secuencia de ADN en un archivo."""
    with open(file_path, 'w') as file:
        file.write(sequence)

def extraer_secuencia_fasta(file_path):
    """Extrae una secuencia de ADN de un archivo FASTA."""
    with open(file_path, 'r') as file:
        lines = file.readlines()
        sequence = ''
        for line in lines:
            if line.startswith('>'):  # Ignorar líneas de descripción
                continue
            sequence += line.strip()
        return sequence
