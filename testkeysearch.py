"""
DATE STARTED: MAY 26, 2019
PURPOSE: SEARCH FOR KEYS AND RECORD THEM.
"""
# IMPORT TOOLS
#   BUILTIN TOOLS
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
    samplestr = "1402 btc"
    print("sample test string to find: ", samplestr)
    found = q.search(samplestr)
    print("Search works!  --> ", found)

    reobj = q.search(pagetext)
    if reobj != "None":
        # REPORT NEW JACKPOT URL
        jackpoturl = driver.current_url
        print("JACKPOT!  -->  ", jackpoturl)


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
#   A. OPEN STORED FILE OF VISITED PAGES
with open("visited.pkl", "rb") as targetfile:
    visited_raw = pkl.load(targetfile)

if visited_raw is None:
    # IF NONE EXISTS, CREATE OBJECT
    visited = []
else:
    visited = visited_raw
    print(type(visited))
    print("CURRENT LIST OF VISITED PAGES:\n", visited)

#   B. OPEN WEBPAGE
driver = webdriver.Firefox()
driver.get("https://keys.lol/bitcoin/random")
humanurl = driver.current_url

#   C. IF REDIRECTED, PASS TEST
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
