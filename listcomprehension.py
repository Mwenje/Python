words = ["apple", "banana", "grape", "kiwi", "orange", "pear"]

odd_length_words=[word for word in words if len(word) %2 !=0]

print("Words with an odd number of characters:", odd_length_words)