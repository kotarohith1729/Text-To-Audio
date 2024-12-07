import pyttsx3
from flask import Flask, render_template,request
app=Flask(__name__)
@app.route('/')
def welcome():
    return render_template('index.html')
@app.route('/op',methods=['POST','GET'])
def ope():
    if(request.method=='POST'):
        text=request.form['inp']
        engine=pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        return render_template('index.html')
@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__=="__main__":
    app.run(debug=True)
