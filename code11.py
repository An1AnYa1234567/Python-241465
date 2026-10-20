# Write a program to demonstrate Text Anagram and Pattern Matcher Tool.
# Anagram Checker

def clean_word(text):
    return ''.join(text.lower().split())


def are_anagrams(word1, word2):
    word1 = clean_word(word1)
    word2 = clean_word(word2)

    # Method 1: Using sorting
    if sorted(word1) == sorted(word2):
        return True
    return False


def find_anagrams(words):
    anagram_dict = {}

    for word in words:
        cleaned = clean_word(word)

        # Immutable tuple key
        key = tuple(sorted(cleaned))

        if key not in anagram_dict:
            anagram_dict[key] = []

        anagram_dict[key].append(word)

    return anagram_dict


# Input words
words = input("Enter words separated by commas: ").split(",")

print("\nAnagram Groups:")

groups = find_anagrams(words)

for key, group in groups.items():
    if len(group) > 1:
        print(group)

# Check two phrases
print("\nCheck Anagram Pair:")
first = input("Enter first word or phrase: ")
second = input("Enter second word or phrase: ")

if are_anagrams(first, second):
    print("They are anagrams.")
else:
    print("They are not anagrams.")