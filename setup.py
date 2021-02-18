import os
import sys
try:
    import pandas
    import bs4
    import matplotlib
    import scipy
    import numpy
except ImportError:
    answer=input("You don't have the necessessary libraries that our program uses.\nWould you like to install them (Enter Y or N):")
    while True:
        if answer.upper()=="N":
            print("Alright, but the program will not work")
            break
        elif answer.upper()=="Y":
            os.system("pip install pandas")
            os.system("pip install pandas-datareader")
            os.system("pip install bs4")
            os.system("pip install matplotlib")
            os.system("pip install scipy")
            os.system("pip install numpy")
            print("All imports have been installed\nNow deleting this file")
            os.remove(sys.argv[0])
            break
        else:
            answer=input("You don't have the necessessary libraries that our program uses.\nWould you like to install them (Enter Y or N):")


