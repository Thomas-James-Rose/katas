import anagrams

def test_anagrams():
  word = "horse"
  expected_anagrams = ["shoer", "shore"]
  assert anagrams.get_anagrams(word) == expected_anagrams