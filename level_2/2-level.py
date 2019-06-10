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
response = None
url = 'http://158.69.76.135/level2.php'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
"""
headers = {
                'User-Agent': user_agent,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'de,en-US;q=0.8,en;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                'User-Agent': user_agent,
                'Cookie': '',
                'Upgrade-Insecure-Requests': '1'}
"""
s = requests.Session()
"""
s.proxies = {'http': '91.214.70.99:3128',
                    'http': '159.203.118.239:8080',}
s.headers = headers
"""
while votes <= 1022:
    response = requests.get(url, user_agent)
    soup = BeautifulSoup(response.text, "html.parser")
    text = str(soup.findAll('tr')[45])
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
    br = RoboBrowser(session=s, user_agent=user_agent, history=True)
    br.open(url)
    form = br.get_form()
    br.session.headers['Referer'] = url
    form['id'].value = 733
    br.submit_form(form, response)
    tmp += 1
    if tmp == 30:
        time.sleep(1)
        tmp = 0
print("Finish! {} votes".format(votes+1))
