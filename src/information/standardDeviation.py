#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## standardDeviation.py
## File description:
## GroundHog
##

from src.information.weird import *

def standardDeviation(infoValue: valueHandler):
    if (infoValue.nbValue < infoValue.period):
        return 0

    averageValue = 0
    for index in range(0, len(infoValue.periodTab) - 1, 1):
        averageValue += infoValue.periodTab[index + 1]
    averageValue = averageValue / infoValue.period

    total = 0
    for index in range(0, len(infoValue.periodTab) - 1, 1):
        total += (infoValue.periodTab[index + 1] - averageValue) ** 2
    total = total / infoValue.period

    result = sqrt(total)
    infoValue.standardDeviation = result
    return 0
