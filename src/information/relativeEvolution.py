#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## relativeEvolution.py
## File description:
## GroundHog
##

from src.information.weird import *

def relativeEvolution(infoValue: valueHandler):
    if (infoValue.nbValue < infoValue.period + 1):
        return 0

    firstTemp = infoValue.periodTab[0]
    lastTemp = infoValue.periodTab[infoValue.period]
    result = (lastTemp - firstTemp)
    if (firstTemp != 0):
        result = result / firstTemp
    result = result * 100
    result = round(result)
    print(f'relativeEvolution: [{result}].', file=sys.stderr)
    return 0
