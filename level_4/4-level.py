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
tmp = 90
response = None
url = 'http://158.69.76.135/level4.php'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0'
user_agent2 = 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)'
iprox = ["49.49.226.36", "179.152.246.95", "103.103.88.91", "142.93.59.240",
        "165.227.71.172", "93.188.165.217", "93.188.165.80", "142.93.78.113",
        "134.209.0.195", "103.56.30.128", "202.166.220.233", "202.136.90.126",
        "200.222.46.130", "45.250.226.47", "103.117.228.22", "180.254.155.118",
        "88.198.24.108", "74.91.20.42", "134.119.205.244", "125.27.251.243",
        "36.74.21.17", "27.145.231.244", "190.110.114.184", "49.0.170.202",
        "109.166.89.125", "181.176.161.19", "177.241.244.214", "103.252.117.100",
        "185.132.178.210", "93.99.179.233", "217.182.51.229", "81.183.228.106",
        "137.59.51.153", "176.115.197.118", "203.190.54.50", "201.49.110.44",
        "202.129.1.66", "211.21.120.163", "14.207.175.245", "36.91.144.227",
        "103.84.39.34", "88.255.65.111", "103.138.62.38", "203.166.200.90",
        "124.122.8.243", "176.9.115.21", "103.129.152.142", "203.192.199.70",
        "94.28.77.182", "177.70.144.30", "185.35.161.110", "96.9.79.218",
        "177.8.216.106", "103.23.32.78", "103.85.197.37", "223.205.216.51",
        "217.182.120.161", "88.205.171.222", "113.53.47.159", "185.20.163.137",
        "189.199.186.107", "177.185.159.62", "134.119.205.247", "103.47.93.102",
        "187.84.91.84", "89.102.2.149", "103.227.19.30", "196.27.106.112",
        "117.102.94.186", "186.192.17.242", "203.130.227.189", "176.35.250.108",
        "183.88.217.214", "205.196.185.218", "191.102.76.170", "125.164.166.21",
        "190.92.72.110", "112.78.185.50", "200.188.151.212", "197.45.109.123",
        "181.188.166.82", "213.109.234.4", "103.252.117.225", "185.72.111.249",
        "200.229.236.185", "201.20.89.126", "125.166.110.189", "45.235.10.125",
        "89.223.66.4", "45.232.9.32", "103.215.177.183"]

while votes <= 1022:
    response = requests.get(url, user_agent)
    soup = BeautifulSoup(response.text, "html.parser")
    text = str(soup.findAll('tr')[23])
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
        profile.set_preference("network.proxy.http.override", iprox[tmp])
        profile.set_preference("network.proxy.http_port.override", int("8080"))
        profile.set_preference("general.useragent.override", user_agent)
        browser = webdriver.Firefox(profile, options=options, executable_path='/home/vagrant/geckodriver')
        browser.header_overrides = {'Referer': url, 'User-Agent': user_agent,}
        browser.get(url)
        """
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
        """
        sid = browser.find_element_by_name(name='id')
        sid.send_keys("733")
        """
        tcapt = browser.find_element_by_name(name='captcha')
        tcapt.send_keys(text2)
        """
        submit = browser.find_element_by_name(name="holdthedoor")
        submit.click()
        """
        browser.save_screenshot("fullpage.png")
        """
        browser.manage().deleteAllCookies();
        browser.close()
        tmp -= 1
    except:
        continue
print("Finish! {} votes".format(votes+1))
