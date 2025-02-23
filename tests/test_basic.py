import pytest
from pathlib import Path
from src.main import get_files_in_both_folders_full_path
from src.config import INPUT_DIR

def test_directory_structure():
    """Test that the directory structure is correct"""
    assert INPUT_DIR.exists()
    assert (INPUT_DIR / "youtube_subtitles").exists()
    assert (INPUT_DIR / "pixel_6_translation").exists()

def test_get_files():
    """Test that we can get files from both folders"""
    # Crear directorios y archivos de prueba si no existen
    INPUT_DIR.mkdir(parents=True, exist_ok=True)
    youtube_subtitles_dir = INPUT_DIR / "youtube_subtitles"
    pixel_6_translation_dir = INPUT_DIR / "pixel_6_translation"
    
    youtube_subtitles_dir.mkdir(exist_ok=True)
    pixel_6_translation_dir.mkdir(exist_ok=True)

    # Crear archivos de prueba
    test_file_1 = youtube_subtitles_dir / "test.txt"
    test_file_2 = pixel_6_translation_dir / "test.txt"
    
    test_file_1.touch()
    test_file_2.touch()

    # Obtener los archivos
    files = get_files_in_both_folders_full_path()
    
    # Verificar que se encontró el archivo de prueba
    assert len(files) == 1
    assert files[0][0] == "test.txt"
    assert str(files[0][1]) == str(test_file_1)
    assert str(files[0][2]) == str(test_file_2) 