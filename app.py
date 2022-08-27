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

@app.route("/self", methods=["GET", "POST"])
def compress():

    if request.method == "GET":
        return render_template("selfAssessment.html", check=0)
    else:
        print(request.form.get("name"));
        print(request.form.get("date"));
        print(request.form.get("class"));
        print(request.form.get("dob"));
        print(request.form.get("address"));
        print(request.form.get("phone"));
        print(request.form.get("dreamProfessions"));
        print(request.form.get("interestedSubjects"));
        print(request.form.get("hobbies"));
        print(request.form.get("additionalSkills"));
        print(request.form.get("qualitiesLiked"));
        print(request.form.get("qualitiesAdmired"));


        return render_template("selfAssessment.html", check=-1)
        
# Restart application whenever changes are made
if __name__ == "__main__":
    app.run(debug = True)