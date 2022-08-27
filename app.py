import os
import time
import glob
from flask import Flask, redirect, render_template, request, send_file
from werkzeug.utils import secure_filename

scores = [0, 0, 0, 0, 0, 0, 0, 0]
# Configure Application
app = Flask(__name__)
app.config["FILE_UPLOADS"] = "/Users/harshahl/Desktop/Hack4Soc/Hack4Soc/uploads"



@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        
        for i in range (1,81):
            s = 'q' + str(i)
            if request.form.get(s) != None:
                scores[int((i-1)%8)] += 1
        print(request.form.get("q1"));
        print(scores)
        return render_template("selfAssessment.html");

      
@app.route("/final", methods=["GET", "POST"])
def final():
    if request.method == "GET":
        return render_template("decompress.html")
    else:
        
        f = request.files['file']
        f.save(secure_filename(f.filename))
        return render_template("decompress.html");

@app.route("/self", methods=["GET", "POST"])
def compress():

    if request.method == "GET":
        return render_template("selfAssessment.html", check=0)
    else:
        d = {
        'Astronomer': ['BE ASE','S','Science, Math',[]],
        'Botanist': ['BE BT','S', 'Biology, Environmental Science',[]],
        'Conservationist': ['BE BT','S','Environmental Science',[]],
        'Ecologist': ['BE BT','S','Geography',[]],
        'Meteorologist': ['BE BT','S','Geography',[]],
        'Audiologist': ['Sound engineering','A','Music',[]],
        'Sound editor': ['Sound engineering','C','Instrumentation',[]],
        'Music conductor': ['Sound engineering','A','BE ECE','Electronics',[]],
        'Recording engineer': ['Sound engineering','S', 'BE ECE','Physics',[]],
        'Songwriter': ['Sound engineering, BE ECE','A','Poetry, Literature',[]],
        'Accountant': ['B COM, CA','C','Statistics, Probability',[]],
        'Computer analyst': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[]],
        'Computer technician': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[]],
        'Computer programmer': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[]],
        'Database designer': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, DBMS, Maths',[]],
        'Counselor': ['Bachelor of Psychology','C','Science, Psychology',[]],
        'Social Worker': ['Commerce','C','Social Science',[]],
        'Teacher': ['Bachelor of Education (B. Ed.) ','S','Maths, Science',[]],
        'Doctor': ['MBBS','S','Science, Biologys',[]],
        'Businessman': ['BBA, MBA','C','Social Science',[]],
        'Athlete': ['BBA in Sports Management','C','Sports',[]],
        'Dancer': ['Bachelor of Performing Arts','A','Dance, Physical Education',[]],
        'Physical Education Instructor': ['BBA in Sports Management','A','Sports',[]],
        'Actor / Actress': ['Acting School','A','Drama',[]],
        'Paramedic': ['MBBS','S','Biology, Science',[]],
        'Journalist': ['Bachelor\'s degree in journalism, mass communications','C','Social Science, Literature, English, Language, Political Science',[]],
        'Public Speaker': ['Bachelor\'s degree in mass communication','C','Language',[]],
        'Politician': ['Political Science','C','Social Science, Civics',[]],
        'Psychologist': ['Bachelor\'s in Psychology','S','Science',[]],
        'Career counselor': ['Master\'s diploma in career guidance or Master\'s diploma in career guidance  development','S','General Knowledge',[]],
        'Writer': ['Degree in  creative writing, communication and media','A','Literature, Language',[]],
        'Consultant': ['Postgraduate diploma in career guidance or management','C','General Knowledge',[]],
        'Event Management': ['Bachelor\'s degree in event management','C','Drama',[]],
        'Graphic Designer': ['B Design','A','Art, Geometry',[]],
        'Architect': ['B Arch','S','Maths, Art',[]],
        'Fashion Designer': ['Bachelor of design in fashion, BSc in fashion design, BA in fashion design','A','Fashion, Art',[]],
        'Interior Decorator': ['Interior Desiging','A','Art, Symmetry',[]],
        'Photographer': ['PG Diploma in Photography','A','Geometry',[]],
        }

        marks=request.form.get("marks")
        dream_careers=request.form.get("dreamProfessions")
        dream_careers=dream_careers.split(', ')
        print("Dream professions", dream_careers)
        dream_subjects =request.form.get("interestedSubjects")
        dream_subjects=dream_subjects.split(', ')
        mi_subjects = ['LIN', 'I-M', 'SP', 'B-K', 'MU', 'NTER', 'NTRA', 'NAT']
        non_academic = ['carpenter', 'farmer', 'painter', 'pottery']
        top5=[]
        riasec = [0.1,0.1,0.1,0.1,0.1]
        subjects_final={}
        mi_careers = {'LIN': ['Astronomer','Botanist','Conservationist', 'Ecologist','Meteorologist'],
            'I-M': ['Audiologist','Audiologist', 'Sound editor', 'Music conductor','Recording engineer','Songwriter'],
            'SP': ['Accountant','Computer analyst', 'Computer technician','Computer programmer','Database designer' ],
            'B-K': ['Counselor', 'Social Worker', 'Teacher', 'Doctor', 'Businessman'],
            'MU': ['Athlete', 'Dancer', 'Physical Education Instructor', 'Actor / Actress', 'Paramedic'],
            'NTER': ['Journalist', 'Public Speaker', 'Politician', 'Teacher', 'Actor / Actress'],
            'NTRA': ['Psychologist', 'Career counselor', 'Writer', 'Consultant', 'Event Management'],
            'NAT': ['Graphic Designer', 'Architect', 'Fashion Designer', 'Interior Decorator', 'Photographer']
            }

        final_percentage={}
    
        domain = mi_subjects[scores.index(max(scores))]
        choice =  mi_careers[domain]   #will be a list
        print("This is choice", choice)

        value = 1/(len(dream_careers)+5)
        

        for i in choice:   #assign equal values
            print(i)
            temp=d[i][2]
            choice_subjects=temp.split(', ')
            final_percentage[i]= value
            print("choice subjects", choice_subjects)
            subjects_final[i]= choice_subjects

        for i in dream_careers:
            final_percentage[i]=value
        print(final_percentage)
        

        #to check for common careers
        for i in dream_careers:
            print("Inside loop")
            print(choice)
            if i in choice:
                final_percentage[i] = final_percentage[i]*2
        print(final_percentage)
        print("Here")
        print(choice,"This is choice")
        print(final_percentage)
        count=0
        for i in dream_subjects:
            if i in subjects_final[choice[count]]:
                print("This is final career",choice[count])
                print("I AM HERE")
                final_percentage[choice[count]] = final_percentage[choice[count]]+0.05
            count+=1

        


        print(request.form.get("name"));
        print(request.form.get("date"));
        print(request.form.get("class"));
        print(request.form.get("dob"));
        print(request.form.get("address"));
        print(request.form.get("phone"));
        print(request.form.get("hobbies"));
        print(request.form.get("additionalSkills"));
        print(request.form.get("qualitiesLiked"));
        print(request.form.get("qualitiesAdmired"));
        


        return render_template("selfAssessment.html", check=-1)
        
# Restart application whenever changes are made
if __name__ == "__main__":
    app.run(debug = True)