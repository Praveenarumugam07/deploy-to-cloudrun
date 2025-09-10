from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Cloud Run deployed by Cloud Deploy!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(__import__('os').environ.get('PORT', '8080')))
