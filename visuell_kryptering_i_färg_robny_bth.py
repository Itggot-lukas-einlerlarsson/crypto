# -*- coding: utf-8 -*-
# our teacher came up with this cryptosystem when working with visual crypto and showed it to us during class
# course MA1493 - VT 22
from PIL import Image
import numpy as np
import random

def main():
    encryption_test()

def encryption_test():
    #initialize
    im = Image.open("sample.png")
    width, length = im.size
    H = np.array(im)
    print("H:", H[0][1])
    R = create_rand_matrix(width, length)

    #encrypt
    S, T = encrypt(H, R, width, length)
    S_image = Image.fromarray(np.uint8(S))
    T_image = Image.fromarray(np.uint8(T))
    S_image.show()
    T_image.show()

    #decrypt
    H = decrypt(S, T, width, length)
    print("H:", H[0][1])
    H_image = Image.fromarray(np.uint8(H))
    H_image.show()


def encrypt(R, H, width, length):
    S = multiply_matrix(H, width, 2)
    print("S:", S[0][1])
    S = arithm_matrix(S, R, "-", width)
    print("S = ", S[0][1], "R = ", R[0][1])


    T = R
    print("T:",T[0][1])
    T = arithm_matrix(T, H, "-", width)
    print("T - H:",T[0][1])
    return (S, T)

def decrypt(S, T, width, length):
    H = arithm_matrix(S, T, "+", width)
    return H


def create_rand_matrix(width, length):
    r_matrix = []
    for i in range(0, length):
        row = []
        for i in range(0,width):
            temp = []
            for j in range(0,3):
                temp.append(random.randrange(0,256))
            temp.append(255)
            row.append(temp)
        r_matrix.append(row)
    return r_matrix

def multiply_matrix(matrix, width, num):
    for value in matrix:
        for i in range(0, width):
            for j in range(0,3):
                value[i][j] = (value[i][j] * num) % 256
    return matrix

def arithm_matrix(m1, m2, op, width):
    if op == "+":
        for k in range(0,len(m1)):
            for i in range(0, width):
                for j in range(0,3):
                    m1[k][i][j] = (m1[k][i][j] +m2[k][i][j]) % 256
    else:
        for k in range(0,len(m1)):
            for i in range(0, width):
                for j in range(0,3):
                    m1[k][i][j] = (m1[k][i][j] - m2[k][i][j]) % 256
    return m1

if __name__ == '__main__':
    main()
