# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:12:50 2018

@author: bjwil
"""
# imports, make sure to download gTTS wil pip
from phone import Phone, Cell, Home, ActionAndBills
from gtts import gTTS # install with pip as in $ pip install gTTS
import datetime
import calendar
from calendar import monthrange
import os
import glob
import sys
from PIL import Image
import subprocess
import time
import requests


# set current directory, make need to set this differently for mac/linux/unix
currDir = str(os.path.abspath(os.path.dirname(sys.argv[0])))
photoDir = currDir + '\\photoDownload'
# create folder for image downloads
if not os.path.exists(photoDir):
    os.makedirs(photoDir)

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?" \
            "view=co&content-type=text/plain"
response = requests.get(word_site)
WORDS = response.content.decode('utf-8').splitlines()

# instantiate Phone class object, 2 each also throuh subclasses Cell and Home
my_phones = [
        Cell("Father's Cell", "cellular", "215", 1, "James"),
        Cell("Mother's Cell", "cellular", "215", 1, "Teresa"),
        Home("Grandmom's House", "home", "610", 15, "James"),
        Cell("Stacy's Walkie Talkie", "cellular", "480", 28, "Stacy"),
        Phone("Work Fax", "Fax", "267", 15, "James"),
        Home("ET Phone Home", 
             "home", 
             "215", 
             # monthrange functions gets current month number (0-11 index) and
             # last day of the month
             monthrange(datetime.datetime.now().year, 
                        datetime.datetime.now().month)[1], 
             "Drew Barrymore"),    
        ]

# Create dictionary of photos.  Photos are a functionality of the phone
photos_ = {} 
for phone in my_phones:
    # for each instance of Phones run the photo definition under Phones class
    phone.photo(photoDir, WORDS)
    # Use glob library to find the latest file that was downloaded.
    # I did not know how to get the retrieve the from MyImageDownloader class
    # while calling the photo(def) so this was best choice
    list_of_files = glob.glob(photoDir + '\\*')
    latest_file = max(list_of_files, key=os.path.getctime)
    # Add the latest file assigned to phone name and owner in photos dict
    photos_.setdefault(phone.name_, (phone.phone_owner, latest_file))

# Use the dictionary and create MP3 to read aloud where the photo came from
# while showing the picture.
for phone_name, picture in photos_.items():
    # Create MP3 recording with Python gTTS package
    tts = gTTS(text="Showing last photo from {} owned by {}:" \
               .format(phone_name, 
                       picture[0]), 
                       lang='en')
    # Saves file to same directory you are running script from
    tts.save(phone_name + '.mp3')
    # Starts the MP3 file recording
    os.startfile(phone_name + '.mp3')
    # Prints on IDE what is being voiced over
    print("Showing last photo from {} owned by {}:".format(phone_name, 
                                                           picture[0]))
    # Open and shows the image opening while recording is playing
    try:    
        img = subprocess.Popen(["cmd", "/c", picture[1]],
                               stdout=subprocess.PIPE, shell=True)
        # waits 7.5 seconds before getting next phones picture before next loop
        time.sleep(7.5)
        img.terminate()
        img.kill()
    except:
        img = Image.open(picture[1])
        img.show()
        # waits 7.5 seconds before getting next phones picture before next loop
        time.sleep(7.5)
        img.close()
    


print("\n")    
# Instantiates Parent class object from class ActionAndBills
my_bills = ActionAndBills(my_phones)
# Iterate each phone through the dial_phone function
my_bills.dial_phone()
print()
# Calls the check_bill() function to iterate through pay_bill function in 
# Phones class
my_bills.check_bill()
print()
# Just show half of the phones's phone attributes and plan
for phones in my_phones[0::2]:
    print(phones.phone_attributes())
    print(phones.plan())


# Set dictionary to add bills still needed to be paid
bills_to_be_paid = {}
# Iterate through bill_paid boolean attribute for all phones
for phone in my_bills.bills:
    # if bill_paid True pass
    if phone.bill_paid:
        pass
    # else set phone name as key and day of month bill is due as value
    else:
        bills_to_be_paid.setdefault(phone.name_, phone.payment_date[0])

# Check is all bill_paid booleans are True         
if all([phone.bill_paid for phone in my_bills.bills]):
    print("All my bills are paid")
# If not print which phone bills are due and the current month due date.
else:
    print("All my bills are not paid.  I still have the following bills due:")
    for k, v in bills_to_be_paid.items():
        print(k, ": ", 
              calendar.month_name[datetime.datetime.now().month],
              "{},".format(v), datetime.datetime.now().year)

