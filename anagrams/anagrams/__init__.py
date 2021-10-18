from . import words
from functools import reduce

def sort_word_by_length (acc, word):
  word_length = len(word)
  if(word_length in acc):
    acc[word_length].append(word)
  else:
    acc[word_length] = [word]

  return acc
  

words_file = open("./words.txt", "r")
word_list =  words_file.read().splitlines()
word_list_by_word_length = reduce(sort_word_by_length, word_list, {})

def separate_anagrams_from_list(word, word_list):
  if word not in word_list:
    raise RuntimeError('Word not found in list')

  anagrams = []
  not_anagrams = []
  
  for check_word in word_list:
    if ''.join(sorted(word)) == ''.join(sorted(check_word)):
      anagrams = anagrams + [check_word]
    else:
      not_anagrams = not_anagrams + [check_word]

  return (anagrams, not_anagrams)

def get_all_anagrams():
  for word_length in word_list_by_word_length:
    word_list = word_list_by_word_length[word_length]
    anagrams_list = []

    while len(word_list) > 0: 
      word = word_list[0]
      (anagrams, remaining_list) = separate_anagrams_from_list(word, word_list)
      print(anagrams)
      word_list = remaining_list
