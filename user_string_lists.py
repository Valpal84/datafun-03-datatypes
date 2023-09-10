"""
Task 4-String lists
Valerie Johnson
Domain- Crowdsourcing -Crowdfunding -donations
Date- 09/09/2023

"""

# imports first

import random

from util_datafun_logger import setup_logger

logger, logname = setup_logger(__file__)

# String lists

list_donors = ["Brett", "Georgia", "Millie", "John", "Renee", "Keegan"]
list_donorlevel = ["Bronze", "Silver", "Gold", "Platinum", "Diamond"]
list_moneytype = ["Check", "Cash", "Credit", "Money order", "Check", "Credit"]
list_crowdfundtype = ["Reward", "Donation", "Equity", "Debt"]
list_platform = ["Kickstarter", "Patreon", "RocketHub", "Indiegogo", "GoFundMe"]

# Reusable functions next

#String Lists 1- using python built-in functions

def built_in_functions():
    len_donors = len(list_donors)
    len_donorlevel = len(list_donorlevel)
    len_moneytype = len(list_moneytype)
    len_crowdfundtype = len(list_crowdfundtype)
    len_platform = len(list_platform)

    logger.info(f"Length of donors list: {len_donors}")
    logger.info(f"Length of donor level list: {len_donorlevel}")
    logger.info(f"Length of money type list: {len_moneytype}")
    logger.info(f"Lenth of crowdfund type list: {len_crowdfundtype}")
    logger.info(f"Length of platform list: {len_platform}")

    unique_donors = set(list_donors)
    unique_donorlevel = set(list_donorlevel)
    unique_moneytype = set(list_moneytype)
    unique_crowdfundtype = set(list_crowdfundtype)
    unique_platform = set(list_platform)

    logger.info(f"unique words in donor list: {unique_donors}")
    logger.info(f"unique words in donor level list: {unique_donorlevel}")
    logger.info(f"unique words in money type list: {unique_moneytype}")
    logger.info(f"unique words in crowdfund type list: {unique_crowdfundtype}")
    logger.info(f"unique words in platform list: {unique_platform}")

    donors_and_moneytype = zip(list_donors, list_moneytype)
    donorlevel_and_platform = zip(list_donorlevel, list_platform)

    logger.info(f"Combined donors and money type lists into a tuple: {donors_and_moneytype}")
    logger.info(f"Combined donor level and platform lists into a tuple: {donorlevel_and_platform}")

# String lists 2- Random Choice

def random_choice():
    random_donors = random.choice(list_donors)
    random_donorlevel = random.choice(list_donorlevel)
    random_moneytype = random.choice(list_moneytype)
    random_crowdfundtype = random.choice(list_crowdfundtype)
    random_platform = random.choice(list_platform)

    sentence = (f"{random_donors}, has been a {random_donorlevel} donor for many years. They prefer to donate via {random_moneytype} on the {random_platform} platform and generally expect their donation to be a part of {random_crowdfundtype}.")
    logger.info(f"Generated sentence: {sentence}")

# String lists 3- Get unique words

def process_text_juliasceasar():
    logger.info(f"CALLING process_text_juliasceasar")
    with open("text_juliasceasar.txt", "r") as fileobject:
        text = fileobject.read()
        listwords = text.split()
        uniquewords = set(listwords)

        wordcount = len(listwords)
        
        logger.info(f"The list of words is: {listwords}")
        logger.info(f"There are {wordcount} words in the file.")

        uniquewordcount = len(uniquewords)

        logger.info(f"The set of unique words is: {uniquewords}")
        logger.info(f"There are {uniquewordcount} words in the file.")

def show_log():
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# call functions and execute code
# use if __name__ == "__main__":

if __name__ == "__main__":
    built_in_functions()
    random_choice()
    process_text_juliasceasar()
    show_log()
    