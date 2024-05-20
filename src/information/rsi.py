#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## werid.py
## File description:
## GroundHog
##

import sys
from math import *
from information.valueHandler import *
from src.data.BotState import *

BUY = 1
SELL = 2
NOTHING = 3

def updateTab(infoValue: valueHandler, botState: BotState):
    indexCloses = -1
    for index in range((infoValue.period - 1), -1, -1):
        infoValue.periodTab[index] = botState.charts["USDT_BTC"].closes[indexCloses]
        indexCloses -= 1

def calculRSIDecision(infoValue: valueHandler):
    Hx = 0
    Bx = 0
    pred = infoValue.periodTab[0]
    for index in range(1, len(infoValue.periodTab) - 1, 1):
        if (pred <= infoValue.periodTab[index]):
            Hx += (infoValue.periodTab[index] - pred)
        else:
            Bx += (infoValue.periodTab[index] - pred)
        pred = infoValue.periodTab[index]

    Hx = Hx / infoValue.period
    Bx = Bx / infoValue.period
    rsi = 100 * Hx / (Hx - Bx)
    print(f'rsi: [{rsi}].', file=sys.stderr)
    return rsi
