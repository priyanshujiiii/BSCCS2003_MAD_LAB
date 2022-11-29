from flask import Flask , render_template
app = Flask(__name__)

@app.route('/home')
def HomePage():
    return "Welcome, folks! This is the Home Page!"

@app.route('/about')
def AboutPage():
    users=[
        {"user":"Shobhit","gender":"Male","age":23,"score":90},
        {"user":"Deepak","gender":"Male","age":17,"score":88},
        {"user":"Nikita","gender":"Female","age":20,"score":87}
    ]
    return render_template('home.html',condition=True,users=users)

if __name__ == "__main__":
    app.run(debug=True)
