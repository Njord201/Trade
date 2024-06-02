#!/usr/bin/env python3
##
## EPITECH PROJECT, 2024
## Trade
## File description:
## BotState
##

import sys
from src.data.BotState import *
from src.information.valueHandler import *
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
            # print(f'Dates: [{self.botState.charts["USDT_BTC"].dates[-1]}].', file=sys.stderr)
            # print(f'High: [{self.botState.charts["USDT_BTC"].highs[-1]}].', file=sys.stderr)
            # print(f'Low: [{self.botState.charts["USDT_BTC"].lows[-1]}].', file=sys.stderr)
            # print(f'Open: [{self.botState.charts["USDT_BTC"].opens[-1]}].', file=sys.stderr)
            # print(f'Volume: [{self.botState.charts["USDT_BTC"].volumes[-1]}].', file=sys.stderr)
            print(f'current_closing_price: [{current_closing_price}].', file=sys.stderr)

            updateTab(self.infoValue, self.botState)
            relativeEvolution(self.infoValue)

            rsi_10 = calculRSIDecision(self.infoValue)
            self.infoValue.period = 15
            updateTab(self.infoValue, self.botState)
            rsi_15 = calculRSIDecision(self.infoValue)
            self.infoValue.period = 10
            updateTab(self.infoValue, self.botState)

            virtuelMoney = dollars + sellable

            buyStatus = False
            sellStatus = False
            stopLossStatus = False

            # Check if borne needed update
            if (self.infoValue.tradingStatus == True and virtuelMoney > self.infoValue.borneMoney[1]):
                self.infoValue.borneMoney[0] = self.infoValue.borneMoney[1] - 80
                self.infoValue.borneMoney[1] += 50

            # Check if crossing the lower one
            if (self.infoValue.tradingStatus == True and virtuelMoney < self.infoValue.borneMoney[0]):
                print(f'SELL: {btc}', file=sys.stderr)
                print(f'sell USDT_BTC {btc}', flush=True)
                self.infoValue.tradingStatus = False
                stopLossStatus = True
                while self.infoValue.dataBuy:
                    self.infoValue.dataBuy.pop()


            print(f'virtuelMoney: {virtuelMoney}', file=sys.stderr)
            print(f'self.infoValue.borneMoney[0]: {self.infoValue.borneMoney[0]}', file=sys.stderr)
            print(f'self.infoValue.borneMoney[1]: {self.infoValue.borneMoney[1]}\n', file=sys.stderr)


            if (stopLossStatus == False and rsi_10 < 8):
                self.infoValue.tradingStatus = True
                self.infoValue.borneMoney[0] = self.infoValue.borneMoney[1] - 20
                self.infoValue.borneMoney[1] += 50

            # Sell if: Trading
            if (self.infoValue.tradingStatus == True and btc >= 0.0001):

                btcToSell = 0.0
                index = 0
                while index < len(self.infoValue.dataBuy):
                    buy = self.infoValue.dataBuy[index]
                    if (buy[2] >= 10):
                        sellStatus = True
                        btcToSell += buy[1]
                        del self.infoValue.dataBuy[index]
                    elif (buy[2] <= -5):
                        sellStatus = True
                        btcToSell += buy[1]
                        del self.infoValue.dataBuy[index]
                    else:
                        index += 1

                if (sellStatus == True):
                    print(f'SELL\n', file=sys.stderr)
                    print(f'sell USDT_BTC {btcToSell}', flush=True)

            # Buy if: Trading | not sell
            if (self.infoValue.tradingStatus == True and sellStatus == False and dollars >= 0.1):

                if (rsi_10 < 30):
                    buyStatus = True
                    print(f'BUY\n', file=sys.stderr)
                    print(f'buy USDT_BTC {1 * affordable}', flush=True)
                    self.infoValue.dataBuy.append([current_closing_price, (0.6 * affordable) * 0.998, 0])

                if (rsi_15 > 73):
                    buyStatus = True
                    print(f'BUY 15\n', file=sys.stderr)
                    print(f'buy USDT_BTC {1 * affordable}', flush=True)
                    self.infoValue.dataBuy.append([current_closing_price, (0.01 * affordable) * 0.998, 0])

            # Do nothing if: not sell | not buy | not stop loss
            if (stopLossStatus == False and sellStatus == False and buyStatus == False):
                print(f'NO MOVE\n', file=sys.stderr)
                print("no_moves", flush=True)
