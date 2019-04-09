# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
from urllib.parse import quote_plus


print("Enter sentence to parse from amazon\n\nExample:'Virtue signalling is society's version of Proof of Stake'\n\n")
query = input()
print("If you want to parse it word by word press 'Y'\n\n To parse in a single go press 'N'\n\n")
flag = input()


def parse(url):
    soup = BeautifulSoup(urllib.request.urlopen(url), "lxml")
    title = soup.title.string
    matched_string = title.replace('Amazon.com: ', '')
    return matched_string


def parse_word_by_word():
    word_list = list()
    word_arr = query.split()
    for word in word_arr:
        url = 'https://www.amazon.com/s?k=%s' % word
        word_list.append(parse(url))
    print(' '.join(word_list))
    return ' '.join(word_list)


def parse_complete_sentence():
    encoded_query = quote_plus(query)
    url = 'https://www.amazon.com/s?k=%s' % encoded_query
    sentence = parse(url)
    print(sentence)
    return sentence


def amazon_parse():
    if flag == 'y':
        parse_word_by_word()
    elif flag == 'n':
        parse_complete_sentence()
    else:
        pass


amazon_parse()
