def calculate_love_score(name1, name2):
    combine_names = (name1 + name2).upper()

    def letter_count(word):
        count_per_letter = 0
        for letter in word:
            count_per_letter += combine_names.count(letter)
        return count_per_letter

    true_count = letter_count("TRUE")
    love_count = letter_count("LOVE")

    love_score = str(true_count) + str(love_count)
    print(int(love_score))


calculate_love_score("Kanye West", "Kim Kardashian")
