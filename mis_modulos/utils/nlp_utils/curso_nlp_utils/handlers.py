from nltk.tokenize import word_tokenize
from nltk.stem import SnowballStemmer


def handle_stemming_snowball(text):
    stemmer = SnowballStemmer('spanish')
    text = word_tokenize(text)
    text = [stemmer.stem(word) for word in text]
    text = ' '.join(text)
    return text


if __name__ == '__main__':
    text = 'De este modo, aún interviniendo la mano del podador, la planta conserva su forma característica; no sufre a causa de cortes antinaturales; se mantiene sana y conservaba un follaje denso y alegre.'

    print(handle_stemming_snowball(text))