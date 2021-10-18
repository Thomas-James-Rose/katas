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

def get_anagrams(word):
  if word not in word_list:
    raise RuntimeError('Word not found in dictionary')

  anagram_filter = words.get_anagram_filter(word)
  anagrams = list(filter(anagram_filter, word_list_by_word_length[len(word)]))
  return anagrams

def get_all_anagrams():
  for word in word_list:
    anagrams = get_anagrams(word)
    if anagrams != []:
      print('{} : {}'.format(word, anagrams))