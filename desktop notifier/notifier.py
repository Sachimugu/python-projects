# import required libraries
from bs4 import BeautifulSoup
from plyer import notification
import requests
import time

#*****************************************
def browse(url): #browse function
    page= requests.get(url) #to load a url
    soup= BeautifulSoup(page.content, 'lxml') # parse it content
    return soup
#*****************************************
url='https://www.nairaland.com/'
Title = 'first title'

while True:
    soup= browse(url)
    link1=soup.findAll("a", href=True)[54]['href']
    soup = browse(link1)
    link1 = soup.findAll("a", href=True)[54]['href']
    title = soup.find('h2').text.strip('\'')[0:-12]
    massage = f'{title} \n {link1}'
    if title != Title:
            notification.notify(title='Notification!',
                                message= massage,
                                timeout=20)
            
    else:
        time.sleep(100)
    Title = title
            # every 20 seconds
    time.sleep(20)