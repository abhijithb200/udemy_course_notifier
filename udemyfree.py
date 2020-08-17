import requests
from bs4 import BeautifulSoup 
import pyshorteners
import redis
import telebot
import time

red = redis.from_url('  YOUR  REDIS  URL')
bot_token = 'TELEGRAM BOT TOKEN'
bot = telebot.TeleBot(token=bot_token)

class UdemyFree:
    def __init__(self):
        self.First()
        self.Second()
        self.Last()
        self.LinkProcess()

    def First(self):
        r = requests.get('http://techcracked.com').text
        soup = BeautifulSoup(r,'html.parser')
        q = soup.find('h2', class_='post-title')
        link = q.find('a')['href']
        head = q.get_text()
        head = head.split()[:-2]
        head=" ".join(head)
        self.head=head
        self.firstlink = link

    def Second(self):
        r = requests.get(self.firstlink).text
        soup = BeautifulSoup(r,'html.parser')
        link=soup.find('a',class_='myButton')['href']
        self.secondlink=link
    
    def Last(self):
        r = requests.get(self.secondlink).text
        soup = BeautifulSoup(r,'html.parser')
        p = soup.find('h6')
        link=p.find('a')['href']
        self.lastlink= link
    
    def LinkProcess(self):
        session = requests.Session()
        resp = session.head(self.lastlink, allow_redirects=True)
        link = pyshorteners.Shortener().tinyurl.short(resp.url)
        self.link = link
        
        
if __name__ == '__main__':
    obj = UdemyFree()
    print(obj.__dict__)
    equ = red.get('dis')
    time.sleep(15)
    equ = str(equ)
    equ2 = obj.head
    equ2 = "b'"+equ2+"'"
    if equ == equ2:
        print("got it")
    if equ != equ2:
        red.set("dis", obj.head)
        message = obj.head+"\n\n Course link:-\n\n"+obj.link
        bot.send_message('  CHAT ID   ',message)


    
   
    
