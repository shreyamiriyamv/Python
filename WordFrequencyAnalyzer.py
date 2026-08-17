
file = open("input.txt", "r")
text = file.read()


text = text.lower()


punctuation_marks = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
for mark in punctuation_marks:
    text = text.replace(mark, "")

words = text.split()

# 3. Count occurrences using a dictionary
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# 4. Sort by frequency and display the top 10
# This sorts the word pairs by their count (item[1]) in descending order
sorted_words = sorted(word_counts.items(),
                      key=lambda item: item[1], reverse=True)
top_10 = sorted_words[:10]

# Display the results
print("Top 10 most frequent words:")
for word, count in top_10:
    print(f"{word} -> {count}")
