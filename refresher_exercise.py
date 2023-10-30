# If statement
'''
Your user wants to find out how much he/she will save when buying a macbook
1. Ask them if they are a university student. If they say yes
2. Ask them for the price of the Macbook
3. Remove 20% from the price of the Macbook and print out the discount price
'''

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

apple_macbook_url = 'https://www.onbuy.com/gb/p/apple-macbook-air-13-m1-2020-256gb-gold~p31823117/'
headers = {"user-agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/119.0"}


options = Options()
options.set_headless(headless=True)
dr = webdriver.Chrome(options=options)
dr.get(apple_macbook_url)
print ("Headless Chrome Initialized")
dr.quit()
soup = BeautifulSoup(dr.page_source, 'lxml')
title = soup.find('div', class_ = 'price')
#print(title)
text = title.get_text()
#print(text)

macbook_price = text.replace('£', '')
is_student = input('Are you a student: (y/n)')
if is_student.lower() == 'n':
    print('You are not availble for student discount')
else:
    print('The Macbook price for you is ', float(macbook_price) * 0.8)