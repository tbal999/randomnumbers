# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:06:45 2019

@author: thoma
"""
import random as rand
import time

race = ([0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],)

list = [1,2,3,4,5,6,7,8,9]

def letsGo(x,y,z):
    global race
    column = 0
    row = 0
    for i in race[column:]:
        for a in i[row:]:
            if column == x and row == y:
                race[column][row] = z
                column = 0
                row = 0
            row = row + 1
        row = 0
        column = column + 1
    for i in race:
        print(i)    
        
def easier():
    letsGo(rand.randint(0,9),rand.randint(0,9),rand.choice(list))

    
checker = 0
while checker < 50:
    easier()
    time.sleep(0.5)
