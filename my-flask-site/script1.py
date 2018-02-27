# This script does all of the routing and hookup of the usual html/css etc files

from flask import Flask, render_template #import the framework. render template helps import outside files

app=Flask(__name__) #instantiate the class -- python will assign the name 'main' to the file

@app.route('/') #where to view the site
def home(): #site content
	# return "Website content goes here! Home"
	return render_template("home.html") #html files must live in templates folder

@app.route('/about/') #where to view the site
def about(): #site content
	# return "Woo About page!"
	return render_template("about.html")


if __name__=="__main__":
	app.run(debug=True) #run script