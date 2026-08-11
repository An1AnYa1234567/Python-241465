# Program-2 - Automated word frequency and pattern analyzer.
print("---Automated Word Frequency and Pattern Analyzer---")

# To read text from  file
file = open("text.txt", "r")
text = file.read()
file.close()

# Convert text to lowercase
text = text.lower()

# Remove punctuation using string methods
punctuation = ".,!?;:'\"()-"

for ch in punctuation:
    text = text.replace(ch, "")

# Remove extra spaces
text = " ".join(text.split())

# Split text into words
words = text.split()

# Total word count
print("\nTotal Words:", len(words))

# Find palindrome words
print("\nPalindrome Words:")

found = False

for word in words:
    reverse = word[::-1]

    if word == reverse and len(word) > 1:
        print(word)
        found = True

if found == False:
    print("No palindrome found")

# Word frequency
print("\nWord Frequency:")

for i in range(len(words)):
    count = 0

    # Check if word was already processed
    already_checked = False

    for j in range(i):
        if words[i] == words[j]:
            already_checked = True
            break

    if already_checked == False:
        for word in words:
            if words[i] == word:
                count += 1

        print(words[i], ":", count)
