# -*- coding: utf-8 -*-

# Vogais #

def vogal(x):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    if x in vogais:
        return True
    elif x.isalpha():
        return False
    else:
        return False


vogal("a")
vogal("b")
vogal("E")

