# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:12:50 2018

@author: bjwil
"""

import datetime
###############################################
'''install icrawler with pip as in $ pip install icrawler
or with Anaconda as in $ conda install -c hellock icrawler
'''
from icrawler.builtin import GoogleImageCrawler 
from icrawler import ImageDownloader
###############################################
import random
from six.moves.urllib.parse import urlparse
import textwrap

# Overide the ImageDownloader class from icrawler package.
# Source: https://github.com/hellock/icrawler/issues/34
class MyImageDownloader(ImageDownloader):
    
    def __init__(self, *args, **kwargs):
        super(MyImageDownloader, self).__init__(*args, **kwargs)
        # This was the variable I needed to created from my e-mail
        self.prefix_name = ''
    
    # Basically everything in this definition up to initializing filename
    # was taken from definition in ImageDownloader of standar library
    def get_filename(self, task, default_ext):
        url_path = urlparse(task['file_url'])[2]
        if '.' in url_path:
            extension = url_path.split('.')[-1]
            if extension.lower() not in [
                    'jpg', 'jpeg', 'png', 'bmp', 'tiff', 'gif', 'ppm', 'pgm'
            ]:
                extension = default_ext
        else:
            extension = default_ext
        filename = self.prefix_name
        # Returns prefix name which will equal phone.name_ in photo function
        # plus underscore, random 7 digit number, & file extension for filename
        return '{}{}{}.{}'.format(filename, "_", 
                                    str(random.randint(1,9999999)), extension)

# Created another Parent Class that will iterate through two definitions
# of the Phone class.  Wanted to try this from the tutorial.
class ActionAndBills:
    
    # Instantiate list of phones
    bills = []
    
    # Initialize bill attribute
    def __init__(self, bills):
        self.bills = bills
    
    # Def to loop through phone bills
    def check_bill(self):
        for bill in self.bills:
            print(bill.pay_bill())
    
    # Def to loop through dialng phones
    def dial_phone(self):
        for bill in self.bills:
            print(bill.dial_phone())
    
# Parent phone class which gives all attribute to phones
class Phone(object):
    
    # Initialize all attributes        
    def __init__(self, name_, type_, area_code, payment_date, phone_owner):
        self.name_ = name_
        self.type_ = type_
        self.area_code = area_code
        self.payment_date = payment_date,
        self.phone_owner = phone_owner
        self.bill_paid = False
    
    # Def to return attributes of each class object created
    def phone_attributes(self):
        return (self.name_, self.type_, 
                self.area_code, self.payment_date, 
                self.phone_owner)
    
    # Def to return dialing for each class object created
    def dial_phone(self):
        if self.type_.lower() != 'fax': 
            return ("Dialing ... " + self.name_)
        else:
            return ("Oops! Cannot dial a {}.".format(self.type_))
    
    # Def to return when bill was paid for each class object created
    def pay_bill(self):
        suffix = 'th.'
        if (str(self.payment_date[0])[-1] == '1' and 
            (self.payment_date[0] < 11 or self.payment_date[0] > 13)):
            suffix = 'st.'
        elif (str(self.payment_date[0])[-1] == '2' and 
              (self.payment_date[0] < 11 or self.payment_date[0] > 13)):
            suffix = 'nd.'
        elif (str(self.payment_date[0])[-1] == '3' and 
              (self.payment_date[0] < 11 or self.payment_date[0] > 13)):
            suffix = 'rd.'
        if datetime.datetime.now().day >= self.payment_date[0]:
            self.bill_paid = True
            return "The payment date for %s has passed and the bill was " \
            "paid by %s on the %s" % (self.name_,
                                      self.phone_owner, 
                                      self.payment_date[0]) \
                                      + suffix
        else:
            self.bill_paid = False
            return "The payment date for %s has not passed yet. The bill " \
            "will be paid by %s on the %s" % (self.name_,
                                              self.phone_owner, 
                                              self.payment_date[0]) \
                                              + suffix

    # The MAJOR FUN def to search Google for the photo functionality of phone
    def photo(self, photoDir, WORDS):  
        # Creates instance of Class object GoogleImageCrawler under icrawler >
        # builtin > google.py file and passes MyImageDowloader class as the
        # downloader class instead of standard library's ImageDownloader class
        google_crawler = GoogleImageCrawler(
                downloader_cls = MyImageDownloader, 
                parser_threads=2, 
                downloader_threads=4,
                # stores the file where user indicates in script argument
                storage={'root_dir': photoDir})
        # This was the key statement that will assign the name_ of the phone
        # to the beginning of the filename for the photo downloaded
        google_crawler.downloader.prefix_name = self.name_
        # Set session.verify = False work around for excpetion from requests 
        # found here: https://github.com/hellock/icrawler/issues/40
        google_crawler.session.verify = False
        # Get a random word from the list of WORDS passed
        word = random.choice(WORDS)
        # Actual call to crawl method to scrape Google images
        google_crawler.crawl(keyword=word, max_num=1)
        # Print location which was passed by script to function
        print(textwrap.dedent(
            """
            File has been downloaded to:
                {}""".format(photoDir)
        ))
    
    # Def to return plan for each class object created. Child classes override
    def plan(self):
        return "%s is a %s and has a %s plan." % (self.name_, 
                                                  self.type_, 
                                                  self.type_)

# Sub classes which override phone plans statements.  Basically not needed
# but wanted to create Child class like in the tutorial.
class Cell(Phone):
    
    def plan(self):
        return "%s is a %s and has a mobile plan." % (self.name_, 
                                                      self.type_)


class Home(Phone):

    def plan(self):
        return "%s is a %s and has a basic home plan." % (self.name_, 
                                                          self.type_)



