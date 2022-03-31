def unicode_decode(input_string):
    return input_string.decode('utf-8')


def unicode_encode(input_string):
    return input_string.encode('utf-8')


if __name__ == '__main__':
    print(unicode_decode('\u0050\u0079\u0074\u0068\u006f\u006e'))
    print(unicode_encode('Python'))
