from flask import Flask,request,render_template,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import itertools

app = Flask(__name__)
                                
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)
class English(db.Model):
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
        self.question = Question
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
    


    # @app.route('/')
    # def Quizzes():
    #     return render_template('Quizzes.html')
    # @app.route('/')
    # def experiment():
    #     return render_template('experimenttmp.html')

def addInquiz(Question,Option1,Option2,Option3,Option4,Answer,First, Second,Answer1,First1,Second1):
    db.create_all()
    allUsers=English.query.all()
    new_item=English(Question,Option1,Option2,Option3,Option4,Answer,First, Second,Answer1,First1,Second1)
    db.session.add(new_item)
    db.session.commit()
    def __repr__(self):
        return '<User %r>' % self.question

# @app.route("/view")
# def userFetch():
#     db.create_all()
#     allUsers=English.query.all()
#     diction = {"Questions":[]}
#     for x in allUsers:
#         diction["Questions"].append({"Question":x.question,"Option1":x.choice1,"Option2":x.choice2,"Option3":x.choice3, "Option4":x.choice4 ,"Answer":x.answers})
#     return jsonify(diction)

addInquiz("The vacation to Myrtle Beach should be extremely restful.","Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",1,"She did not cheat on the test,","her it was the wrong thing to do.","for","Because my coffee was too cold"," I heated it in the microwave")
addInquiz("Dr. Matthews did what could be done, but it simply was not enough to save his life.", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",2,"I really need to go to work,", "I am too sick to drive.","but","Although he was wealthy,"," he was still unhappy.")
addInquiz("Eric ran home the rest of the way because he knew he was in trouble.", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",3,"Everyone was busy,","I went to the movie alone.","so","Whenever prices goes up,"," customers buy less products.")
addInquiz("A sentence with two independent clause and atleast one dependent clause is called ......", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",4,"It was getting dark,","we weren't near the cabin yet.","and","As she was bright and ambitious,"," she became a manager in no time.")
addInquiz("I know you don't like him, but that doesn't matter", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",2,"I am counting my calories,","I really want dessert.","yet","Wherever you go,"," you can always find beauty.")
addInquiz("While the music played, Rachel sneaked in through the side door.", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",3,"We have never been to Asia,","have we visited Africa.","nor","Although it was very long,"," the movie was still enjoyable.")

addInquiz("In which type of sentences FANBOYS or semicolon(;) used to join clauses?", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",2,"Should we start class now,","wait for everyone to get here?","or","As genes change over time,"," evolution progresses")
addInquiz("Although Lia gets scared very easily, she nevertheless loves to watch scary movies, and she will often stay up really late watching movie marathons.", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",4,"Should we start class now,","wait for everyone to get here?","or","As genes change over time,"," evolution progresses")

addInquiz("After she picks me up, Mum is taking me to buy shoes", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",3,"I thought the promotion was mine,","my attendance wasn't good enough.","but","After the tornado hit,"," there was very little left standing.")
addInquiz("Although he searched everywhere, Mr. Goyal could not find the keys to the computer lab.", "Simple sentence","Compound sentence","Complex sentence","Compound-Complex sentence",3,"The sky is clear","the stars are twinkling.",";","Even though he's thoroughly trained,"," he still makes a lot of mistakes.")
if __name__ == '__main__':
    app.run(port='8080')
