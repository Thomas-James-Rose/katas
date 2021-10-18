from . import words

words_file = open("./words.txt", "r")
word_list =  words_file.read().splitlines()

def get_anagrams (word):
  print(word_list[0])
  anagram_filter = words.get_anagram_filter(word)
  anagrams = list(filter(anagram_filter, word_list))
  return anagrams