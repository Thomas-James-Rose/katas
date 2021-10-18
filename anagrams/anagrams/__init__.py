from . import words

words_file = open("./words.txt", "r")
word_list =  words_file.read().splitlines()

def get_anagrams(word):
  if word not in word_list:
    raise RuntimeError('Word not found in dictionary')
  anagram_filter = words.get_anagram_filter(word)
  anagrams = list(filter(anagram_filter, word_list))
  return anagrams

def get_all_anagrams():
  for word in word_list:
    print('{} : {}'.format(word, get_anagrams(word)))