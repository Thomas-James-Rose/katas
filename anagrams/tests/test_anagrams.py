import anagrams
import pytest

def test_separate_anagrams_from_list():
  test_cases = [
    { 
      "word": "horse",
      "word_list": ["horse", "house", "shoer", "shore"],
      "anagrams": ["horse", "shoer", "shore"],
      "not_anagrams": ["house"]
    }
  ]

  for case in test_cases:
    (found_anagrams, not_anagrams) = anagrams.separate_anagrams_from_list(case["word"], case["word_list"])
    assert found_anagrams == case["anagrams"]
    assert not_anagrams == case["not_anagrams"]

def test_non_existent_word():
  with pytest.raises(RuntimeError, match="Word not found in dictionary"):
        anagrams.separate_anagrams_from_list("purplemonkeydishwasher", ["orange", "giraffe", "kettle"])