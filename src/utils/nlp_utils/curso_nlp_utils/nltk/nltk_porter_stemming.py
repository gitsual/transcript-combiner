"""
Hay muchos algoritmos de Stemming, aunque un método popular y de larga data es el algoritmo de Porter Stemming. Este método está disponible en NLTK a través de la clase PorterStemmer.
"""

from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer


def porter_stemming(text):

    # Dividirse en palabras
    tokens = word_tokenize(text)

    # Derivado de las palabras
    porter = PorterStemmer()
    stemmed = [porter.stem(word) for word in tokens]
    print(stemmed[:100])


    """
    Al ejecutar el ejemplo, se puede ver que las palabras se han reducido a su origen.
    
    ['one', 'morn', ',', 'when', 'gregor', 'samsa', 'woke', 'from', 'troubl', 'dream', ',', 'he', 'found', 'himself', 'transform', 'in', 'hi', 'bed', 'into', 'a', 'horribl', 'vermin', '.', 'He', 'lay', 'on', 'hi', 'armour-lik', 'back', ',', 'and', 'if', 'he', 'lift', 'hi', 'head', 'a', 'littl', 'he', 'could', 'see', 'hi', 'brown', 'belli', ',', 'slightli', 'dome', 'and', 'divid', 'by', 'arch', 'into', 'stiff', 'section', '.', 'the', 'bed', 'wa', 'hardli', 'abl', 'to', 'cover', 'it', 'and', 'seem', 'readi', 'to', 'slide', 'off', 'ani', 'moment', '.', 'hi', 'mani', 'leg', ',', 'piti', 'thin', 'compar', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him', ',', 'wave', 'about', 'helplessli', 'as', 'he', 'look', '.', '``', 'what', "'s", 'happen', 'to']
    """


if __name__ == '__main__':
    text = 'De este modo, aún interviniendo la mano del podador, la planta conserva su forma característica; no sufre a causa de cortes antinaturales; se mantiene sana y conservaba un follaje denso y alegre.'

    print(porter_stemming(text))
