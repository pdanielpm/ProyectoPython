import sys 
import argparse
sys.path.append("C:/Users/pdmpe/Desktop/ProyectoPython/dna_analysis/")
from dna_analysis.operations.translate_dna import translate_all_frames
from dna_analysis.operations.codon_frecuency import extraer_secuencia_fasta, contar_codones, calcular_frecuencias

def main():
    parser = argparse.ArgumentParser(description='Traducir todas las posibles lecturas de un archivo FASTA de ADN.')
    parser.add_argument('archivo_entrada', type=str, help='Ruta al archivo FASTA de entrada.')
    
    args = parser.parse_args()
    
    translate_all_frames(args.archivo_entrada)

    parser = argparse.ArgumentParser(
        description="Calcular la frecuencia de codones en una secuencia de ADN en formato FASTA.")
    parser.add_argument("file", help="Archivo en formato FASTA que contiene la secuencia de ADN.")

    args = parser.parse_args()

    secuencia = extraer_secuencia_fasta(args.file)
    codones, total_codones = contar_codones(secuencia)
    frecuencias = calcular_frecuencias(codones, total_codones)

    # Imprimir la frecuencia de cada codón
    for codon, freq in frecuencias.items():
        print(f"Codón: {codon}, Frecuencia: {freq:.4f}")


if __name__ == "__main__":
    main()