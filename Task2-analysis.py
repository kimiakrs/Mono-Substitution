#KimiaSadatKarbasi-SID60393958
#Import library
import random
#Using regex (Regular Expression)
import re
#Counting (n-grams)
from collections import Counter
import string


#Common English letter frequencies (20)
#Single letter frequency
ENGLISH_MONOGRAM = [
    "e", "t", "a", "o", "i", "n","s", "r", "h", "l", "d", "c",
    "u", "m", "f", "p", "g", "w", "y", "b",
]
#Two letters frequency
ENGLISH_BIGRAMS = [
    "th", "he", "in", "er", "an", "re","on", "at", "en", "nd", "ti", "es",
    "or", "te", "of", "ed", "is", "it", "al", "ar",
]                    

#Three letters frequency
ENGLISH_TRIGRAMS = [
    "the", "and", "ing", "ent", "ion", "her", "for", "tha", "nth", "int",
    "ere", "tio", "ter", "est", "ers", "ati", "hat","ate", "all","eth",
]

# Generate n-grams counting without spaces
def ngrams(n, text):
    #Using regex to not to add space and other charachters except alhpabetic words
    text = re.sub('[^a-zA-Z]', '', text)  
    for i in range(len(text) - n + 1):
        yield text[i:i+n]

#Printing out n-grams including()
def print_ngrams(text, N_GRAM, TOP_K):
    ngrams_dict = {}
    for N in range(1, N_GRAM + 1):
        #Coung and Sorting
        counts = Counter(ngrams(N, text))
        sorted_counts = counts.most_common(TOP_K)
        #Put it in the dictionary
        ngrams_dict[N] = {ngram: count for ngram, count in sorted_counts}
        print(f"{N}-gram (top {TOP_K}):")
        for ngram, count in sorted_counts:
            print(f"{ngram}: {count}")
        print("=====================")
    return ngrams_dict


#For applying mono_mapping (charachter by charachter)
def apply_mono_mapping(text, mono_map):
    return ''.join(mono_map.get(ch, ch) for ch in text)


#After getting first mono-gram
def apply_mapping_keys(mapping_dict, input_dict):
    output_dict = {}
    #Getting Keys and values of the sepecific mapping dict
    for key, value in input_dict.items():
        new_key = ''.join([mapping_dict.get(char, char) for char in key])
        output_dict[new_key] = value
    return output_dict


#Using for biagram and trigram
def apply_ngram(text, mapping, n):
    result = ""
    i = 0
    while i < len(text):
        section = text[i:i+n]
        if len(section) == n and section in mapping and section.isalpha():
            result += mapping[section]
            i += n
        else:
            result += text[i]
            i += 1
    return result
    
if __name__ == "__main__":
    print("This is Task2-analysis.py")
    print("Kimia Sadat Karbasi - Student ID Number ='60393958'")

    #Reading Cipher.txt
    with open('/opt/mono-cipher/cipher.txt') as f:
        encrypted_plain_text = f.read().lower()

#Finding mono-grams and mapping to the most common mono frequency
#Count and sort
#adding to  the dictionary and map them to the most frequency
ngrams_all = print_ngrams(encrypted_plain_text, 3, 20)
print("====================")
print("Show the mono mapping")
mono_gram = ngrams_all[1]
#Getting keys
mono_keys = list(mono_gram.keys())
map_mono = dict(zip(mono_keys, ENGLISH_MONOGRAM))
print(map_mono)
text_after_mono = apply_mono_mapping(encrypted_plain_text, map_mono)
print("========================")

#Reading the print_ngrams again from the new text
ngrams_all = print_ngrams(text_after_mono, 3, 20)
print("Show the bigram mapping")
bi_grams = ngrams_all[2]
bi_keys = list(bi_grams.keys())
map_bi = dict(zip(bi_keys, ENGLISH_BIGRAMS))
print(map_bi)
print("========================")
print("Show the trigram mapping")
tri_grams = ngrams_all[3]
tri_keys = list(tri_grams.keys())
map_tri = dict(zip(tri_keys, ENGLISH_TRIGRAMS))
print(map_tri)
print("========================")



#Apply my initial mono-mapping to other n-grams
#Transfering the value of mono-gram into other n-grams
mapp_bigrams = apply_mapping_keys(map_mono, map_bi)
mapp_trigrams = apply_mapping_keys(map_mono, map_tri)


#Show your changes after using initial mono-mapping
print("My bi-gram mapping after substitution:")
for k , v in mapp_bigrams.items():
    print(f"{k} ==> {v}")

print("My tri-gram mapping after substitution:")
for k, v in mapp_trigrams.items():
    print(f"{k} ==> {v}")

print("============================")


#Apply trigram to the text (first-one)
print("Initial applying using (trigram)")
Initial_decryption = apply_ngram(text_after_mono, map_tri, 3)
print("\n")
print(Initial_decryption)

#Now we are going to break down the code from the user.(Frequency Analysis)
#We will break it manually. (User Input)
#Adding loop (10 times/ or how many times we want) and
#Ask user to input 20 letters (one by one) and add it in the mapping dictionary

#Ask the user :  how many iteration you want to add for making the process
while True:
    iteration = int(input("How many iterations do you want to perform?: "))
    if iteration <= 0:
        print("Please enter a positive integer:")
    else:
        break

for i in range(iteration):
    print(f"\n My {i+1} iteration")
    #Get from the initial decryption you made (n-grams)
    current_ngrams = print_ngrams(Initial_decryption, 1, 20)
    current_mono_key = mono_keys = list(current_ngrams[1].keys())
    print("Current_mono_key:\n", current_mono_key)
    #Showing the mono-mapping
    map_cmono = dict(zip(current_mono_key, ENGLISH_MONOGRAM))
    print(f"{i+1} mapping mono:\n", map_cmono)
    print("========================")
    print("Please Enter 20 Letters:")
    manual_map = {}
    while len(manual_map) < 20:
        #We have to make sure that the user add the letter in the lower case
        #Using this example for generating the mapping manually by the hacker.
        user_input = input(f"({len(manual_map)+1}/20) Enter your mapping (x:y): ").strip().lower()
        if len(user_input) == 3 and user_input[1] == ":" and user_input[0] in string.ascii_lowercase and user_input[2] in string.ascii_lowercase:
            #Just get x and y without ":"
            src, dest = user_input[0], user_input[2]
            if src in manual_map:
                #If the mapping we add was in the manual_map we ask user again.
                print("The mapping you added is already exists.")
            else:
                manual_map[src] = dest
        else:
            print("Invalid format.")
            break
    print("Final manual map:")
    print(manual_map)

    Initial_decryption = apply_mono_mapping(Initial_decryption, manual_map)
    print(f"\n Decrypted text after {i+1} manual mapping:")
    print(Initial_decryption)
    print("===============================")
    






