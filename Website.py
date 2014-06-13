'''
Created on Feb 13, 2014

@author: Luke MacCormick
'''
import postclass
from flask import Flask, session
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from os import path, makedirs, listdir
from os.path import isfile, join
app = Flask(__name__)
app.secret_key = 'ZSXDCFGVBHAJNWDKCYJSDVCBKUSDFVJKYSDVCJKBDKUAHBVDKUAYHVDKUYAE'


@app.route('/')
def start():
    return render_template('main.html' , name = "Hello User !")

@app.route('/login' , methods = ['POST'])
def login():
    session['login'] = False
    username = request.form['username']
    password = request.form['password']
    f = open('usernames/' + username.strip() + '/' + username.strip() + '.txt', 'r')
    session['logindata'] = f.readlines()
    f.close()
    if password == session['logindata'][1].strip() :
        session['login'] = True
    onlyfiles = [ f for f in listdir('usernames') if isfile(join('usernames',f)) ]
    print onlyfiles
    if session['login'] == True:
        return render_template('main.html' , name = 'Hello ' + session['logindata'][2].strip() +' !' , failure = 'Success! You have logged in!' , login = True)
    if session['login'] == False : 
        return render_template('main.html' , name = 'Hello User !' , failure = 'You have entered the wrong password, Try again please.')
@app.route('/post' , methods = ['POST'])
def post():
    session['posttitles'] = ''
    session['posttitles'] += request.form['posttitle']
    if session['login'] == True :
        return render_template('post.html' , name = session['logindata'][2].strip())
    else : 
        return render_template('post.html' , name = "Hello User!")
@app.route('/post2' , methods = ['POST'])
def post2():
    createpost = postclass.post(session['posttitles'][-1].strip() , session['logindata'][0].strip() , request.form['post'])
    return redirect(url_for('myposts'))
@app.route('/newpost')
def newpost():
    if session['login'] == True :
        return render_template('newpost.html' , name = session['logindata'][2].strip())
    else:
        return render_template('newpost.html' , name = 'HELLO')
@app.route('/myposts')
def myposts():
    return redirect(url_for('user_func', username = session['logindata'][0].strip()))
@app.route('/userlist')
def userlist():
    userlist = listdir('usernames/')
    if userlist[0] == ".DS_Store" :
        del userlist[0]
    return render_template('userlist.html' , name = session['logindata'][2].strip(), userlist = userlist)
@app.route('/user/<username>')
def user_func(username):
    posts = postclass.post.postgenerator(username)
        
    return render_template('users.html', name = session['logindata'][2], theirposts = posts)
@app.route('/signup')
def signup():
    return render_template('signup.html' , name = 'Welcome to Sign Up!')
@app.route('/welcome' , methods = ['POST'])
def welcome():
    username = request.form['username']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    password = request.form['password']
    userdata = (username, password, firstname, lastname)
    if not path.exists(username.strip()) :
        makedirs("usernames/" + username.strip())
    f = open('usernames/' + username.strip() + '/' + username.strip() + '.txt' , "w")                                 #Puts User Data into the file 'username'.txt
    for x in userdata:
        f.write(x + "\n")
    f.close()
    return redirect(url_for('start'))


if __name__ == '__main__':
    app.debug = False
    app.run(debug = True , use_reloader = False)  
    
    
    
    
    
    
    
    
    