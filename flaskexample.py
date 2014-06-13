from flask import Flask
from random import random
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    start = """
  <html>
  <head>
  <title>
  <body>
  
  """
  
  
    start2 = """
  </title>
  </head>
  """
    preamble = """
  <a href= "http://cdn.superbwallpapers.com/wallpapers/funny/cat-riding-a-fire-breathing-unicorn-16414-1366x768.jpg" >
  <img src="http://www.factslides.com/imgs/s-Cats.png" />
  </a>
  """
    mainbody = """
    <form action="">
    Name: <input type="text" name="name">
    Password: <input type = "password" name = "pwd"
    """
    prepostamble =""" </form> """
    postamble = """
  </body>
  </html>
  """
    return start + start2 + mainbody + prepostamble + (preamble * 20) + postamble

if __name__ == '__main__':
    app.run()
