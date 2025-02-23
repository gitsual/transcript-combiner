import spacy
import re

from src.utils.text_utils import list_one_to_one_package, clean_text

def string_tokenizer(text, punctuation_marks, remove_punctuation_marks):
    """
    This function takes a string and returns a list of tokens.
    The tokens are the words in the string.
    The punctuation marks are removed if remove_punctuation_marks is True.
    The punctuation marks are kept if remove_punctuation_marks is False.
    
    Parameters:
        text (str): The string to tokenize
        punctuation_marks (str): The punctuation marks to remove
        remove_punctuation_marks (bool): Whether to remove punctuation marks
        
    Returns:
        list: A list of tokens
    """
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    
    if remove_punctuation_marks:
        tokens = [token.text for token in doc if token.text not in punctuation_marks]
    else:
        tokens = [token.text for token in doc]
    
    return tokens

# ... resto de funciones de spaCy_utils.py ... 