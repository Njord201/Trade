#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## Trade
## File description:
## BotState
##

import sys
from src.data.BotState import *

class Bot:
    def __init__(self):
        self.botState = BotState()

    def run(self):
        while True:
            reading = input()
            if len(reading) == 0:
                continue
            self.parse(reading)

    def parse(self, info: str):
        tmp = info.split(" ")
        if tmp[0] == "settings":
            self.botState.update_settings(tmp[1], tmp[2])
        if tmp[0] == "update":
            if tmp[1] == "game":
                self.botState.update_game(tmp[2], tmp[3])
        if tmp[0] == "action":
            dollars = self.botState.stacks["USDT"]
            btc = self.botState.stacks["BTC"]
            current_closing_price = self.botState.charts["USDT_BTC"].closes[-1]
            affordable = dollars / current_closing_price
            sellable = btc * current_closing_price
            print(f'My stacks in dollars are {dollars}. The current closing price is {current_closing_price}. So I can afford {affordable}', file=sys.stderr)
            print(f'My stacks in BTC are {btc}. The current closing price is {current_closing_price}. So I can sell {sellable}', file=sys.stderr)
            print(f'current_closing_price: [{current_closing_price}].', file=sys.stderr)
