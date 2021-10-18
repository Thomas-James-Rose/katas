import anagrams
import pytest

def test_get_anagrams():
  test_cases = [
    { "word": "horse", "anagrams": ["shoer", "shore"] },
    { "word": "lemon", "anagrams": ["melon", "monel"] },
    { "word": "dog", "anagrams": ["god"] },
  ]

  for case in test_cases:
    assert anagrams.get_anagrams(case["word"]) == case["anagrams"]

def test_non_existent_word():
  with pytest.raises(RuntimeError, match="Word not found in dictionary"):
        anagrams.get_anagrams("purplemonkeydishwasher")