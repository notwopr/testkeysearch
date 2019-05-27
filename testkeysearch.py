"""
DATE STARTED: MAY 26, 2019
PURPOSE: SEARCH FOR KEYS AND RECORD THEM.
"""
# IMPORT TOOLS
#   BUILTIN TOOLS
import tkinter as tk
from tkinter import messagebox
import pickle as pkl
#   THIRD PARTY TOOLS
from selenium import webdriver


def getpagenum():
    currenturl = driver.current_url
    pagenum = currenturl[25:]
    print(pagenum)
    return pagenum


# CLICKS ON "RANDOM LINK"  AND RECORDS NEW PAGE
def getnewpage():
    randombutton = driver.find_element_by_xpath("//*[@class='my-4']/div/a[3]")
    randombutton.click()
    pagenum = getpagenum()


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
        search()
    else:
        exit()
else:
    search()


# UNTIL ACCOUNT IS FOUND, RUN:

def search():
    # FIND UNIQUE PAGE AND RECORD IT IN HISTORY
    pagenum = getpagenum()
    while pagenum in visited:
        getnewpage()
    visited.append(pagenum)

    # SEARCH PAGE
        # RECORD WEBLINK
        # STORE UPDATED VISITED LIST TO PICKLE
        print("UPDATED VISITED LIST:\n", visited)
        with open("visited.pkl", "wb") as targetfile:
            pkl.dump(visited, targetfile, protocol=4)
        # STOP
        exit()


        # HOW TO RUN THIS IN BACKGROUND USING THE CLOUD?
