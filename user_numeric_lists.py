"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics


# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [1,2,3,4,16,22,34,45,87,94,32,21,14,19,25,75,80,90,70,15,55,45,23,65]
listx = [1,2,3,4,5,6,7,8,9,10]
listy = [4,3,3,2,4,7,8,9,5,3]


# TODO: define some custom functions
def measures_of_central_tendency():
    logger.info(f"donations: {list1}")
    logger.info(f"range to 10: {listx}")

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    var = statistics.variance(list1)
    stdev = statistics.stdev(list1)

    logger.info(f"donations mean: {list1}")
    logger.info(f"donations median: {list1}")
    logger.info(f"donations mode: {list1}")

    logger.info(f"donations var: {list1}")
    logger.info(f"donations stdev: {list1}")

def correlation_and_prediction():
    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    correlationxy = statistics.correlation(listx, listy)
    
    




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("Replace this with calls to your functions." )



