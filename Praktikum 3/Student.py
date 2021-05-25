# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:53:44 2021

@author: LENOVO
"""

from Person import Person

class Student(Person) :
   def __init__(self, fname, lname):
    super().__init__(fname, lname)