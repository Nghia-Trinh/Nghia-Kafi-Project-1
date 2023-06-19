"""
Date: 6/19/23
Name: Nghia Trinh
Project: Getting started with Python

This file would work to resolve the two following issues:
-Print out the data provided by yfinance.
-Return list of data based on inputed script
#Chuyen thanh dang data frame, luu tren github
#Bao cao theo gia hang ngay, theo phut, x
"""

#IMPORTED PACKAGES
import pandas as pd
import requests
from datetime import datetime
import yfinance as yf
import logging
import statistics


##CONSTRUCTION OF VARIABLES
print("The following script will request for a stock index that would return the list of all info.\n")
index = input("Please enter the requested stock code for the following stock info: ")
stock = yf.Ticker(index)


## RETURN THE OUTPUT OF TIME BASED DATA
print(" RETURNING THE DATA ON STOCK INDEX:",stock)
print(" THE STOCK PRICING AFTER 1 MINUTE")
print(pd.DataFrame(data=stock.history(period="1m")))
print(" THE STOCK PRICING AFTER 1 DAY")
print(pd.DataFrame(data=stock.history(period="1d")))
print(" THE STOCK PRICING AFTER 1 MONTH")
print(pd.DataFrame(data=stock.history(period="1mo")))
print(" THE STOCK PRICING AFTER 1 YEAR")
print(pd.DataFrame(data=stock.history(period="1y")))
