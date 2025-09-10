# main.py - minimal Flask application with a simple form
from flask import Flask, request, redirect


app = Flask(__name__)


FORM_HTML = """
<!doctype html>
<title>Contact</title>
<h1>Contact Form</h1>
<form method="post">
<label>Name: <input type="text" name="name"></label><br/>
<label>Email: <input type="email" name="email"></label><br/>
<label>Number: <input type="text" name="number"></label><br/>
<button type="submit">Send</button>
</form>
"""


@app.route('/', methods=['GET','POST'])
def index():
if request.method == 'POST':
name = request.form.get('name','')
email = request.form.get('email','')
number = request.form.get('number','')
return f"Received — name={name}, email={email}, number={number}\n"
return FORM_HTML


if __name__ == '__main__':
app.run(host='0.0.0.0', port=int(__import__('os').environ.get('PORT', 8
