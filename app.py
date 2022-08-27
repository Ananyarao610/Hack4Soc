import os
import time
import glob
from flask import Flask, redirect, render_template, request, send_file

# Configure Application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        scores = [0, 0, 0, 0, 0, 0, 0, 0]
        for i in range (1,81):
            s = 'q' + str(i)
            if request.form.get(s) != None:
                scores[int((i-1)%8)] += 1
        print(request.form.get("q1"));
        print(scores)
        return render_template("home.html");

@app.route("/compress", methods=["GET", "POST"])
def compress():

    if request.method == "GET":
        return render_template("compress.html", check=0)

    else:
        return render_template("compress.html", check=-1)
        
# Restart application whenever changes are made
if __name__ == "__main__":
    app.run(debug = True)