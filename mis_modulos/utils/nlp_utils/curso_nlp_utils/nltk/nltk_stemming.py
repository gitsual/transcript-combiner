"""
Stemming se refiere al proceso de reducir cada palabra a su raíz o base. Algunas aplicaciones, como la clasificación de documentos, pueden beneficiarse de la derivación para reducir el vocabulario y centrarse en el sentido o sentimiento de un documento más que en un significado más profundo.


    Cargar el texto sin procesar.
    Divídanse en fichas.
    Convertir a minúsculas.
    Elimina el signo de puntuación de cada ficha.
    Filtrar los tokens restantes que no estén en orden alfabético.
    Filtrar tokens que son palabras de parada.
"""

import string
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


def stemming(text):
    # Convirtiendo en palabras
    tokens = word_tokenize(text)

    # Convertir a minúsculas
    tokens = [w.lower() for w in tokens]

    # Prepare a regex para el filtrado de caracteres
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))

    # Eliminar la puntuación de cada palabra
    stripped = [re_punc.sub('', w) for w in tokens]

    # Eliminar los tokens restantes que no estén en orden alfabético
    words = [word for word in stripped if word.isalpha()]

    # Filtrar las palabras de interrupción
    stop_words = set(stopwords.words('spanish'))
    words = [w for w in words if not w in stop_words]
    print(words[:100])

    """
    Al ejecutar este ejemplo, podemos ver que además de todas las otras transformaciones, las palabras de stop como a y haber sido eliminadas. Observo que todavía nos quedan fichas como nt. La madriguera del conejo es profunda; siempre hay algo más que podemos hacer.
    
    ['one', 'morning', 'gregor', 'samsa', 'woke', 'troubled', 'dreams', 'found', 'transformed', 'bed', 'horrible', 'vermin', 'lay', 'armourlike', 'back', 'lifted', 'head', 'little', 'could', 'see', 'brown', 'belly', 'slightly', 'domed', 'divided', 'arches', 'stiff', 'sections', 'bedding', 'hardly', 'able', 'cover', 'seemed', 'ready', 'slide', 'moment', 'many', 'legs', 'pitifully', 'thin', 'compared', 'size', 'rest', 'waved', 'helplessly', 'looked', 'happened', 'thought', 'nt', 'dream', 'room', 'proper', 'human', 'room', 'although', 'little', 'small', 'lay', 'peacefully', 'four', 'familiar', 'walls', 'collection', 'textile', 'samples', 'lay', 'spread', 'table', 'samsa', 'travelling', 'salesman', 'hung', 'picture', 'recently', 'cut', 'illustrated', 'magazine', 'housed', 'nice', 'gilded', 'frame', 'showed', 'lady', 'fitted', 'fur', 'hat', 'fur', 'boa', 'sat', 'upright', 'raising', 'heavy', 'fur', 'muff', 'covered', 'whole', 'lower', 'arm', 'towards', 'viewer']
    """

    return words


if __name__ == '__main__':
    text = 'De este modo, aún interviniendo la mano del podador, la planta conserva su forma característica; no sufre a causa de cortes antinaturales; se mantiene sana y conservaba un follaje denso y alegre.'
    print(stemming(text))
