from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/index/")
def home():
    return render_template("index.html",range1 = [1,2,3,4,5,6,7,8,9,10])

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
