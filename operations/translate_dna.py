from Bio.Seq import Seq
from Bio import SeqIO

def translate_frames(dna_sequence):
    frames = {}
    for i in range(3):
        frames[f"Frame {i+1} (5' to 3')"] = str(dna_sequence[i:].translate())
        frames[f"Frame {i+4} (3' to 5')"] = str(dna_sequence.reverse_complement()[i:].translate())
    return frames

def translate_all_frames(archivo_entrada):
    try:
        for registro in SeqIO.parse(archivo_entrada, "fasta"):
            dna_sequence = registro.seq
            print(f"Secuencia de ADN para {registro.id}:\n{dna_sequence}")
            
            translated_frames = translate_frames(dna_sequence)
            for frame, translation in translated_frames.items():
                print(f"{frame}:\n{translation}\n")
    except FileNotFoundError:
        print(f"Error: Archivo '{archivo_entrada}' no encontrado.")

