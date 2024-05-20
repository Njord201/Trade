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
        self.period = 10
        self.periodTab = [0] * (self.period + 1)

        self.dataBuy = []
        self.borneMoney = [920.0, 1100.0]
        self.stopLoss = 1050.0
        self.tradingStatus = True
