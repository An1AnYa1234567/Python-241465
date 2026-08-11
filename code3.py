# Program1-Dynamic command-line caesar cipher tool
text = input("Enter the message: ")
shift = int(input("Enter the shift key: "))
mode = input("Enter mode (encode/decode): ")
if mode == "decode":          # If decoding, make the shift negative
    shift = -shift
result = ""
for ch in text:               # Process each character
    if ch.isalpha():
        if ch.isupper():
            ascii_value = ord(ch) - ord('A')
            new_value = (ascii_value + shift) % 26
            new_char = chr(new_value + ord('A'))

        else:
            ascii_value = ord(ch) - ord('a')
            new_value = (ascii_value + shift) % 26
            new_char = chr(new_value + ord('a'))

        result = result + new_char

    else:
        result = result + ch

print("Result:", result)