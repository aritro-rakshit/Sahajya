from flask import Flask, render_template,request
import urllib.request, json      
import requests
import os
from twilio.rest import Client

app = Flask(__name__)
headings=[]
B=[]


@app.route("/")
def home():
    url = "https://spreadsheets.google.com/feeds/cells/1EmYQusCzsCInmGy2kSwPhT5MM02qy7GguISo_6p_8Ug/od6/public/basic?alt=json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    feed=data['feed']
    entry=feed['entry']
    itms=[]
    for each_entry in entry:
        content=(each_entry['content'])
        itms.append(content['$t'])
    headings=itms[:3]
    infos=itms[3:]
    i=0
    B = []
    C = []
    for x in infos:
        if(i%3==0):
            C = []
            B.append(C)
        C.append(x)
        i=i+1
    #oxygen
    url_1 = "https://spreadsheets.google.com/feeds/cells/1Otr_if3P38dMHetfr5XWr6uVm5PO4olnHi5bGVt3mUY/od6/public/basic?alt=json"
    response_1 = urllib.request.urlopen(url_1)
    data_1 = json.loads(response_1.read())
    feed_1=data_1['feed']
    entry_1=feed_1['entry']
    itms_1=[]
    for each_entry_1 in entry_1:
        content_1=(each_entry_1['content'])
        itms_1.append(content_1['$t'])
    headings_1=itms_1[:3]
    infos_1=itms_1[3:]
    i=0
    B_1 = []
    C_1 = []
    for x in infos_1:
        if(i%3==0):
            C_1= []
            B_1.append(C_1)
        C_1.append(x)
        i=i+1
    return render_template('index.html', heading=headings, data=B, heading_1=headings_1, data_1=B_1)
@app.route("/contact", methods =["GET", "POST"])
def contact():
    if request.method == "POST":
       name_1 = request.form.get("name_1")
       contact_1 = request.form.get("contact_1")
       query_1 = request.form.get("query_1")
       msg=[name_1,contact_1,query_1]
       base_url = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Name:{}'.format(msg[0])
       requests.get(base_url)
       base_url1 = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Contact:{}'.format(msg[1])
       requests.get(base_url1)
       base_url2 = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Query:{}'.format(msg[2])
       requests.get(base_url2)
       account_sid = 'ACca9a08403d7ed1350ba2610187bd2911'
       auth_token = '03c6e18f112fed2728a758a359571d40'
       client = Client(account_sid, auth_token)

       message = client.messages.create(
                              body='Name:'+name_1+"\n"+"Contact:"+contact_1+"\n"+"Query:"+query_1,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917908594645'
                          )
       message = client.messages.create(
                              body='Name:'+name_1+"\n"+"Contact:"+contact_1+"\n"+"Query:"+query_1,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917076158941'
                          )
       message = client.messages.create(
                              body='Name:'+name_1+"\n"+"Contact:"+contact_1+"\n"+"Query:"+query_1,
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917365025556'
                          )

    
    return render_template('contact.html')
       
if __name__ == "__main__":
    app.run(use_reloader = True,debug=True)
