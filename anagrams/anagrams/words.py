def get_anagram_filter(a):
  return lambda b : a != b and ''.join(sorted(a)) == ''.join(sorted(b))