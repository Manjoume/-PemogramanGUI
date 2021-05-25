# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:40:52 2021

@author: LENOVO
"""

class Aritmatika : 
    
    @staticmethod 
    def tambah(a,b) : 
        return a+b
    
    @staticmethod
    def kurang(a,b) : 
        return a - b
    
    @staticmethod 
    def bagi(a,b) : 
        return a / b
    
    @staticmethod 
    def bagi_int(a,b) : 
        return a // b
    
    @staticmethod 
    def pangkat(a,b) : 
        return a ** b

# Langsung Panggil Fungsi dan kelas
print (Aritmatika.tambah(5,5))

# Bikin Objek Dahulu
objekA = Aritmatika()
print (objekA.pangkat(2,3))
