#KimiaSadatKarbasi-SID60393958
#Import library
import random
import string


def mono_encrypt(text, alphabet, key):
    # maketrans creates a mapping between characters from alphabet to key
    translation_table = str.maketrans(alphabet, key)
    print("Translation_table", translation_table)
    return text.translate(translation_table)

def mono_decrypt(text, alphabet, key):
    #maketrans creates a mapping between characters from key to alphabet
    reverse_translation_table = str.maketrans(key, alphabet)
    print("Translation Table:", reverse_translation_table)
    return text.translate(reverse_translation_table)


if __name__ == "__main__":  

    print("This is Task2-mono.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")

    #Adding Charachters
    alphabet = string.ascii_lowercase

    #Generating Key
    key_list = random.sample(alphabet, len(alphabet))
    #Convert key to a string
    key = ''.join(key_list)
    print( f"Generated Key: {key}")

    #Plain_text path
    file_path = "/opt/mono-cipher/plain.txt"
    cipher_text_path = "/opt/mono-cipher/cipher.txt"
    decrypted_text_path = "/opt/mono-cipher/decrypted.txt"

    #Reading plain.txt
    try:
        with open(file_path, "r", encoding="utf-8") as f:
         text = f.read().lower()
    except Exception as e:
        print(f"The file was not found")
        exit()
    
    print("Plain text:", text)
    cipher_text = mono_encrypt(text, alphabet, key) 
    cipher_text_lower = cipher_text.lower()
    decrypted_text = mono_decrypt(cipher_text, alphabet, key)

    # Write encrypted data to the file
    with open(cipher_text_path, "w", encoding="utf-8") as f:
        f.write(cipher_text_lower)

    #Write decrypted data to the file
    with open(decrypted_text_path, "w", encoding="utf-8") as f:
        f.write(decrypted_text)

    print(f"Encrypted text saved to: {cipher_text_path}")
    print("Encrypted Text:", cipher_text_lower)
    print("Decrypted Text:", decrypted_text)




