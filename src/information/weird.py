#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## werid.py
## File description:
## GroundHog
##

import sys
from math import *

BUY = 1
SELL = 2
NOTHING = 3

class valueHandler():
    def __init__(self):
        self.period = 7
        self.periodTab = [0] * (self.period + 1)

        self.valueBuy = 0

        self.nbValue = 0
        self.allValue = []
        self.average = 0.0
        self.standardDeviation = 0.0
        self.borne = [0.0, 0.0]

def calculRatioWeird(infoValue: valueHandler, value: float):
    infoValue.average = 0
    if (infoValue.nbValue < infoValue.period):
        return 0
    infoValue.allValue.append(float(value))
    for index in range(0, len(infoValue.periodTab) - 1, 1):
        infoValue.average += infoValue.periodTab[index + 1]
    infoValue.average = infoValue.average / infoValue.period

    if (infoValue.valueBuy == 0):
        infoValue.borne[0] = infoValue.average - (2 * infoValue.standardDeviation)
        infoValue.borne[1] = infoValue.average + (2 * infoValue.standardDeviation)
    else:
        infoValue.borne[0] = infoValue.valueBuy - (2 * infoValue.standardDeviation)
        infoValue.borne[1] = infoValue.valueBuy + (2 * infoValue.standardDeviation)

    if (value < infoValue.borne[0]):
        print(f'Closing Price inférieur a borne INF | indice: [{value - infoValue.borne[0]}].', file=sys.stderr)
        infoValue.valueBuy = value
        return BUY
    elif (infoValue.borne[1] < value):
        print(f'Closing Price supérieur a borne SUP | indice: [{value}].', file=sys.stderr)
        return SELL
    elif (abs(infoValue.borne[0] - value) < abs(infoValue.borne[1] - value)):
        print(f'Closing Price entre les bornes proche de la borne INF | indice: [{abs(infoValue.borne[0] - value)}].', file=sys.stderr)
        return NOTHING
    else:
        print(f'Closing Price entre les bornes proche de la borne SUP | indice: [{abs(infoValue.borne[1] - value)}].', file=sys.stderr)
        return NOTHING
