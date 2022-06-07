from flask import Flask, render_template
import json

app = Flask(__name__)

with open('./static/result/progress_event.json', 'r') as file:
    progress_text = json.load(file, strict=False)

with open('./static/result/new_event.json', 'r') as file:
    new_text = json.load(file, strict=False)

with open('./static/result/end_event.json', 'r') as file:
    end_text = json.load(file, strict=False)
    
with open('./static/result/result_event.json', 'r') as file:
    result_text = json.load(file, strict=False)



with open('./static/result/progress_event_busan.json', 'r') as file:
    progress_busan_text = json.load(file, strict=False)

with open('./static/result/new_event_busan.json', 'r') as file:
    new_busan_text = json.load(file, strict=False)

with open('./static/result/end_event_busan.json', 'r') as file:
    end_busan_text = json.load(file, strict=False)



@app.route('/')
def index():
    return render_template("index.html", text=progress_text)

@app.route('/new_event')
def new_event():
    return render_template("index.html", text=new_text)

@app.route('/end_event')
def end_event():
    return render_template("index.html", text=end_text)
    
@app.route('/progress_busan')
def progress_event_busan():
    return render_template("index.html", text=progress_busan_text)
    
@app.route('/new_event_busan')
def new_event_busan():
    return render_template("index.html", text=new_busan_text)
    
@app.route('/end_event_busan')
def end_event_busan():
    return render_template("index.html", text=end_busan_text)
    
@app.route('/result_event')
def result_event():
    return render_template("index.html", text=result_text)
 
if __name__ == '__main__':
    app.static_folder = 'static'
    app.run(host = '0.0.0.0', port =5050, debug = False)

#http://3.15.67.95:5050/