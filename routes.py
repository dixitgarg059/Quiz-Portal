from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'     # providing address of database-file to app
db = SQLAlchemy(app)
class English(db.Model):                                        # class definition of database  
    id = db.Column(db.Integer, primary_key = True)
    question = db.Column(db.String(120), nullable=False)
    answers = db.Column(db.String(120), nullable=False)
    choice1=db.Column(db.String(120),nullable=False)
    choice2=db.Column(db.String(120),nullable=False)
    choice3=db.Column(db.String(120),nullable=False)
    choice4=db.Column(db.String(120),nullable=False)
    first = db.Column(db.String(120), nullable=False)
    second = db.Column(db.String(120), nullable=False)
    ans=db.Column(db.String(120),nullable=False)
    first1 = db.Column(db.String(120), nullable=False)
    second1 = db.Column(db.String(120), nullable=False)




    def __init__(self,Question, Option1,Option2, Option3,Option4,Answer,First, Second,Answer1,First1,Second1):
        self.question = Question             # for initialization
        self.choice1 = Option1
        self.choice2 = Option2
        self.choice3 = Option3
        self.choice4 = Option4
        self.answers = Answer
        self.first = First
        self.second = Second
        self.ans = Answer1
        self.first1=First1
        self.second1=Second1
    
    def __repr__(self):                         # giving representation to class
        return '<User %r>' % self.question
@app.route('/')
@app.route('/intro')                            # for introduction page
def intro():
    return render_template('Introduction.html')
@app.route('/theory')
def theory():
    return render_template('Theory.html')       # for theory page
@app.route('/objective')
def objective():
    return render_template('Objective.html')   # for objective page
@app.route('/experiment',methods=['POST','GET'])  
def experiment(): 
    db.create_all()                           # querying data 
    data1=English.query.all()                 # for experiment page
    arr1=random.sample(range(0,9),5)        
    return render_template('Experiment.html',q11=data1[arr1[0]],op1=data1[arr1[0]].first1,op2=data1[arr1[1]].first1,op3=data1[arr1[2]].first1,op4=data1[arr1[3]].first1,op5=data1[arr1[4]].first1,que=data1[arr1[0]].second1)
@app.route('/quiz',methods=['POST','GET'])
def quiz():                                    # for quiz page
    db.create_all()                            # querying data
    data = English.query.all()
    global arr
    arr=random.sample(range(0,9),5)
    return render_template('Quizzes.html',q1=data[arr[0]],q2=data[arr[1]],q3=data[arr[2]],q4=data[arr[3]],q5=data[arr[4]])
@app.route('/procedure')
def procedure():                              # for procedure page
    return render_template('Procedure.html')
@app.route('/feedback')                       # for feedback page
def feedback():
    return render_template('Feedback.html')


@app.route('/check',methods= ['POST'])
def check():                                 # this is for checking quiz answers 
    
    R1=request.form['Q1']
    R2=request.form['Q2']
    R3=request.form['Q3']
    R4=request.form['Q4']
    R5=request.form['Q5']
    db.create_all()
    allUsers=English.query.all()
    Correct="Correct Answers : "
    Wrong="Wrong Answers : "
    Unattempted="Unattempted  : "
    if R1==allUsers[arr[0]].answers:
        Correct+="1 "
    elif R1=='5':
        Unattempted+="1 "
    else:
        Wrong+="1 "
    if R2==allUsers[arr[1]].answers:
        Correct+="2 "
    elif R2=='5':
        Unattempted+="2 "
    else:
        Wrong+="2 "
    if R3==allUsers[arr[2]].answers:
        Correct+="3 "
    elif R3=='5':
        Unattempted+="3 "
    else:
        Wrong+="3 "
    if R4==allUsers[arr[3]].answers:
        Correct+="4 "
    elif R4=='5':
        Unattempted+="4 "
    else:
        Wrong+="4 "
    if R5==allUsers[arr[4]].answers:
        Correct+="5 "
    elif R5=='5':
        Unattempted+="5 "
    else:
        Wrong+="5 "
    Correct+="\n"
    Wrong+="\n"
    Unattempted+="\n"
    return jsonify({'output':Correct+Wrong+Unattempted,'status':'1'})
@app.route('/check1',methods= ['POST'])    
def check1():          
    db.create_all()        
    alldata=English.query.all()    # this is for checking experiment answers        
    R1=request.form['Q1']       
    R2=request.form['Q2']       
    R3=request.form['Q3']       
    R1=R1.strip()
    R2=R2.strip()
    R3=R3.strip()
    print(R1,R2,R3)
    flag="Wrong Answer!!"        
    for i in alldata:
        i.ans=(i.ans).strip()
        i.first=(i.first).strip()
        i.second=(i.second).strip()
        print(i.ans,i.first,i.second)       
        if i.ans == R1 and i.first == R2 and i.second == R3:        
            flag="Right Answer!!";

                
    return jsonify({'output':flag,'status':'1'})     
@app.route('/check2',methods= ['POST'])     
def check2():       
    db.create_all()           # this is for checking experiment answers
    alldata=English.query.all()        
    R1=request.form['P1']       
    R2=request.form['P2']       
    flag="Wrong Answer!!"        
    for i in alldata:       
        if i.first1 == R1 and i.second1 == R2:      
            flag="Right Answer!!";             
    return jsonify({'output':flag,'status':'1'})     
app.run()
if __name__=='__main__':
    app.run()
