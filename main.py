import os
from src.transcript_processor import combine_transcripts

def ensure_output_directory():
    output_dir = "data/output/processed_transcripts"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

def get_common_files(source_1_path, source_2_path):
    # Obtener archivos de ambas carpetas
    files_1 = set(os.listdir(source_1_path))
    files_2 = set(os.listdir(source_2_path))
    
    # Encontrar archivos que están en ambas carpetas
    files_in_both = files_1.intersection(files_2)
    
    # Crear rutas completas
    files_full_path = [(
        os.path.join(source_1_path, f),
        os.path.join(source_2_path, f)
    ) for f in files_in_both]
    
    return list(files_in_both), files_full_path

def main():
    source_1_path = "data/input/source_1"
    source_2_path = "data/input/source_2"
    output_dir = ensure_output_directory()
    
    print("Transcript Combiner")
    print("====================================\n")
    print("[1]. Combine Versions")
    print("[2]. Update")
    print("[3]. Exit\n")
    
    option = input("Enter an option: ")
    
    if option == "1":
        files_in_both, files_full_path = get_common_files(source_1_path, source_2_path)
        
        if not files_full_path:
            print("No files found to process")
            return
            
        print("\nProcesando archivos...")
        # Leer el contenido del archivo del Pixel para cada par de archivos
        for youtube_path, pixel_path in files_full_path:
            with open(pixel_path, 'r', encoding='utf-8') as f:
                pixel_text = f.read()
            
            filename = os.path.basename(youtube_path)
            output_path = os.path.join(output_dir, filename)
            
            result = combine_transcripts(youtube_path, pixel_text)
            
            # Guardar el resultado
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result)
            
            print(f"Archivo procesado: {filename}")
            
        print("\n¡Proceso completado! Los archivos están en:", output_dir)
            
    elif option == "2":
        print("Función de actualización aún no implementada")
    elif option == "3":
        print("¡Hasta luego!")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main() 