def calculate_shifts(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    return alphabet.index(letter.lower())

def encrypt_letter(letter, key_char):
    if not letter.isalpha():
        return letter
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_char = str(key_char)
    shift = calculate_shifts(key_char)
    shifted_index = (alphabet.index(letter.lower()) + shift) % 26
    return alphabet[shifted_index]

def encrypt_text(encrypted_text, key):
    encrypted_text = ''
    key_index = 0
    encrypted_text = encrypted_text.lower()
    key = key.lower()
    for char in encrypted_text:
        key_char = key[key_index % len(key)]
        encrypted_text += encrypt_letter(char, key_char)
        if char.isalpha():
            key_index = (key_index + 1) % len(key)
    return encrypted_text

text = input("Which text should be encrypted? ").lower()
custom_key = input("Which keyword should be used? ").lower()

print(encrypt_text(text, custom_key))
