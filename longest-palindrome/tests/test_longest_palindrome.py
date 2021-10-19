import longest_palindrome

def test_get_longest_palindrome():
  test_cases = [
    {
      "string": "Banana",
      "expected_palindrome": "anana"
    },
    {
      "string": "Hello world",
      "expected_palindrome": "ll"
    },
    {
      "string": "Platypus",
      "expected_palindrome": "P"
    }
  ]

  for case in test_cases:
    assert longest_palindrome.get(case["string"]) == case["expected_palindrome"]
