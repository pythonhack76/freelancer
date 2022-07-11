#hacker news email 
#requests, bs4, smtplib, email.mime, datetime
from urllib import response
import requests
from bs4 import BeautifulSoup #web scraping
#invio email
import smtplib
#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
#gestione tempo 
import datetime  
now = datetime.datetime.now() 

# email content placeholder 
content = ''

#project script 

def extract_news(url):
    print('Estrazione titoli ...')
    cnt = ''
    cnt += ('<b>HN Top Stories : </b>\n'+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class':'title','valign':''})):
        cnt += ((str(i+1)+' :: '+tag.text + "\n" + '<br>') if tag.text!='More' else '')
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>-------------<br>')
content +=('<br><br>Fine messagggio')

#creazione email 

print('Email in composizione ...')

#aggiungi dettagli email 

SERVER = 'smtp.gmail.com' 
PORT = 587
FROM = 'pythonthehack@gmail.com'
TO = 'pythonthehack@gmail.com'
PASS = 'Facile2020!@'

# fp = open(file_name, 'rb')
# msg = MIMEText('')
msg = MIMEMultipart()

msg['Subject'] = 'News stories ' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = FROM
msg['To'] = TO 

msg.attach(MIMEText(content, 'html'))
#fp.close()

msg.attach(MIMEText(content, 'html'))
print('Initialing Server ...')

server = smtplib.SMTP(SERVER, PORT)









