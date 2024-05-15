#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## receive.py
## File description:
## GroundHog
##

from src.information.weird import *

def shiftTemp(infoValue: valueHandler):
    for index in range(0, len(infoValue.periodTab) - 1, 1):
        infoValue.periodTab[index] = infoValue.periodTab[index + 1]
