words = ["apple", "cat", "orange", "egg", "ball"]
vowels = ("a", "e", "i", "o", "u")
vowel_words = list(filter(lambda w: w.lower().startswith(vowels), words))
print(vowel_words)
