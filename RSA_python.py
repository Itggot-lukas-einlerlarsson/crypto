#!/usr/bin/env python
# -*- coding: utf-8 -*-
# TODO:
#two big primes
#n , phi(n)
#e - random til acceptable
#d = e^-1
# convert text into intstring -> then int -> send into RSA system.

import math
from random import randint

def main():
    blocksize = 3 # the larger the primes -> the larger the blocksize can be.
    indata = "hallåellerärduheltgoknödig"
    text = check_input_length(indata, blocksize)
    print("indata, plaintext:", text)
    text_in_ints = text_convert(text, blocksize)
    print(text_in_ints)
    public_key, private_key = RSA(1021,1087) #ex
    cipher = encrypt(text_in_ints, public_key[0], public_key[1]) #ciphers are integers -> cannot control conversion to be z_28
    print("cipher:", cipher)
    plaintext_in_ints = decrypt(cipher, private_key[0], private_key[1]) # doesnt work with blocksize larger than 1, text_in_ints =/= plaintext_in_ints
    print(plaintext_in_ints)
    plaintext = text_convert(plaintext_in_ints, blocksize, "text")
    print("Deciphered text:", plaintext)

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
                # print(blockstring)
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

def RSA(p, q): #only primes
    n = p*q
    phi = (p-1)*(q-1) #phi of n -> p and q are primes -> phi(n)=phi(p*q)=phi(p)*phi(q) = (p-1)*(q-1)
    e = 0
    d = 0
    while math.gcd(e,phi) != 1:
        e = randint(3,phi)
    d = pow(e, -1, phi)
    public_key = [n, e] # security is based on the fact that factorization of n takes a hella long time for large primes.
    private_key = [n, d]
    return public_key, private_key

def encrypt(text_in_ints, n, e):
    cipher = []
    for value in text_in_ints:
        cipher.append(pow(value, e)%n) #calculating...
    return cipher

def decrypt(cipher_in_ints, n, d):
    plaintext= []
    for value in cipher_in_ints:
        plaintext.append(pow(value, d)%n) #calculating...
    return plaintext


if __name__ == '__main__':
    main()
