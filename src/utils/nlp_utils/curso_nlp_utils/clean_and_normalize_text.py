import re
import string

from utils.spaCy_utils import string_tokenizer
from utils.vanilla_utils import get_nlp_punctuation_marks


def private_supra_1__clean_text(text, punctuation_marks, word_punctuation, tokenization):
    # Tokenizacion
    ## Dividimos por espacios en blanco
    if tokenization == 'SPACY':
        words = string_tokenizer(text, ' '.join(get_nlp_punctuation_marks()), False)

        # print(words[:100])
    else:
        words = text.split()

        # print(words[:100])

        ## Seleccionar palabras
        ### Filtramos por cadenas de caracteres alfanumericos
        words = re.split(r'\W+', text)
        # print(words[:100])

        """
        ['One', 'morning', 'when', 'Gregor', 'Samsa', 'woke', 'from', 'troubled', 'dreams', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin', 'He', 'lay', 'on', 'his', 'armour', 'like', 'back', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections', 'The', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment', 'His', 'many', 'legs', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him', 'waved', 'about', 'helplessly', 'as', 'he', 'looked', 'What', 's', 'happened', 'to', 'me', 'he', 'thought', 'It', 'wasn', 't', 'a', 'dream', 'His', 'room']
        """


    ## Dividir por espacios en blanco y eliminar la puntuación
    ### Python proporciona una constante llamada string.punctuation que proporciona una gran lista de caracteres de puntuación.
    # print(string.punctuation)

    """
    !"#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~
    """

    ### Podemos usar expresiones regulares para seleccionar los caracteres de puntuación y usar la función sub() para reemplazarlos por nada.
    if punctuation_marks != '':
        re_punc = re.compile('[%s]' % re.escape(punctuation_marks))
    else:
        re_punc = re.compile('[%s]')

    #### Eliminar la puntuación de cada palabra
    stripped = [re_punc.sub('', w) for w in words]
    words_without_punctuation = []

    for word in words:
        word_without_punctuation = word
        for key, value in zip(word_punctuation.keys(), word_punctuation.values()):
            word_without_punctuation.replace(key, value)
        words_without_punctuation.append(
            word.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u').replace('ñ',
                                                                                                                   'ni'))

    # print(stripped[:100])

    ### A veces, los datos de texto pueden contener caracteres no imprimibles.
    re_print = re.compile('[^%s]' % re.escape(string.printable))
    result = [re_print.sub('', w) for w in words_without_punctuation]
    # print(result[:100])

    return ' '.join(result)


def normalize_text(text):
    # Caso de Normalizacion
    ## Es común convertir todas las palabras en un solo caso.
    ## Podemos convertir todas las palabras a minúsculas llamando a la función lower() en cada palabra.

    # dividido de palabras por un espacio en blanco
    words = text.split()
    # convertir a minúsculas
    result = [word.lower() for word in words]
    # print(words[:100])

    """
    ['one', 'morning,', 'when', 'gregor', 'samsa', 'woke', 'from', 'troubled', 'dreams,', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin.', 'he', 'lay', 'on', 'his', 'armour-like', 'back,', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly,', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections.', 'the', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment.', 'his', 'many', 'legs,', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him,', 'waved', 'about', 'helplessly', 'as', 'he', 'looked.', '"what\'s', 'happened', 'to', 'me?"', 'he', 'thought.', 'it', "wasn't", 'a', 'dream.', 'his', 'room,', 'a', 'proper', 'human']
    """

    return ' '.join(result)


word_punctuation_dict = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
                         'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
                         'ä': 'a', 'ë': 'e', 'ï': 'i', 'ö': 'o', 'ü': 'u',
                         'â': 'a', 'ê': 'e', 'î': 'i', 'ô': 'o', 'û': 'u',
                         'ç': 'c'}

word_punctuation_with_ñ_dict = word_punctuation_dict
word_punctuation_with_ñ_dict['ñ'] = 'ni'


def clean_text_left_punctuation_left_ñ(text):
    return private_supra_1__clean_text(text, '', word_punctuation_dict, 'SPACY')


def clean_text_left_punctuation_normalize_ñ(text):
    return private_supra_1__clean_text(text, '', word_punctuation_with_ñ_dict, 'SPACY')


def clean_text_english(text):
    return private_supra_1__clean_text(text, string.punctuation, word_punctuation_dict, 'NORMAL')


def clean_text_english_normalize_ñ(text):
    return private_supra_1__clean_text(text, string.punctuation, word_punctuation_with_ñ_dict, 'NORMAL')


def clean_text_spanish_left_ñ(text):
    return private_supra_1__clean_text(text, ' '.join(get_nlp_punctuation_marks()), word_punctuation_dict, 'NORMAL')


def clean_text_spanish_normalize_ñ(text):
    return private_supra_1__clean_text(text, ' '.join(get_nlp_punctuation_marks()), word_punctuation_with_ñ_dict, 'NORMAL')


def clean_text_and_normalize_left_punctuation_left_ñ(text):
    return normalize_text(clean_text_left_punctuation_left_ñ(text))


def clean_text_and_normalize_left_punctuation_normalize_ñ(text):
    return normalize_text(clean_text_left_punctuation_normalize_ñ(text))


def clean_text_and_normalize_english(text):
    return normalize_text(clean_text_english(text))


def clean_text_and_normalize_english_normalize_ñ(text):
    return normalize_text(clean_text_english_normalize_ñ(text))


def clean_text_and_normalize_spanish_left_ñ(text):
    return normalize_text(clean_text_spanish_left_ñ(text))


def clean_text_and_normalize_spanish_normalize_ñ(text):
    return normalize_text(clean_text_spanish_normalize_ñ(text))


if __name__ == '__main__':
    text = 'De este modo, aún interviniendo la mano del podador, la planta conserva su forma característica; no sufre a causa de cortes antinaturales; se mantiene sana y conservaba un follaje denso y alegre.'

    print('CLEAN_TEXT:')
    print(clean_text_left_punctuation_left_ñ(text))
    print(clean_text_left_punctuation_normalize_ñ(text))
    print(clean_text_english(text))
    print(clean_text_english_normalize_ñ(text))
    print(clean_text_and_normalize_spanish_left_ñ(text))
    print(clean_text_spanish_normalize_ñ(text))
    print('\nNORMALIZE_TEXT:')
    print(normalize_text(text))
    print('\nCLEAN_AND_NORMALIZE_TEXT:')
    print(clean_text_and_normalize_left_punctuation_left_ñ(text))
    print(clean_text_and_normalize_left_punctuation_normalize_ñ(text))
    print(clean_text_and_normalize_english(text))
    print(clean_text_and_normalize_english_normalize_ñ(text))
    print(clean_text_and_normalize_spanish_left_ñ(text))
    print(clean_text_and_normalize_spanish_normalize_ñ(text))
