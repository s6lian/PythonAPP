from flask import Flask, render_template
# from the flask library import the Flask class

app = Flask(__name__)
# instantiating the object ,'__name__' gets as value of the name of python script

@app.route('/')
# a decorator, the output of the function below will be mapped to this url
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug = True)
