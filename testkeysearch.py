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


# FIND UNIQUE PAGE AND RECORD IT IN HISTORY
def getnewpage(visited):
    currenturl = driver.current_url
    pagenum = currenturl[25:]
    while pagenum in visited:
        randombutton = driver.find_element_by_xpath("//*[@class='my-4']/div/a[3]")
        randombutton.click()
    visited.append(pagenum)


def churn():

    # GET UNIQUE PAGE
    getnewpage(visited)

    # SEARCH PAGE
    pagetext = driver.find_element_by_tag_name("body").text
    print(pagetext)
    q = re.compile('[1-9]+ btc')

    # TEST WHETHER REGEX WORKS
    samplestr = "aerbaer regae4tnb4a3t34na34an a4 1,014.020 btcaw4nta4ta 4w"
    print("sample test string to search: ", samplestr)
    found = re.findall('[1-9]+ btc', samplestr)
    print("found= ", found)

    found = re.findall('[1-9]+ btc', pagetext)
    print("FOUND STRING MATCH:", found)
    if len(found) != 0:
        # REPORT NEW JACKPOT URL
        jackpoturl = driver.current_url
        print("JACKPOT!  -->  ", jackpoturl)
    else:
        print("NO POSITIVE BTC ACCOUNT BALANCES FOUND! :_(")


def record_jackpot(jackpoturl):

    # OPEN STORED FILE OF JACKPOT PAGES
    with open("jackpots.pkl", "rb") as targetfile:
        jackpots_raw = pkl.load(targetfile)
    if jackpots_raw is None:
        # IF NONE EXISTS, CREATE OBJECT
        jackpotlist = []
    else:
        jackpotlist = jackpots_raw
        print(type(jackpotlist))
        print("CURRENT LIST OF JACKPOT PAGES:\n {}\n\n".format(jackpotlist))

    # ADD NEW JACKPOT URL TO LIST AND STORE UPDATED LIST TO PICKLE
    jackpotlist.append(jackpoturl)
    with open("jackpots.pkl", "wb") as targetfile:
        pkl.dump(jackpotlist, targetfile, protocol=4)

    # STORE UPDATED VISITED LIST TO PICKLE
    print("UPDATED VISITED LIST:\n", visited)
    with open("visited.pkl", "wb") as targetfile:
        pkl.dump(visited, targetfile, protocol=4)
    # STOP
    exit()


def jackpotsearch():
    jackpoturl = ""
    # UNTIL ACCOUNT IS FOUND, RUN:
    while jackpoturl == "":
        churn()
    record_jackpot(jackpoturl)


# EXECUTION BEGINS HERE
# I. PREP STAGE

#   A. SEARCH FOR EXISTENCE OF PICKLE FILE
#       1. SEARCH FILE AND DIR NAMES FOR THE VISITED PAGES FILE
visited = []
for f_name in os.listdir('F:\\Google Drive\\Goals\\Random Projects\\testkeysearch\\'):
    if f_name.startswith('visited'):
        print("Visited Pages File Found!")

    #       a. OPEN STORED FILE OF VISITED PAGES AND STORE AS OBJECT
        with open("visited.pkl", "rb") as targetfile:
            visited_raw = pkl.load(targetfile)
        visited = visited_raw
        print(type(visited))
        print("CURRENT LIST OF VISITED PAGES:\n", visited)

    #       b. IF NONE EXISTS, CREATE OBJECT
if len(visited) == 0:
    print("No visited pages pickle file found. Creating new list...")

#   B. OPEN WEBPAGE
driver = webdriver.Firefox()
driver.get("https://keys.lol/bitcoin/random")
humanurl = driver.current_url

#   C. IF REDIRECTED, PASS TEST, THEN RUN REMAINDER OF PROGRAM
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
# fix regex search to find "{} btc" where {} is not " 0"
