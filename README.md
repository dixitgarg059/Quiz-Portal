# Run Application
```
1. To run this application, you need to install flask, sqlalchemy.Go to Commandline Terminal:
	$ pip3 install flask
	$ pip3 install flask_sqlalchemy
2. Now run routes.py (in exp2 folder) file on your  Terminal 
	$ python3 routes.py
3. Right Click on link shown on terminal and open it in browser.
```
# Folder Structure
```	
1. exp2
	1. __init__.py 	 	            #import flask,routes , contain app, db
	2. routes.py                    #contain all routes
	3. templates			        #contain all html files
		layout.html 			        #contain layout part of website
		other files contain the main block containing part as indicated by their name.
	5. static
		1.images                      
		2.css
			style.css               #contain css part of all html files
			some downloaded css files
		3.js
			custom.js               #contain js part of all html files
			other js files also
			some downloaded js files
	6. quiz.db                       #database file contains all questions of quiz and experiment and   
									 options and correct answers of quiz and experiment
3. Documentation.txt 				#contains description of all functions
4. README.md 						#about how to run app and file structure
```