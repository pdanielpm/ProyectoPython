import sys 
import argparse
sys.path.append("C:/Users/pdmpe/Desktop/ProyectoPython/dna_analysis/")
from dna_analysis.utils.file_io import extraer_secuencia_fasta
from dna_analysis.utils.validators import validar_dna_sequence, validar_fasta
from dna_analysis.operations.codon_frecuency import extraer_secuencia_fasta, contar_codones, calcular_frecuencias
from dna_analysis.operations.translate_dna import translate_all_frames


def main():
    parser = argparse.ArgumentParser(description="Análisis de secuencias de ADN.")
    parser.add_argument('file', type=str, help="Ruta al archivo de secuencia de ADN en formato FASTA.")
    args = parser.parse_args()

    # Validar archivo FASTA
    if not validar_fasta(args.file):
        print(f"Error: El archivo '{args.file}' no tiene formato FASTA válido.")
        return

    # Extraer secuencia de ADN
    secuencia = extraer_secuencia_fasta(args.file)
    print(f"Secuencia de ADN extraída:\n{secuencia}\n")

    # Validar secuencia de ADN
    if not validar_dna_sequence(secuencia):
        print(f"Error: La secuencia de ADN '{secuencia}' contiene caracteres no válidos.")
        return

    # Contar y calcular frecuencias de codones
    codones, total_codones = contar_codones(secuencia)
    frecuencias = calcular_frecuencias(codones, total_codones)

    print("Frecuencia de codones:")
    for codon, frecuencia in frecuencias.items():
        print(f"{codon}: {frecuencia:.2%}")

    # Traducir marcos de lectura
    translate_all_frames(args.file)

if __name__ == "__main__":
    main()