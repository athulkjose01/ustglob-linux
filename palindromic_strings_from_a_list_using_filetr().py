words = ["level", "python", "madam", "world", "noon"]
palindromes = list(filter(lambda w: w == w[::-1], words))
print(palindromes)
