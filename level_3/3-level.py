#!/bin/bash/python3
""" """
import requests
import time
import re
import cv2
import pytesseract
from random import randint
from robobrowser import RoboBrowser
from pytesseract import image_to_string
from PIL import Image
from seleniumwire import webdriver
from seleniumrequests import Firefox
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options

count = 0
ini = ''
votes = 0
tmp = 0
response = None
url = 'http://158.69.76.135/level3.php'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
user_agent2 = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
iprox = ["74.91.20.42", "104.248.115.236", "162.243.108.129"]
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

s = requests.Session()

options_s = {
    'proxy': {
        'http': '91.214.70.99:3128',
        'http': '159.203.118.239:8080',
        'no_proxy': 'localhost,127.0.0.1:80',}}
"""
while votes <= 1022:
    response = requests.get(url, user_agent)
    soup = BeautifulSoup(response.text, "html.parser")
    text = str(soup.findAll('tr')[22])
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
    try:
        binary = FirefoxBinary('/home/vagrant/geckodriver')
        options = Options()
        options.headless=True
        profile = webdriver.FirefoxProfile()
        profile.set_preference("network.proxy.type.override", 1)
        profile.set_preference("network.proxy.http.override", iprox[randint(0,2)])
        profile.set_preference("network.proxy.http_port.override", int("8080"))
        profile.set_preference("general.useragent.override", user_agent)
        browser = webdriver.Firefox(profile, options=options, executable_path='/home/vagrant/geckodriver')
        browser.header_overrides = {'Referer': url, 'User-Agent': user_agent,}
        browser.get(url)
        captcha = browser.find_element_by_xpath("//form[1]/img[1]")
        captcha.screenshot("shot.png")
        img = cv2.imread("shot.png")
        textc = image_to_string(img)
        print(textc)
        text2 = ''
        for i in textc:
            if i == 'p':
                text2 += 'f'
            if i == 'P':
                text2 += 'F'
            if i == 'f':
                text2 += 'p'
            if i == 'F':
                text2 += 'P'
            text2 += i
        sid = browser.find_element_by_name(name='id')
        sid.send_keys("733")
        tcapt = browser.find_element_by_name(name='captcha')
        tcapt.send_keys(text2)
        submit = browser.find_element_by_name(name="holdthedoor")
        """
        time.sleep(0.5)
        """
        submit.click()
        browser.close()
    except:
        continue
print("Finish! {} votes".format(votes+1))
