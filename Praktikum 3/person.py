# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 16:15:01 2021

@author: LENOVO
"""

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)