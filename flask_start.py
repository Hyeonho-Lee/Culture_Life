from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port =5050, debug = False)