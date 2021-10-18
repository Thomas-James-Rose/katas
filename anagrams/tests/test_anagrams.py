import anagrams
import pytest

def test_get_anagrams():
  test_cases = [
    { 
      "word": "horse",
      "anagrams": ["horse", "shoer", "shore"]
    },
    { 
      "word": "dog",
      "anagrams": ["dog", "god"]
    },
    {
      "word": "lemon",
      "anagrams": ["lemon", "melon", "monel"]
    }
  ]

  for case in test_cases:
    assert anagrams.get_anagrams(case["word"]) == case["anagrams"]

def test_non_existent_word():
  with pytest.raises(RuntimeError, match="purplemonkeydishwasher not found in dictionary"):
        anagrams.get_anagrams("purplemonkeydishwasher")