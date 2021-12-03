#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO:
# ett stort primitivt tal p
# ett tal g som är en primitiv root till p
    # kan bruteforceas fram eller gaussalgoritm
# styrka: DLP - privatanyckeln a 

# OPTIMIZE:
#primitive root -- can use gaussalgoritm
# no double modulo

import math
from random import randint

def main():
    blocksize = 1 # streamcipher atm
    indata = "hallåellerärduheltgoknödigw"
    text = check_input_length(indata, blocksize)
    print("indata, plaintext:", text)
    text_in_ints = text_convert(text, blocksize)
    print(text_in_ints)
    public_key, private_key = elgamal(173) #p > 28
    print(public_key, private_key)
    cipher = encrypt(text_in_ints, public_key[0], public_key[1], public_key[2]) #ciphers are integers
    print("cipher:", cipher)
    plaintext_in_ints = decrypt(cipher, private_key[0], private_key[1])
    print(plaintext_in_ints)
    plaintext = text_convert(plaintext_in_ints, blocksize, "text")
    print("Deciphered text:", plaintext)

def elgamal(p):
    g = 0
    for a in range(2,p-2): # bruteforce, nat optimized.
        if g != 0:
            break
        if math.gcd(a,p) == 1:
            count = 1
            for j in range(1,p-1):
                if pow(a, j, p) == 1 and count != p-1:
                    break
                if count == p-2:
                    g = a
                    break
                count += 1
    a = randint(p, p*10)
    b = pow(g, a, p)
    public_key = [p, g, b]
    private_key = [a, p]
    return public_key, private_key

def text_convert(text, blocksize, type = "int"):
    if type == "text":
        alphabet = S_A()
        plaintext = ""
        if blocksize == 1:
            for value in text:
                plaintext += alphabet[value]
        else:
            for i in range(0, len(text)):
                count = 0
                blockstring = ""
                while count < blocksize:
                    blockstring += str(text[i]).zfill(blocksize*2)
                    count += 1
                count = 0
                while count < blocksize:
                    plaintext += alphabet[int(blockstring[count*2:count*2+2])]
                    count += 1
        return plaintext
    text_int = []
    count = 0
    while count < len(text):
        m = "" # blockstring first
        i = count
        while i < count+blocksize: #add m's number into a blockstring
            m += str(number_in_S_A(text[i])).zfill(2)
            i += 1
        m = int(m) #m -> integer
        text_int.append(m)
        count += blocksize
    return text_int

def check_input_length(text, blocksize):
    while len(text) % blocksize != 0:
        text += "x" #add filler
    return text

def number_in_S_A(letter_in):
    letter_in = letter_in.lower()
    alphabet = S_A()
    for index, letter in enumerate(alphabet):
        if letter == letter_in:
            return index
    return 22 # if it doesn't exist in {swedishalphabet}\{w} -> x

def S_A():
    return "abcdefghijklmnopqrstuvxyzåäö"

def encrypt(text_in_ints, p, g, b):
    cipher = []
    k = 0
    while math.gcd(k, p) != 1:
        k = randint(1, p)
    for value in text_in_ints:
        r = pow(g, k, p)
        t = (pow(b, k, p)*value)% p
        cipher.append([r, t])
    return cipher

def decrypt(cipher_in_ints, a, p):
    plaintext= []
    for value in cipher_in_ints:
        m = (pow(value[0], -a, p) * value[1])% p
        plaintext.append(m)
    return plaintext

if __name__ == '__main__':
    main()
