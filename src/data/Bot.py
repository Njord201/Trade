#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## Trade
## File description:
## BotState
##

import sys
from src.data.BotState import *
from src.information.weird import *
from src.information.standardDeviation import *
from src.information.relativeEvolution import *
from src.information.rsi import *

class Bot:
    def __init__(self):
        self.botState = BotState()
        self.infoValue = valueHandler()

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
            print(f'Dates: [{self.botState.charts["USDT_BTC"].dates[-1]}].', file=sys.stderr)
            print(f'High: [{self.botState.charts["USDT_BTC"].highs[-1]}].', file=sys.stderr)
            print(f'Low: [{self.botState.charts["USDT_BTC"].lows[-1]}].', file=sys.stderr)
            print(f'Open: [{self.botState.charts["USDT_BTC"].opens[-1]}].', file=sys.stderr)
            print(f'Volume: [{self.botState.charts["USDT_BTC"].volumes[-1]}].', file=sys.stderr)
            print(f'current_closing_price: [{current_closing_price}].', file=sys.stderr)

            updateTab(self.infoValue, self.botState)
            # standardDeviation(self.infoValue)
            # firstdecision = calculRatioWeird(self.infoValue, current_closing_price)
            # relativeEvolution(self.infoValue)

            rsi = calculRSIDecision(self.infoValue)


            if (dollars > 0.0):
                if (rsi < 10):
                    print(f'BUY\n', file=sys.stderr)
                    print(f'buy USDT_BTC {1 * affordable}', flush=True)
                    self.infoValue.valueBuy = current_closing_price
                else:
                    print(f'NO MOVE\n', file=sys.stderr)
                    print("no_moves", flush=True)
            
            elif (btc > 0.0):
                if (rsi > 90):
                    print(f'SELL\n', file=sys.stderr)
                    print(f'sell USDT_BTC {1 * btc}', flush=True)
                    self.infoValue.valueBuy = 0
                elif (rsi > 80):
                    print(f'SELL\n', file=sys.stderr)
                    print(f'sell USDT_BTC {0.3 * btc}', flush=True)
                    self.infoValue.valueBuy = 0
                else:
                    print(f'NO MOVE\n', file=sys.stderr)
                    print("no_moves", flush=True)
            else:
                print(f'NO MOVE\n', file=sys.stderr)
                print("no_moves", flush=True)
