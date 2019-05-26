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

# OPEN STORED FILE OF VISITED PAGES
with open("visited.pkl", "rb") as targetfile:
    visited_raw = pkl.load(targetfile)


if history_raw is None:
    # IF NONE EXISTS, CREATE OBJECT
    visited = []
else:
    visited = history_raw
    print(type(visited))


# OPEN WEBPAGE
driver = webdriver.Firefox()
driver.get("https://keys.lol/bitcoin/random")
humanurl = driver.current_url

# IF REDIRECTED, PASS TEST
if humanurl == "https://keys.lol/are-you-human":
    print("We've been redirected to: ", humanurl)
    # WAIT UNTIL I INPUT MY CREDENTIALS
    answer = messagebox.askokcancel("Are you ready for Python to continue?")
    if answer is True:
        unique()
    else:
        exit()
else:
    unique()


# FUNCTION SEARCHES FOR UNIQUE PAGE YOU HAVEN'T VISITED, AND RECORDS NEW UNIQUE PAGE
def unique():

    # STORE NAME OF PAGE
    getpageslice()



    # IF MATCHES LIST OF VISITED PAGES,
    if sliced in visited:

        # CLICK ON "RANDOM LINK"
        randombutton = driver.find_element_by_xpath("//*[@class="my-4"]/div/a[3]")
        randombutton.click()
        getpageslice()

    # IF NOT,
    #   RECORD PAGE TO LIST OF VISITED PAGES
    else:
        visited.append(sliced)
        # RUN SEARCH()


def search():
    # SEARCH WEBPAGE
    # IF FOUND,
    if asdf :
        # RECORD WEBLINK
        # STORE UPDATED VISITED LIST TO PICKLE
        with open("tickerdb.pkl", "wb") as targetfile:
            pkl.dump(finalfile, targetfile, protocol=4)
        # STOP

    # IF NOT,
    else:

        # CLICK ON "RANDOM LINK"
        randombutton = driver.find_element_by_xpath("//*[@class="my-4"]/div/a[3]")
        randombutton.click()

        # RETURN TO

        # HOW TO RUN THIS IN BACKGROUND USING THE CLOUD?
