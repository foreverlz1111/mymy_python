import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common import keys

if __name__ == "__main__":
    print("begining...")
    try:
        page = requests.request("GET","https://www.github.com",timeout=1)
    except requests.exceptions.Timeout as e:
        print("error: ",e)
    else:
       print("succeed")

    
