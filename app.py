from flask import Flask, render_template
import urllib.request, json      

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
   
if __name__ == "__main__":
    app.run(use_reloader = True,debug=True)
