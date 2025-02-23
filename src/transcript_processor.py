import re
import nltk
from typing import List
from pathlib import Path
from langdetect import detect

# Mapeo de códigos de idioma a códigos NLTK
LANG_MAP = {
    'es': 'spanish',
    'en': 'english',
    'fr': 'french',
    'de': 'german',
    'it': 'italian',
    'pt': 'portuguese',
    # Añadir más idiomas según sea necesario
}

def detect_language(text: str) -> str:
    """
    Detecta el idioma del texto y devuelve el código de idioma NLTK correspondiente.
    Por defecto retorna 'english' si no se puede detectar.
    """
    try:
        lang_code = detect(text)
        return LANG_MAP.get(lang_code, 'english')
    except:
        return 'english'

def ensure_nltk_resources(language: str):
    """
    Asegura que los recursos necesarios de NLTK estén disponibles.
    """
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')

def extract_timestamp(text: str) -> str:
    """Extrae el timestamp del texto."""
    timestamp_match = re.search(r'\[(\d{2}:\d{2})\]', text)
    return f"[{timestamp_match.group(1)}]" if timestamp_match else "[00:00]"

def split_into_sentences(text: str) -> List[str]:
    """Divide el texto en oraciones usando puntuación."""
    # Primero preservamos los puntos en abreviaturas comunes
    abbreviations = ['Mr.', 'Mrs.', 'Dr.', 'Ph.D.', 'etc.', 'i.e.', 'e.g.']
    for abbr in abbreviations:
        text = text.replace(abbr, abbr.replace('.', '@'))
    
    # Dividimos por puntos finales, exclamaciones y preguntas
    sentences = []
    current = []
    words = text.split()
    
    for word in words:
        current.append(word)
        if word.endswith(('.', '!', '?')):
            sentence = ' '.join(current)
            # Restauramos los puntos en abreviaturas
            sentence = sentence.replace('@', '.')
            sentences.append(sentence)
            current = []
    
    if current:
        sentence = ' '.join(current)
        sentence = sentence.replace('@', '.')
        sentences.append(sentence)
        
    return sentences

def clean_and_normalize(text: str) -> str:
    """Limpia y normaliza el texto base."""
    # Eliminar espacios y saltos de línea excesivos
    text = re.sub(r'\s+', ' ', text)
    # Normalizar puntuación
    text = re.sub(r'\s+([.,!?])', r'\1', text)
    text = re.sub(r'([.,!?])([^\s])', r'\1 \2', text)
    return text.strip()

def fix_capitalization(text: str, language: str) -> str:
    """Corrige la capitalización de oraciones y nombres propios."""
    # Lista de términos que siempre deben estar capitalizados
    proper_nouns = ['Myers-Briggs', 'Enneagram', 'Sandy', 'Crocker']
    
    # Dividir en oraciones usando el tokenizador del idioma correcto
    sentences = nltk.sent_tokenize(text, language=language)
    capitalized = []
    
    for sentence in sentences:
        # Capitalizar primera letra de la oración
        sentence = sentence[0].upper() + sentence[1:] if sentence else ''
        
        # Capitalizar nombres propios
        for noun in proper_nouns:
            pattern = re.compile(re.escape(noun.lower()), re.IGNORECASE)
            sentence = pattern.sub(noun, sentence)
            
        capitalized.append(sentence)
        
    return ' '.join(capitalized)

def format_paragraphs(text: str, language: str) -> str:
    """Formatea el texto en párrafos legibles."""
    sentences = nltk.sent_tokenize(text, language=language)
    paragraphs = []
    current = []
    
    for sentence in sentences:
        current.append(sentence)
        # Crear nuevo párrafo después de 2-4 oraciones que terminen en .!?
        if len(current) >= 2 and sentence[-1] in '.!?':
            paragraphs.append(' '.join(current))
            current = []
            
    if current:
        paragraphs.append(' '.join(current))
        
    return '\n\n'.join(paragraphs)

def combine_transcripts(youtube_text: str, pixel_text: str) -> str:
    """Combina dos transcripciones priorizando la versión más completa."""
    # Detectar idioma del texto más largo (probablemente el más confiable)
    base_text = pixel_text if len(pixel_text) > len(youtube_text) else youtube_text
    language = detect_language(base_text)
    
    # Asegurar que tenemos los recursos necesarios
    ensure_nltk_resources(language)
    
    # Extraer timestamp
    timestamp = extract_timestamp(youtube_text)
    
    # Usar Pixel 6 como base por ser más completo
    base_text = pixel_text
    
    # Aplicar procesamiento
    text = clean_and_normalize(base_text)
    text = fix_capitalization(text, language)
    text = format_paragraphs(text, language)
    
    # Añadir timestamp
    return f"{timestamp}\n\n{text}" 