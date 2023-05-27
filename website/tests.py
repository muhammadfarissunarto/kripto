# from django.test import TestCase

# Ceate your tests here.
def decrypt(text, shift):
    decrypted_text = ''
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

encrypted_text = "ddddd"
shift_value = 3
decrypted_text = decrypt(encrypted_text, shift_value)
print(decrypted_text)
