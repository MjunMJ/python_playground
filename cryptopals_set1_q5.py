# -*- coding: utf-8 -*-
"""cryptopals_set1_Q5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dPrWNyu3HgCOUoSlABepc8CWbGn99GmB
"""

#repeating key XOR challenge in https://cryptopals.com/sets/1/challenges/5

plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

print(plaintext)

key ="ICE"

def repeat_keyxor(key, plaintext):
  parts = len(plaintext)
  key_len = len(key)
  times_of_key = int(parts/key_len)
  remainder = parts%key_len
  keystream = key*(times_of_key)+key[:remainder]
  input_bytes = bytes(plaintext, "ascii")
  keystream_bytes = bytes(keystream, "ascii")
  return bytes([a ^ b for a, b in zip(input_bytes, keystream_bytes)])

print(repeat_keyxor(key, plaintext).hex())