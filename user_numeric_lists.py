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

# Task 3 numeric lists 
# List 1: list statistics

# TODO: Create some shared data lists if you like - or just create them in your functions
list1 = [1,2,3,4,16,22,34,45,87,94,32,21,14,19,25,75,80,90,70,15,55,45,23,65]
listx = [1,2,3,4,5,6,7,8,9,10]
listy = [4,3,3,2,4,7,8,9,5,3]


# TODO: define some custom functions
def measures_of_central_tendency():
    logger.info(f"donations: {list1}")
    logger.info(f"range to 10: {listx}")

    mean1 = statistics.mean(list1)
    median1 = statistics.median(list1)
    mode1 = statistics.mode(list1)

    meanx = statistics.mean(listx)
    medianx = statistics.median(listx)
    modex = statistics.mode(listx)

    meany = statistics.mean(listy)
    mediany = statistics.median(listy)
    modey = statistics.mode(listy)

    var = statistics.variance(list1)
    stdev = statistics.stdev(list1)
    varx = statistics.variance(listx)
    stdevx = statistics.stdev(listx)
    vary = statistics.variance(listy)
    stdevy = statistics.stdev(listy)


    logger.info(f"donations mean: {list1}")
    logger.info(f"donations median: {list1}")
    logger.info(f"donations mode: {list1}")

    logger.info(f"listx mean: {listx}")
    logger.info(f"listx median: {listx}")
    logger.info(f"listx mode: {listx}")

    logger.info(f"listy mean: {listy}")
    logger.info(f"listy median: {listy}")
    logger.info(f"listy mode: {listy}")

    logger.info(f"donations var: {list1}")
    logger.info(f"donations stdev: {list1}")
    logger.info(f"listx var: {listx}")
    logger.info(f"listx stdev: {listx}")
    logger.info(f"listy var: {listy}")
    logger.info(f"listy stdev: {listy}")


#list 2- correlation and prediction

def correlation_and_prediction():
    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    correlationxy = statistics.correlation(listx, listy)
    slope, intercept = statistics.linear_regression(listx, listy)

    future_time = 15
    future_y= (slope * future_time) + intercept

    logger.info(f"correlation between x and y: {correlationxy}")
    logger.info(f"slope of listx and listy: {slope}")
    logger.info(f"intercept of listx and listy: {intercept}")
    logger.info(f"the equation of best fit line is: y={slope}x +{intercept}")
    logger.info(f"when the value of x = {future_time}, y will be approximately {future_y}")

#-lists 3 using python built in functions

def list_basic_functions():
    minimum1 = min(list1)
    minimumx = min(listx)
    minimumy = min(listy)

    maximum1 = max(list1)
    maximumx = max(listx)
    maximumy = max(listy)

    length1 = len(list1)
    lengthx = len(listx)
    lengthy = len(listy)

    sum1 = sum(list1)
    sumx = sum(listx)
    sumy = sum(listy)

    average1 = sum(list1) / len(list1)
    averagex = sum(listx) / len(listx)
    averagey = sum(listy) / len(listy)

    set1 = set(list1)
    setx = set(listx)
    sety = set(listy)

    sorted1 = sorted(list1)
    sortedx = sorted(listx)
    sortedy = sorted(listy)

    sorted_reverse1 = sorted(list1, reverse=True)
    sorted_reversex = sorted(listx, reverse=True)
    sorted_reversey = sorted(listy, reverse=True)

    logger.info(f"minimum of list 1: {minimum1}")
    logger.info(f"minimum of list x: {minimumx}")
    logger.info(f"minimum of list y: {minimumy}")
    
    logger.info(f"maximum of list 1: {maximum1}")
    logger.info(f"maximum of list x: {maximumx}")
    logger.info(f"maximum of list y: {maximumy}")

    logger.info(f"length of list 1: {length1}")
    logger.info(f"length of list x: {lengthx}")
    logger.info(f"length of list y: {lengthy}")

    logger.info(f"sum of list 1: {sum1}")
    logger.info(f"sum of list x: {sumx}")
    logger.info(f"sum of list y: {sumy}")

    logger.info(f"average of list 1: {average1}")
    logger.info(f"average of list x: {averagex}")
    logger.info(f"average of list y: {averagey}")

    logger.info(f"the set of list 1 is: {set1}")
    logger.info(f"the set of list x is: {setx}")
    logger.info(f"the set of list y is: {sety}")

    logger.info(f"list 1 sorted is: {sorted1}")
    logger.info(f"list x sorted is: {sortedx}")
    logger.info(f"list y sorted is: {sortedy}")

    logger.info(f"list 1 reversed is: {sorted_reverse1}")
    logger.info(f"list x reversed is : {sorted_reversex}")
    logger.info(f"list y reversed is: {sorted_reversey}")

# list 4- list methods

def list_methods():
    lst = [6,3,2,7,4]

    logger.info(f"lst short list = {lst}")

    lst.append(5)
    logger.info(f"after append(5), lst short list ={lst}")

    lst.extend([8,1,9])
    logger.info(f"after extend([8,1,9]), lst short list={lst}")

    lst.insert(2,11)
    logger.info(f"after insert(2,11), lst short list ={lst}")

    lst.remove(5)
    logger.info(f"after removing(5), lst short list = {lst}")

    count2 = lst.count(2)
    logger.info(f"count of 2 in lst = {count2}")

    lst.sort()
    logger.info(f"after list sort(), lst short list = {lst}")

    lst.sort(reverse=True)
    logger.info(f"after reverse list sort(reverse=True), lst short list = {lst}")

    lstcopy = lst.copy()
    logger.info(f"copy of lst short list = {lstcopy}")

    popfirstitem = lst.pop(0)
    logger.info(f"after popping first item from lst {popfirstitem}, lst short list = {lst}")

    poplast = lst.pop(-1)
    logger.info(f"after popping last item from lst {poplast}, lst short list = {lst}")

# list 5- transformations using filter and map

def apply_filter_and_map():
    filterlist1 = list(filter(lambda x: x < 4, list1))
    logger.info(f"filtered list (x < 4): {filterlist1}")

    cubedrootlist = list(map(lambda x: math.pow(x,1/3), list1))
    logger.info(f"cubed root list: {cubedrootlist}")

    cubedvolumelist = list(map(lambda x: x * x * x, list1))
    logger.info(f"cubed volume list: {cubedvolumelist}")

# list 6- list transformations using list comprehension

def apply_list_comprehension():
    filteredlistcomprehension = [x for x in list1 if x < 4]
    logger.info(f"filtered list comprehension (x < 4), {filteredlistcomprehension}")

    triplelistcomprehension = [x * 3 for x in list1]
    logger.info(f"triple list comprehension (x * 3), {triplelistcomprehension}")

    customlistcomprehension = [x * 2 for x in list1]
    logger.info(f"custom list comprehension (x * 2), {customlistcomprehension}")


def show_log():
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())



# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":
    logger.info(f"CALLING measures of central tendency")
    measures_of_central_tendency()

    logger.info(f"CALLING correlation and prediction")
    correlation_and_prediction()

    logger.info(f"CALLING list basic functions")
    list_basic_functions()

    logger.info(f"CALLING list methods")
    list_methods()

    logger.info(f"CALLING apply filter and map")
    apply_filter_and_map()

    logger.info(f"CALLING apply list comprehension")
    apply_list_comprehension()

    show_log()
    


