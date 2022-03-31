# Tokenización y limpieza con NLTK
## Instalar NLTK
# sudo pip install -U nltk

## Instalar NLKT en Anconda (recomendado)
# conda install -c anaconda nltk

## Después de la instalación, necesitará instalar los datos usados con la librería, incluyendo un gran conjunto de documentos que puede usar más tarde para probar otras herramientas en NLTK.
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

## Dividir en frases
### NLTK proporciona la función sent_tokenize() para dividir el texto en frases.
from nltk import sent_tokenize


def tokenize(text):
    ### Dividir en oraciones
    sentences = sent_tokenize(text)
    print(sentences[0])

    """
    Ejecutando el ejemplo, podemos ver que aunque el documento está dividido en oraciones, cada oración todavía conserva la nueva línea de la envoltura artificial de las líneas en el documento original.
    
    
    One morning, when Gregor Samsa woke from troubled dreams, he found
    himself transformed in his bed into a horrible vermin.
    """

    ## Dividir en palabras
    tokens = word_tokenize(text)
    print(tokens[:100])

    """
    Ejecutando el código, podemos ver que la puntuación son ahora símbolos que podríamos decidir filtrar específicamente.
    
    ['One', 'morning', ',', 'when', 'Gregor', 'Samsa', 'woke', 'from', 'troubled', 'dreams', ',', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin', '.', 'He', 'lay', 'on', 'his', 'armour-like', 'back', ',', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly', ',', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections', '.', 'The', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment', '.', 'His', 'many', 'legs', ',', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him', ',', 'waved', 'about', 'helplessly', 'as', 'he', 'looked', '.', '``', 'What', "'s", 'happened', 'to']
    """

    ## Filtrar puntuación en la salida del texto
    ### Eliminar todos los tokens que no estén en orden alfabético
    words = [word for word in tokens if word.isalpha()]
    print(words[:100])

    """
    Al ejecutar el ejemplo, se puede ver que se filtraron los signos de puntuación.
    
    ['One', 'morning', 'when', 'Gregor', 'Samsa', 'woke', 'from', 'troubled', 'dreams', 'he', 'found', 'himself', 'transformed', 'in', 'his', 'bed', 'into', 'a', 'horrible', 'vermin', 'He', 'lay', 'on', 'his', 'back', 'and', 'if', 'he', 'lifted', 'his', 'head', 'a', 'little', 'he', 'could', 'see', 'his', 'brown', 'belly', 'slightly', 'domed', 'and', 'divided', 'by', 'arches', 'into', 'stiff', 'sections', 'The', 'bedding', 'was', 'hardly', 'able', 'to', 'cover', 'it', 'and', 'seemed', 'ready', 'to', 'slide', 'off', 'any', 'moment', 'His', 'many', 'legs', 'pitifully', 'thin', 'compared', 'with', 'the', 'size', 'of', 'the', 'rest', 'of', 'him', 'waved', 'about', 'helplessly', 'as', 'he', 'looked', 'What', 'happened', 'to', 'me', 'he', 'thought', 'It', 'was', 'a', 'dream', 'His', 'room', 'a', 'proper', 'human', 'room']
    """

    ## Filtrar las palabras de interrupción
    """
    Las palabras reservadas son aquellas que no contribuyen al significado más profundo de la frase. Son las palabras más comunes tales como: the, a, y is. Para algunas aplicaciones como la clasificación de documentación, puede tener sentido eliminar las palabras de parada. NLTK proporciona una lista de palabras de parada comúnmente acordadas para una variedad de idiomas, como el inglés.
    """
    stop_words = stopwords.words('spanish')
    print(stop_words)

    """
    Puede ver que todas son minúsculas y que se ha eliminado la puntuación.
    
    ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    """

    return stop_words


if __name__ == '__main__':
    text = 'De este modo, aún interviniendo la mano del podador, la planta conserva su forma característica; no sufre a causa de cortes antinaturales; se mantiene sana y conservaba un follaje denso y alegre.'
    print(tokenize(text))
