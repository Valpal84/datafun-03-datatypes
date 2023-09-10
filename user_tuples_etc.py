"""
Task 5- Tuples and more
Valerie Johnson
Crowdsourcing-crowdfunding
Today's date: 9/10/23

"""
# add imports

import random
import math

# add logger

from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)

# Create some tuples
# Created tuple with months in year and donations to coincide with months for the year

tuple_monthsinayear = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
tuple_donationsforyear = (0, 4500, 2700, 3000, 1200, 3500, 500, 0, 150, 7500, 250, 400)

logger.info(f"tuple_monthsinayear = {tuple_monthsinayear}")
logger.info(f"tuple_donationsforyear = {tuple_donationsforyear}")

# tuple concatenation
tuple_combined = tuple_monthsinayear + tuple_donationsforyear

# tuple repitition
tuple_monthsinayear_thrice = tuple_monthsinayear * 3


