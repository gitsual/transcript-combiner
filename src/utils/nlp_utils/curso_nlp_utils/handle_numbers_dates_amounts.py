import re


def remove_numbers(text):
    text_without_numbers = ''
    for char in text:
        if not char.isdigit():
            text_without_numbers += char
    return text_without_numbers


def remove_dates(text):
    text_without_dates = ''
    for char in text:
        if not char.isdigit() or char == '/':
            text_without_dates += char
    return text_without_dates


def remove_amounts(text):
    text_without_amounts = ''
    for char in text:
        if not char.isdigit() or char == '.':
            text_without_amounts += char
    return text_without_amounts


def remove_numbers_regex(text):
    return re.sub(r'\d+', '', text)


def remove_dates_regex(text):
    return re.sub(r'\d+/\d+/\d+', '', text)


def remove_amounts_regex(text):
    return re.sub(r'\d+\.\d+', '', text)
