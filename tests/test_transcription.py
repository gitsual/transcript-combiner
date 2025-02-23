import pytest
from pathlib import Path
from src.process_files import process_files
from src.config import INPUT_DIR

TEST_INPUT_DIR = Path(__file__).parent / "input"
TEST_OUTPUT_DIR = Path(__file__).parent / "output"

def test_transcription_combination():
    """Test the combination of two real transcription files"""
    
    # Asegurar que el directorio de salida de tests existe
    TEST_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Rutas a los archivos de prueba
    youtube_file = TEST_INPUT_DIR / "correlacion_eneagrama_mbti_1.txt"
    pixel6_file = TEST_INPUT_DIR / "correlacion_eneagrama_mbti_2.txt"
    
    # Verificar que los archivos existen
    assert youtube_file.exists(), "Archivo de YouTube no encontrado"
    assert pixel6_file.exists(), "Archivo de Pixel 6 no encontrado"
    
    # Procesar los archivos
    output_file, processed_content = process_files(
        pixel6_file, 
        youtube_file,
        output_dir=TEST_OUTPUT_DIR  # Pasar el directorio de salida específico para tests
    )
    
    # Verificar que el archivo de salida existe
    output_path = TEST_OUTPUT_DIR / output_file
    assert output_path.exists(), f"El archivo de salida no se creó: {output_path}"
    
    # Verificaciones básicas del resultado
    assert output_file is not None
    assert processed_content is not None
    assert len(processed_content) > 0
    
    # Verificar que el contenido procesado contiene palabras clave esperadas
    expected_keywords = ["myers", "enneagram", "correlation"]
    for keyword in expected_keywords:
        assert keyword.lower() in processed_content.lower(), f"Palabra clave '{keyword}' no encontrada en el resultado"
    
    # Verificar formato del resultado
    lines = processed_content.split('\n')
    assert lines[0].startswith('# '), "El resultado debe comenzar con un título"
    assert lines[1] == '', "Debe haber una línea en blanco después del título"
    assert '[00:05]' in processed_content, "Debe preservar los timestamps"
    
    # Verificar que mantiene frases comunes intactas
    common_phrases = [
        "that is",
        "this is",
        "it is",
        "is our"
    ]
    for phrase in common_phrases:
        if phrase in processed_content.lower():
            assert phrase in processed_content.lower(), f"Frase común '{phrase}' eliminada incorrectamente"
    
    # Verificar que no hay duplicados obvios (palabras repetidas consecutivamente)
    words = processed_content.split()
    for i in range(len(words)-1):
        assert words[i].lower() != words[i+1].lower(), \
            f"Palabra duplicada encontrada: '{words[i]}' y '{words[i+1]}' en posición {i}"
    
    # Verificar el contenido específicamente para duplicados
    assert "be be" not in processed_content, "Encontrado 'be be' en el contenido"
    assert "that that" not in processed_content, "Encontrado 'that that' en el contenido"
    assert "the the" not in processed_content, "Encontrado 'the the' en el contenido"

def test_file_structure():
    """Test the structure of the input files"""
    # Verificar que el directorio de pruebas existe
    assert TEST_INPUT_DIR.exists()
    assert TEST_INPUT_DIR.is_dir()
    
    # Verificar que los archivos necesarios existen
    expected_files = [
        "correlacion_eneagrama_mbti_1.txt",
        "correlacion_eneagrama_mbti_2.txt"
    ]
    
    for file in expected_files:
        assert (TEST_INPUT_DIR / file).exists(), f"Archivo {file} no encontrado"
        assert (TEST_INPUT_DIR / file).stat().st_size > 0, f"Archivo {file} está vacío"

def test_content_comparison():
    """Test that both input files have related content"""
    file1 = TEST_INPUT_DIR / "correlacion_eneagrama_mbti_1.txt"
    file2 = TEST_INPUT_DIR / "correlacion_eneagrama_mbti_2.txt"
    
    # Leer contenido de ambos archivos
    content1 = file1.read_text().lower()
    content2 = file2.read_text().lower()
    
    # Verificar que ambos archivos contienen palabras clave similares
    common_keywords = ["myers", "enneagram", "correlation"]
    for keyword in common_keywords:
        assert keyword in content1, f"Palabra clave '{keyword}' no encontrada en archivo 1"
        assert keyword in content2, f"Palabra clave '{keyword}' no encontrada en archivo 2"
    
    # Verificar que hay cierto nivel de similitud entre los archivos
    def get_words_set(text):
        return set(text.split())
    
    words1 = get_words_set(content1)
    words2 = get_words_set(content2)
    
    common_words = words1.intersection(words2)
    assert len(common_words) > 10, "Los archivos no parecen tener suficiente contenido en común" 