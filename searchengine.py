from flask import Flask

from flask import request
from flask import render_template
"""
import os
from jinja2 import Environment, FileSystemLoader"""
import sqlite3










#create a app for flask  
app = Flask(__name__)

"""# Define the template directory
tpldir = os.path.dirname(os.path.abspath(__file__))+'/templates/'

# Setup the template enviroment
env = Environment(loader=FileSystemLoader(tpldir), trim_blocks=True)"""



#set the app route in home directory
@app.route('/')
def my_form():
	return render_template("main.html")


@app.route('/', methods=['POST'])
def my_form_post():


	#for take inpt from main page where value is on sent varible
	text = request.form['sent']
	print (text)
	#for call value from data base
	a,b,c = data(text)
	print (a,b,c,"3")
	"""output = env.get_template('search1.html').render(
					value1=a,value2=b,value3=c,text1 = text
				)
				return output"""

	#call search page with argument 			
	return render_template("search1.html",value1=a,value2=b,value3=c,text1 = text)
	









def data(sent):
	#made connection from datavbase and create a cursor
	conn = sqlite3.connect("C:/Search Engine/search.db")
	cur = conn.cursor()
	text =sent.lower()
	#split the input in list of string
	line = text.split()
	print (line)
	

	# remove the wh words and helping verb from list of string	
	whlist = ["why","who","which","what","where","when","how","how far","how long","how many","how much","how old","how come"]
	axlist = ["be","am","are","is","was","were","being","can","could","do","did","does","doing","have","had","has","having","may","might","must","shall","should","will","would"]
	line = [n for n in line if n not in whlist]
	line = [n for n in line if n not in axlist]
	
	sent =""
	
	#change the list of sring in again sent
	for i,j in enumerate(line):
		if i==len(line)-1:
			sent = sent + j 
		else:    
			sent = sent + j +" "
	
	#faetch keyword from database 
	cur.execute("select distinct keyword from book1")   
	keyword = cur.fetchall()
	
	key1 = []
	result = []
	
	#check for sent is availble in database 
	for i in keyword:
		if sent == i[0]:
			key1.append(i[0])
	
	#if keyword is availabe in data base then
	#fetch the value of title, decription & url		
	if len(key1) > 0:
		print (key1[0])
		cur.execute("Select title,decription,url From book1 Where keyword = '"+key1[0]+"'")
		result = cur.fetchall()
	else:
		#if keyword is availabe in data base then
		#create a google link for input sentence
		title = text
		print (title, "2")
		decription = "please search on google by click on link"
		url = "https://www.google.co.in/?gfe_rd=cr&ei=gtrlWIexGanT8gem2Y-YBQ#q="
		tex=text.split()
		print (tex, "1")
		for j,i in enumerate(tex):
			if j==len(tex)-1:
				url=url+i
			else:
				url=url+i+"+"
		a=[]
		#append the title, decription, url in result
		a.append(title)
		a.append(decription)
		a.append(url)
		a=tuple(a)
		result.append(a)
	

	for i in result:
			print (i)
	
	print (result)

	a=[]
	b=[]
	c=[]
	#divide the result in difernt list according
	#title, decription & url
	for i in range(0,len(result)):
		a.append(result[i][0])
		b.append(result[i][1])
		c.append(result[i][2])
	print (a)
	print (b)
	print (c)		
	return a, b, c

			 	
#for running this program on server
if __name__ == '__main__':
    app.run()


    