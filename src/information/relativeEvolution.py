#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## relativeEvolution.py
## File description:
## GroundHog
##

from src.information.weird import *

def relativeEvolution(infoValue: valueHandler):
    for buy in infoValue.dataBuy:
        firstTemp = buy[0]
        lastTemp = infoValue.periodTab[infoValue.period -1]
        result = (lastTemp - firstTemp)
        if (firstTemp != 0):
            result = result / firstTemp
        result = result * 100
        result = round(result)
        buy[2] = result
        print(buy, file=sys.stderr)
    return 0


def relativePeriodEvolution(infoValue: valueHandler):
    firstTemp = infoValue.periodTab[0]
    lastTemp = infoValue.periodTab[infoValue.period -1]
    result = (lastTemp - firstTemp)
    if (firstTemp != 0):
        result = result / firstTemp
    result = result * 100
    result = round(result)
    print(f'relativePeriodEvolution: {result}', file=sys.stderr)
    return result
