from functools import reduce

words_file = open("./words.txt", "r")
word_list =  words_file.read().splitlines()

def sort_by_key(acc, word):
  key = ''.join(sorted(word))

  if key in acc:
    acc[key].append(word)
  else:
    acc[key] = [word]

  return acc

sorted_anagrams = reduce(sort_by_key, word_list, {})

def get_anagrams(word):
  if word not in word_list:
    raise RuntimeError(f"{word} not found in dictionary")
  return sorted_anagrams[''.join(sorted(word))]

def get_all_anagrams():
  for key in sorted_anagrams:
    anagrams = sorted_anagrams[key]
    print(anagrams)
