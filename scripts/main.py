from ProyectoPython.operations.translation import translate_all_frames

if __name__ == "__main__":
    archivo_entrada = input("Ingresa la ruta al archivo FASTA de entrada: ")
    translate_all_frames(archivo_entrada)
