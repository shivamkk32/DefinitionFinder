from flask import Flask,render_template,request
from urllib.request import   urlopen as uReq
from bs4 import BeautifulSoup as bs


app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=['POST'])
def route():
    productName=request.form['content'].replace(' ','_')
    try:
        reviews=[]
        wikiURL="https://en.wikipedia.org/wiki/" +productName
        uClient=uReq(wikiURL)  #Open the URL
        fillPage=uClient.read() #Get complete webpage
        uClient.close()
        wikiHtml=bs(fillPage,'html.parser')
        description = wikiHtml.find_all('div', {'id': "mw-content-text"})
        reviews.append(description[0].select_one("p:nth-of-type(3)").text)
        """
        for i in description:

             try:
                definition=i.select_one("p:nth-of-type(3)").text
             except:
                 definition='No information on this topic'
             mydict = {"Product": definition}  # saving that detail to a dictionary
        """
        #x = table.insert_one(mydict)  # insertig the dictionary containing the rview comments to the collection
        #reviews.append(mydict)
        return render_template('results.html', reviews=reviews)
    except:
        return 'something is wrong'


if __name__== '__main__':
    app.run()