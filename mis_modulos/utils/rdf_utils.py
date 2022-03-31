import requests

# Regular Expressions
import re

# RDFLIB
from rdflib import Graph


def get_babelnet_synonyms(url):

    print('\nBABELNET SYNONYM RDFLIB METHOD')

    g = Graph()
    g.parse(url)
    has_word = False

    related = []
    broader = []
    narrower = []

    for index, (sub, pred, obj) in enumerate(g):
        print(sub, pred, obj)
        if 'wiktionaryPageLink' in pred:
            word = str(obj).split('/')[-1]
            if not has_word:
                print('word: ' + word + ' (wiki)')
                has_word = True
        elif 'exactMatch' in pred:
            word = str(obj)
            if not has_word:
                if 'http' not in word:
                    print('http not in word')
                    print('word: ' + word + ' (exactMatch)')
                    has_word = True
                else:
                    print('http in word')
                    if 'https://lemon-model.net/lexica/uby/ow_eng/OW_eng_Synset_22656' not in word:
                        print('http not error in word')
                        print('word: ' + get_name_from_url(word) + ' (exactMatch)')
                        has_word = True
        elif 'related' in pred:
            related_url = str(obj)
            synonym = get_name_from_url(related_url)
            if synonym:
                related.append(synonym)
        elif 'broader' in pred:
            broader_url = str(sub)
            synonym = get_name_from_url(broader_url)
            if synonym:
                broader.append(synonym)
        elif 'narrower' in pred:
            narrower_url = str(sub)
            synonym = get_name_from_url(narrower_url)
            if synonym:
                narrower.append(synonym)

    return related, broader, narrower


def get_name_from_url(url):
    g = Graph()
    word = ''

    try:
        print('Parsed')
        g.parse(url)
        for index, (sub, pred, obj) in enumerate(g):
            print('\t' + str(sub) + ' ' + str(pred) + ' ' + str(obj))
            if 'exactMatch' in pred:
                exact_match_url = str(obj)
                if 'http://wordnet-rdf.princeton.edu/wn31/' in exact_match_url:
                    word = wordnet_treatment(exact_match_url)
                elif 'http://dbpedia.org/resource/' in exact_match_url:
                    print('Checking')
                    word = dbpedia_treatment(exact_match_url)
            elif 'wiktionaryPageLink' in pred:
                word = str(obj).split('/')[-1]
    except:
        print('Parsing error')
        print('url: ' + str(url))
        if 'http://dbpedia.org/resource/' in url:
            print('Checking')
            word = dbpedia_treatment(url)
        elif 'http://wordnet-rdf.princeton.edu/wn31/' in url:
            print('Checking')
            word = wordnet_treatment(url)

    return word


def wordnet_treatment(exact_match_url):
    # print(exact_match_url)
    match_id = exact_match_url.split('/')[-1]
    wordnet_json_url = 'http://wordnet-rdf.princeton.edu/json/id/' + match_id[1:len(match_id)]
    # print('\t' + wordnet_json_url)
    response = requests.get(wordnet_json_url)

    synonym = ''
    #synonyms = []

    # Response treatment
    if response.status_code == 200 and response.text != 'Synset Not Found':
        # Parsing the response
        json_response = response.json()

        # print(json_response)

        if json_response[0]:
            response_content = json_response[0]
            # print(response_content)
            for lemmas in response_content['lemmas']:
                # print(lemmas['lemma'])
                if lemmas['lemma']:
                    synonym = lemmas['lemma']
                    # synonyms.append(synonym)

    return synonym


def dbpedia_treatment(exact_match_url):
    print(exact_match_url)
    match_id = exact_match_url.split('/')[-1]
    dbpedia_json_url = 'http://dbpedia.org/data/' + match_id + '.jsod'
    response = requests.get(dbpedia_json_url)

    print('AQUI' + str(dbpedia_json_url))

    synonym = ''
    #synonyms = []

    # Response treatment
    if response.status_code == 200:

        response.encoding = response.apparent_encoding

        # Parsing the response
        json_response = response.json(strict=False)

        print(json_response)

        if json_response['d']:
            response_content = json_response['d']
            print(response_content)
            if response_content['results']:
                results = response_content['results']
                print(results)
                if results[0]:
                    first_result = results[0]
                    print(first_result)
                    for key in first_result:
                        if 'label' in key:
                            if is_occidental_version(first_result[key]):
                                print(first_result[key])
                                synonym = first_result[key].lower()
                                clean_synonym = re.sub("[\(\[].*?[\)\]]", "", synonym).rstrip()
                                synonym = clean_synonym

    print('returned synonym: ' + str(synonym))

    return synonym


def is_occidental_version(word):
    words = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚabcdefghijklmnñopqrstuvwxyzáéíóú()[] '
    occidental_version = True
    for character in word:
        if not character in words:
            occidental_version = False

    return occidental_version

