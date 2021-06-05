from flask import Flask, render_template,request
import urllib.request, json      
import requests
import os
import json

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
    verify="a"
    if request.method == "POST":
       name_1 = request.form.get("name_1")
       contact_1 = request.form.get("contact_1")
       query_1 = request.form.get("query_1")
       clientKey= request.form.get("g-recaptcha-response")
       secretKey='6LdWCtAaAAAAANf2fQ2bAFf59A8m7E9FBphOk1hP'
       msg=[name_1,contact_1,query_1]
       captchaData={
           "secret":secretKey,
           "response":clientKey
       }
       r=requests.post('https://www.google.com/recaptcha/api/siteverify', data=captchaData)
       response=json.loads(r.text)
       verify=response['success']
       if verify:
            base_url = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Name:{}'.format(msg[0])
            requests.get(base_url)
            base_url1 = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Contact:{}'.format(msg[1])
            requests.get(base_url1)
            base_url2 = 'https://api.telegram.org/bot1666558244:AAEX4roH11bGFKUhV_e9MFHCl7iA1UP3S6Q/sendMessage?chat_id=-583194863&text=Query:{}'.format(msg[2])
            requests.get(base_url2)

    
    return render_template('contact.html',ver=verify)
@app.route("/imp")
def imp():
    #Medicine
    url = "https://spreadsheets.google.com/feeds/cells/1CZ-rZeN8nh6gNBAvsy0079-l4ltfMKvPKgb0BNGyP_8/od6/public/basic?alt=json"
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    feed=data['feed']
    entry=feed['entry']
    itms=[]
    for each_entry in entry:
        content=(each_entry['content'])
        itms.append(content['$t'])
    headings=itms[:2]
    infos=itms[2:]
    i=0
    B = []
    C = []
    for x in infos:
        if(i%2==0):
            C = []
            B.append(C)
        C.append(x)
        i=i+1
    
    #Testing
    url_1 = "https://spreadsheets.google.com/feeds/cells/1XAeSd7_8YSl5P8Xvjk2XmQ7bfdDeJBrU4MIv7LJCgZk/od6/public/basic?alt=json"
    response_1 = urllib.request.urlopen(url_1)
    data_1 = json.loads(response_1.read())
    feed_1=data_1['feed']
    entry_1=feed_1['entry']
    itms_1=[]
    for each_entry_1 in entry_1:
        content_1=(each_entry_1['content'])
        itms_1.append(content_1['$t'])
    headings_1=itms_1[:2]
    infos_1=itms_1[2:]
    i=0
    B_1 = []
    C_1 = []
    for x in infos_1:
        if(i%2==0):
            C_1 = []
            B_1.append(C_1)
        C_1.append(x)
        i=i+1

    # Food Delivery
    url_2 = "https://spreadsheets.google.com/feeds/cells/1MB84Gkn22G_RJ1_V76ho2cJQQbYqZA2TWK3BEy3j6S4/od6/public/basic?alt=json"
    response_2 = urllib.request.urlopen(url_2)
    data_2 = json.loads(response_2.read())
    feed_2=data_2['feed']
    entry_2=feed_2['entry']
    itms_2=[]
    for each_entry_2 in entry_2:
        content_2=(each_entry_2['content'])
        itms_2.append(content_2['$t'])
    headings_2=itms_2[:2]
    infos_2=itms_2[2:]
    i=0
    B_2 = []
    C_2 = []
    for x in infos_2:
        if(i%2==0):
            C_2 = []
            B_2.append(C_2)
        C_2.append(x)
        i=i+1
    # Sanitization
    url_3 = "https://spreadsheets.google.com/feeds/cells/1W9qPXnzN6KQc_A3Gm8PwKZO_whAdehhaFqqzMOrtwPg/od6/public/basic?alt=json"
    response_3 = urllib.request.urlopen(url_3)
    data_3 = json.loads(response_3.read())
    feed_3=data_3['feed']
    entry_3=feed_3['entry']
    itms_3=[]
    for each_entry_3 in entry_3:
        content_3=(each_entry_3['content'])
        itms_3.append(content_3['$t'])
    headings_3=itms_3[:2]
    infos_3=itms_3[2:]
    i=0
    B_3 = []
    C_3 = []
    for x in infos_3:
        if(i%2==0):
            C_3 = []
            B_3.append(C_3)
        C_3.append(x)
        i=i+1
    print(B_3)
    return render_template('imp.html',heading=headings, data=B,headings_1=headings_1, data_1=B_1,headings_2=headings_2, data_2=B_2,headings_3=headings_3, data_3=B_3)
       
if __name__ == "__main__":
    app.run(use_reloader = True,debug=True)
