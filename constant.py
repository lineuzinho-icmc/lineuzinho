import os
import sys

if __name__ == "__main__":
    try:
        with open("safe.txt",'w',encoding = 'utf-8') as f:
            f.write(sys.argv[1])
    except:
    	print("Please, add API key to console call")
        
safe = open("safe.txt", "r")
api = safe.read()

sheet = "https://docs.google.com/spreadsheets/d/1Kfy-tCDA_UggPUOaYs1w9oN_DtuL6GBWPyCmcl_R3f8/edit?usp=sharing"
github = "https://github.com/lineuzinho-icmc/lineuzinho"
docs = "https://t.me/docs21"
