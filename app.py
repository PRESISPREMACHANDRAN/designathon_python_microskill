from flask import Flask,render_template,request
app=Flask(__name__)


datab={'presi@gmail.com':'1234','anju@gmail.com':'5678'}

@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/kerala.html')
def kerala():
    return render_template('kerala.html')

@app.route('/alappuzha.html')
def alappuzha():
    return render_template('alappuzha.html')


@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/sample',methods=['GET','POST'])
def logins():
    username=request.form['textbox1']
    pwd=request.form['textbox2']
    if username not in datab:
        return render_template('login.html',msg='invalid username')
    elif datab[username]!=pwd:
        return render_template('login.html',msg='invalid password')
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True,port=5100)