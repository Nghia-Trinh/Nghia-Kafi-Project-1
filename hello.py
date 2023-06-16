"""
Date: 6/16/23
Name: Nghia Trinh
Project: Getting started with Python

This file would work to resolve the two following issues:
-Print out the data provided by yfinance.
-Return list of data based on inputed script
"""

#IMPORTED PACKAGES
import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

########################################
#                                      #
#           DATA ON YFINANCE           #
#                                      #
########################################

print(type(yf))
print(dir(yf))

########################################
#                                      #
#     RETRIEVE DATA FROM YFINANCE      #
#                                      #
########################################

##CONSTRUCTION OF VARIABLES
print("The following part will request for a stock code script that would return the list of all info.\n")
data = input("Please enter the requested stock code for the following stock info: ")
index = yf.Ticker(data)


##RETURN THE OUTPUT
print(index.info)
#print(msft.info)




