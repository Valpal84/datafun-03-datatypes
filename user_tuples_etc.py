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

def illustrate_tuples():

  tuple_monthsinayear = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
  tuple_donationsforyear = (0, 4500, 2700, 3000, 1200, 3500, 500, 0, 150, 7500, 250, 400)

  logger.info(f"tuple_monthsinayear = {tuple_monthsinayear}")
  logger.info(f"tuple_donationsforyear = {tuple_donationsforyear}")

# tuple concatenation
  tuple_combined = tuple_monthsinayear + tuple_donationsforyear

# tuple repitition
  tuple_monthsinayear_thrice = tuple_monthsinayear * 3

# use syntactic sugar
  logger.info(f"{tuple_monthsinayear = }")
  logger.info(f"{tuple_donationsforyear = }")
  logger.info(f"{tuple_combined = }")
  logger.info(f"{tuple_monthsinayear_thrice = }")

# Illistrate sets, create two sets and get the intersection and union

def illustrate_sets():
  set_firsthalf = {1, 2, 3, 4, 5, 6, 7}  
  set_secondhalf = {6, 7, 8, 9, 10, 11, 12}

  logger.info(f"{set_firsthalf = }")
  logger.info(f"{set_secondhalf = }")

  # set union
  set_union = set_firsthalf | set_secondhalf

  # set intersection
  set_intersection = set_firsthalf & set_secondhalf

  logger.info(f"{set_union = }")
  logger.info(f"{set_intersection = }")

# use a dictionary to create key-value pairs of each word and its count from a file

def illustrate_dictionaries():
  with open("text_zen_of_python.txt") as file_object:
    wordlist = file_object.read().split()

  word_counts_dict = {}
  for word in wordlist:
    if word in word_counts_dict:
      word_counts_dict[word] += 1
    else: word_counts_dict[word] = 1

    logger.info(f"Given text_zen_of_python.txt, the word_counts_dict = {word_counts_dict}")

 # The preferred method of word count in dictionaries
  word_counts_dict2 = {word: wordlist.count(word) for word in wordlist}

  logger.info(f"The word_counts_dict2 = {word_counts_dict2}")

# sorting by value
  sorted_wordcount = {k: v for k, v in sorted(word_counts_dict.items(), key=lambda item: item[1], reverse=True)}
  logger.info(f"Word frequency: {sorted_wordcount}")


# -------------------------------------------------------------
# Call some functions and execute code!

def show_log():
  with open(logname, "r") as file_wrapper:
    print(file_wrapper.read())

if __name__ == "__main__":
  illustrate_tuples()
  illustrate_sets()
  illustrate_dictionaries()
  show_log()

  






