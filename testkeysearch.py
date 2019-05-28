"""
DATE STARTED: MAY 26, 2019
PURPOSE: SEARCH FOR KEYS AND RECORD THEM.
"""
# IMPORT TOOLS
#   BUILTIN TOOLS
import os
from tkinter import messagebox
import re
import pickle as pkl

#   THIRD PARTY TOOLS
from selenium import webdriver


# RECORD NEW JACKPOT URL TO JACKPOTS FILE AND EXIT PROGRAM
def record_jackpot(jackpoturl):

    # SEARCH FOR EXISTENCE OF JACKPOT PICKLE FILE
    jackpotlist = []
    for f_name in os.listdir("F:\\Google Drive\\Goals\\Random Projects\\testkeysearch\\"):
        if f_name.startswith("jackpotlist"):
            print("Jackpot File Found!")

            # OPEN STORED JACKPOT FILE AND STORE CONTENTS AS LIST OBJECT
            with open("jackpotlist.pkl", "rb") as targetfile:
                jackpotlist_raw = pkl.load(targetfile)
            jackpotlist = jackpotlist_raw
            print("Jackpot Data Type: ", type(jackpotlist))
            print("CURRENT LIST OF JACKPOTS:\n", jackpotlist)

    # IF NONE EXISTS, REPORT SO
    if len(jackpotlist) == 0:
        print("No Jackpot pickle file found.")

    # ADD NEW JACKPOT URL TO LIST AND STORE UPDATED LIST TO PICKLE
    jackpotlist.append(jackpoturl)
    print("JACKPOTLIST NEW ADDITION: ", jackpoturl)
    print("UPDATED LIST OF JACKPOTS:\n", jackpotlist)
    with open("jackpotlist.pkl", "wb") as targetfile:
        pkl.dump(jackpotlist, targetfile, protocol=4)

    exit()


# SEARCH PAGE FOR JACKPOTS
def searchtext():
    # SEARCH PAGE FOR ANY "X btc" where X is any number (float or integer) > 0.
    pagetext = "awevaweibnvaoiew aefna eiowf awenin oiaeion 294120 btc ag4ha348fhewufawug" #driver.find_element_by_tag_name("body").text
    print("Pagetext type:", type(pagetext))
    found = (
        re.findall(" [0-9]*[1-9] btc", pagetext)
        + re.findall(" [0-9]*[1-9]0+ btc", pagetext)
        + re.findall(" \.[0-9]+ btc", pagetext)
        + re.findall(" [0-9]+\.[0-9]+ btc", pagetext)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+ btc", pagetext)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\. btc", pagetext)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\.[0-9]+ btc", pagetext)
    )
    # IF JACKPOT FOUND, REPORT IT AND RECORD IT
    if len(found) != 0:
        jackpoturl = driver.current_url
        print("JACKPOT!  -->  ", jackpoturl)
        record_jackpot(jackpoturl)
    # OTHERWISE, REPORT THAT JACKPOT WAS NOT FOUND
    else:
        print("NO POSITIVE BTC ACCOUNT BALANCES FOUND! :_(")


# CHECK IF CURRENT PAGE HAS ALREADY BEEN VISITED
def checkifvisited():
    currenturl = driver.current_url
    pagenum = currenturl[25:]
    print("Current URL: ", pagenum)

    # SEARCH FOR EXISTENCE OF VISITED PAGES PICKLE FILE
    visited = []
    for f_name in os.listdir("F:\\Google Drive\\Goals\\Random Projects\\testkeysearch\\"):

        # IF EXISTS, OPEN STORED FILE OF VISITED PAGES AND STORE CONTENTS AS LIST OBJECT
        if f_name.startswith("visited"):
            print("Visited Pages File Found!")
            with open("visited.pkl", "rb") as targetfile:
                visited_raw = pkl.load(targetfile)
            visited = visited_raw
            print("VISITED DATA TYPE: ", type(visited))
            print("CURRENT LIST OF VISITED PAGES:\n", visited)

    # IF NONE EXISTS, REPORT SO
    if len(visited) == 0:
        print("No visited pages pickle file found.")

    # IF CURRENT PAGE NOT VISITED BEFORE, ADD PAGE TO VISITED PAGES PICKLE FILE
    if pagenum not in visited:
        visited.append(pagenum)
        print("UPDATED VISITED LIST:\n", visited)
        with open("visited.pkl", "wb") as targetfile:
            pkl.dump(visited, targetfile, protocol=4)
    # AND RETURN BOOLEAN
        return False
    # OTHERWISE JUST RETURN BOOLEAN
    else:
        return True


def getnewpage():
    randombutton = driver.find_element_by_xpath("//*[@class='my-4']/div/a[3]")
    randombutton.click()


def jackpotsearch():
    '''
    counter = 0
    while True:
        print("TRIAL ", counter)
    '''
    for i in range(1, 11):
        print("TRIAL ", i)
        boolean = checkifvisited()
        print("Have we visited the current page? ", boolean)
        if boolean is False:
            searchtext()
            getnewpage()
        else:
            getnewpage()
    #   counter += 1


# EXECUTION BEGINS HERE
driver = webdriver.Firefox()
driver.get("https://keys.lol/bitcoin/random")
humanurl = driver.current_url

# IF REDIRECTED, PASS TEST, THEN RUN REMAINDER OF PROGRAM
if humanurl == "https://keys.lol/are-you-human":
    print("We've been redirected to: ", humanurl)
    # WAIT UNTIL I INPUT MY CREDENTIALS
    answer = messagebox.askokcancel("Are you ready for Python to continue?")
    if answer is True:
        jackpotsearch()
    else:
        exit()
else:
    jackpotsearch()


# ISSUES TO ADDRESS:
#   how to run this in background using the cloud?
#   visited pages may have new balances after you have visited them.
''' REGEX BELOW CAPTURES ANY REAL NUMBER INTEGERS, OR FLOATS INCLUDING COMMA NOTATION
    samplestr = "aerbaer regae4tnb4a3t34na34an a4 12,524,675.00 btcaw4nta4ta 4w"
    print("sample test string to search: ", samplestr)
    found = (
        re.findall(" [0-9]+ btc", samplestr)
        + re.findall(" \.[0-9]+ btc", samplestr)
        + re.findall(" [0-9]+\. btc", samplestr)
        + re.findall(" [0-9]+\.[0-9]+ btc", samplestr)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+ btc", samplestr)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\. btc", samplestr)
        + re.findall("[0-9]{1,3}(?:,[0-9]{3})+\.[0-9]+ btc", samplestr)
    )
    print("found= ", found)
'''
