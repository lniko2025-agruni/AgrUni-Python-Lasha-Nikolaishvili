import functools


sentence = "Data Science is fun and Data Analysis is powerful if data is understood well."

# 1
words = sentence[:-1].split(" ")
print("Words:", words)

# 2
lower_words = list(map(lambda word: word.lower(), words))
print("Lower case words:", lower_words)

# 3
word_counts = functools.reduce(lambda res, word: res.update({word: lower_words.count(word)}) or res, lower_words, {})
print("Word counts dict:", word_counts)

# 4
most_repeated = max(word_counts, key=lambda w: word_counts.get(w))
print("Most repeated word: ", most_repeated)

# 5
more_than_3 = list(filter(lambda w: len(w) > 3, word_counts.keys()))
print("Words that have more than 3 letters:", more_than_3)