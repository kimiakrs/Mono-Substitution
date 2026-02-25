# Monoalphabetic Substitution Cipher

This project presents a complete implementation of the Monoalphabetic Substitution Cipher in Python, 
followed by a practical cryptanalysis phase using Frequency Analysis (Monograms, Bigrams, and Trigrams).

The study demonstrates:

* Secure random key generation

* Encryption and decryption pipeline

* Statistical cryptanalysis

* Iterative refinement using manual mapping

Practical demonstration of why classical substitution ciphers are insecure

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Classical Cipher](https://img.shields.io/badge/Cipher-Monoalphabetic%20Substitution-pink.svg)](https://en.wikipedia.org/wiki/Substitution_cipher)
[![Cryptanalysis](https://img.shields.io/badge/Technique-Frequency%20Analysis-purple.svg)](https://en.wikipedia.org/wiki/Frequency_analysis)
[![N-gram Analysis](https://img.shields.io/badge/Method-N--Gram%20Statistics-green.svg)](https://en.wikipedia.org/wiki/N-gram)
[![Cryptography](https://img.shields.io/badge/Field-Cryptography-darkblue.svg)](https://en.wikipedia.org/wiki/Cryptography)
[![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-critical.svg)](https://en.wikipedia.org/wiki/Computer_security)
[![Educational Project](https://img.shields.io/badge/Purpose-Academic%20Project-lightgrey.svg)](https://en.wikipedia.org/wiki/Classical_cipher)
[![MIT License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---
## Table of Contents

- [Project Overview](#project-overview)
- [Theoretical Background](#theoretical-background)
- [Phase1: Monoalphabetic Encryption & Decryption](#phase1-monoalphabetic-encryption--decryption)
- [Phase2: Frequency Analysis Attack](#phase2-frequency-analysis-attack)
- [Techonlogies Used](#techonlogies-used)
- [Project Structure](#project-structure)
- [Security Discussion ](#security-discussion )
- [Key Learning Outcomes](#key-learning-outcomes)
- [Disclaimer](#disclaimer)
- [License](#license)

---

## Project Overview

The Monoalphabetic Substitution Cipher is a classical encryption technique 
where each letter in the plaintext is replaced by a fixed substitute letter (26 letters) from a randomly generated key.

```python
Plain Alphabet : abcdefghijklmnopqrstuvwxyz
Key Alphabet   : qwertyuiopasdfghjklzxcvbnm
```

Each plaintext letter maps uniquely to one ciphertext letter.
Although the theoretical key space is large (26!), the cipher is vulnerable to statistical attacks, particularly frequency analysis.

This project is divided into two major phases:

* Secure encryption and decryption using a randomly generated key
* Breaking the cipher using frequency analysis and iterative refinement


---

## Theoretical Background

Monoalphabetic Substitution Cipher

* One-to-one fixed letter mapping 
* Deterministic transformation
* Key consists of a permutation of the 26-letter alphabet
* Encyrption and decryption are symmetric

Key space:

```
26! ≈ 4 × 10^26 possible keys
```

Despite the large key space, language redundancy makes the cipher insecure.


### Frequency Analysis

Natural languages follow predictable statistical patterns.

#### Common English Letter Frequencies

Most frequent letters:
```
E, T, A, O, I, N, S, R, H, L

```

#### Common Bigrams

```
TH, HE, IN, ER, AN

```

#### Common Trigrams

```
THE, AND, ING, ENT

```

---

## Phase1: Monoalphabetic Encryption & Decryption 


### Step1 - Initialization

* Read plaintext file

* Normalize text (lowercase)

* Prepare alphabet

```python
import random
import string

alphabet = string.ascii_lowercase
```

### Step2 - Random Key Generation
Generate a secure random substitution key:

```python
key = ''.join(random.sample(alphabet, len(alphabet)))
```

* No duplicate characters

* Complete permutation

* Strong randomness


### Step3 - Encryption 

Create translation mapping:

```python
mapping = str.maketrans(alphabet, key)
cipher_text = plain_text.translate(mapping)
```

Each plaintext character is replaced consistently.

### Step4 - Decryption

Reverse the mapping:

```python
reverse_mapping = str.maketrans(key, alphabet)
decrypted_text = cipher_text.translate(reverse_mapping)
```


## Phase2: Frequency Analysis Attack

This phase demonstrates how to break the cipher using statistical methods.

### Step1 - N-gram Generation

* Monograms (1-gram) :Single letter frequency
* Bigrams (2-gram) : Two-letter sequences
* Trigram (3-gram) : Three-letter sequences

```
Tree
→ Tr, re, ee

```

### Step2 - Frequnecy Counting

```python
Counter(n_grams)
```

* Count occurrences

* Sort frequencies

* Display top 20 results

Compare cipher frequencies with known English frequency tables.


### Step3 - Initial Mono Mapping

Map :

Most frequent cipher letter
==> Most frequent English letter

```
Cipher 'x' → 'e'
Cipher 't' → 'h
```

Apply initial substitution to generate partially decrypted text.


### Step4 - Bigram & Trigram Refinement

* Recompute frequencies after initial mapping
* Compare with English bigram/trigram tables
* Apply substitution corrections
* Improve readability

### Step5 - Manual Iterative Refinement

* Specify number of iterations

* Display updated frequencies

* Provide character substitution pairs

* Apply mapping

* Repeat

This demonstrates real-world cryptanalysis workflow.


---

## Techonlogies Used


| Component           | Description           |
| ------------------- | --------------------- |
| Python 3.x          | Programming language  |
| random              | Secure key generation |
| string              | Alphabet generation   |
| re                  | Text preprocessing    |
| collections.Counter | Frequency analysis    |

### Installation

No external libraries required.
Ensure Python 3.x is installed.

Run : 
```
python3 Task2-mono.py
python3 Task2-analysis.py

```
---

## Project Structure

```
Mono-Substitution/
│
├── Task2-mono.py              # Encryption & Decryption
├── Task2-analysis.py          # Frequency Analysis Attack
├── Report-Task2.pdf           # Full academic documentation
└── README.md
```

 For a complete step-by-step explanation of the implementation, execution workflow, frequency analysis process, screenshots, and detailed outputs, please refer to:

[Report-Task2.pdf](./Report-Task2.pdf)

### Execution Workflow

### Run Encryption

```Bash
python3 Task2-mono.py
```

### Run Frequency Analysis Attack

```
python3 Task2-analysis.py
```

---

## Security Discussion 

Monoalphabetic substitution:

* Preserves language patterns

* Is vulnerable to statistical analysis

* Does not provide modern cryptographic security

Even with a large key space (26!), it is easily broken due to predictable frequency patterns.

Modern secure alternatives include:

* AES

* DES (historical)

* ChaCha20

* RSA / ECC

---

## Key Learning Outcomes

* Implementation of classical substitution cipher
* Secure key permutation generation
* Translation table mapping
* Frequency-based cryptanalysis
* N-gram statistical modeling
* Human-assisted iterative refinement
* Understanding weaknesses of classical encryption

---
## Disclaimer


This implementation is for educational purposes only.

This project was developed for the Software Optimization course at the University of Europe for Applied Sciences and monoalphabetic substitution is cryptographically insecure and must not be used for secure communication.

---
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
