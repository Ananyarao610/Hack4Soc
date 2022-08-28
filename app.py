import os
import time
import glob
from flask import Flask, redirect, render_template, request, send_file
from openpyxl import load_workbook
from docx import Document
from docxtpl import DocxTemplate
# import aspose.words as aw
scores = [0, 0, 0, 0, 0, 0, 0, 0]
# Configure Application
app = Flask(__name__)


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

      
@app.route("/first", methods=["GET", "POST"])
def first():
    return render_template("index2.html")

@app.route("/final", methods=["GET", "POST"])
def final():
    if request.method == "GET":
        return render_template("final.html")
    else:
        
        return render_template("final.html");

@app.route("/self", methods=["GET", "POST"])
def compress():

    if request.method == "GET":
        return render_template("selfAssessment.html", check=0)
    else:
        
        d = {
        'Astronomer': ['BE ASE','S','Science, Math',[0.1,0.2,0.2,0.1,0.2,0.5]],
        'Botanist': ['BE BT','S', 'Biology, Environmental Science',[0.3,0.1,0.3,0.1,0.2,0.2]],
        'Conservationist': ['BE BT','S','Environmental Science',[0.3,0.2,0.1,0.2,0.1,0.2]],
        'Ecologist': ['BE BT','S','Geography',[0.2,0.2,0.1,0.2,0.2,0.3]],
        'Meteorologist': ['BE BT','S','Geography',[0.4,0.3,0.1,0.1,0.1,0.4]],
        'Audiologist': ['Sound engineering','A','Music',[0.4,0.3,0.3,0.2,0.1,0.3]],
        'Sound editor': ['Sound engineering','C','Instrumentation',[0.4,0.2,0.3,0.1,0.2,0.2]],
        'Music conductor': ['Sound engineering','A','BE ECE','Electronics',[0.4,0.1,0.2,0.1,0.2,0.1]],
        'Recording engineer': ['Sound engineering','S', 'BE ECE','Physics',[0.4,0.2,0.2,0.1,0.2,0.2]],
        'Songwriter': ['Sound engineering, BE ECE','A','Poetry, Literature',[0.1,0.1,0.1,0.3,0.3,0.2]],
        'Accountant': ['B COM, CA','C','Statistics, Probability',[0.2,0.1,0.1,0.3,0.3,0.5]],
        'Computer analyst': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[0.4,0.3,0.2,0.2,0.2,0.5]],
        'Computer technician': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[0.4,0.3,0.3,0.2,0.2,0.5]],
        'Computer programmer': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, Maths, Science',[0.4,0.4,0.3,0.2,0.2,0.5]],
        'Database designer': ['BE CSE, AI/ML, BE IS','S','DSA, Python, C++, C, OOP, Java, DBMS, Maths',[0.4,0.3,0.1,0.1,0.2,0.5]],
        'Counselor': ['Bachelor of Psychology','C','Science, Psychology',[0.1,0.2,0.1,0.5,0.4,0.1]],
        'Social Worker': ['Commerce','C','Social Science',[0.5,0.1,0.1,0.4,0.5,0.1]],
        'Teacher': ['Bachelor of Education (B. Ed.) ','S','Maths, Science',[0.1,0.4,0.2,0.5,0.4,0.3]],
        'Doctor': ['MBBS','S','Science, Biologys',[0.2,0.5,0.2,0.3,0.4,0.2]],
        'Businessman': ['BBA, MBA','C','Social Science',[0.1,0.2,0.2,0.3,0.4,0.3]],
        'Athlete': ['BBA in Sports Management','C','Sports',[0.1,0.1,0.1,0.2,0.3,0.1]],
        'Dancer': ['Bachelor of Performing Arts','A','Dance, Physical Education',[0.2,0.1,0.3,0.2,0.2,0.1]],
        'Physical Education Instructor': ['BBA in Sports Management','A','Sports',[0.2,0.1,0.3,0.3,0.4,0.1]],
        'Actor / Actress': ['Acting School','A','Drama',[0.2,0.1,0.3,0.3,0.4,0.1]],
        'Paramedic': ['MBBS','S','Biology, Science',[0.2,0.1,0.2,0.3,0.5,0.1]],
        'Journalist': ['Bachelor\'s degree in journalism, mass communications','C','Social Science, Literature, English, Language, Political Science',[0.1,0.2,0.3,0.4,0.5,0.1]],
        'Public Speaker': ['Bachelor\'s degree in mass communication','C','Language',[0.1,0.1,0.3,0.4,0.4,0.1]],
        'Politician': ['Political Science','C','Social Science, Civics',[0.1,0.1,0.3,0.5,0.4,0.1]],
        'Psychologist': ['Bachelor in Psychology','S','Science',[0.2,0.4,0.2,0.5,0.4,0.1]],
        'Career counselor': ['Master\'s diploma in career guidance or Master\'s diploma in career guidance  development','S','General Knowledge',[0.1,0.2,0.1,0.5,0.4,0.1]],
        'Writer': ['Degree in  creative writing, communication and media','A','Literature, Language',[0.1,0.3,0.5,0.2,0.3,0.1]],
        'Consultant': ['Postgraduate diploma in career guidance or management','C','General Knowledge',[0.1,0.2,0.3,0.3,0.4,0.1]],
        'Event Management': ['Bachelor\'s degree in event management','C','Drama',[0.4,0.3,0.3,0.4,0.3,0.2]],
        'Graphic Designer': ['B Design','A','Art, Geometry',[0.4,0.4,0.4,0.2,0.2,0.3]],
        'Architect': ['B Arch','S','Maths, Art',[0.4,0.4,0.4,0.2,0.3,0.4]],
        'Fashion Designer': ['Bachelor of design in fashion, BSc in fashion design, BA in fashion design','A','Fashion, Art',[0.2,0.1,0.4,0.2,0.2,0.2]],
        'Interior Decorator': ['Interior Desiging','A','Art, Symmetry',[0.3,0.1,0.4,0.2,0.2,0.2]],
        'Photographer': ['PG Diploma in Photography','A','Geometry',[0.4,0.1,0.4,0.3,0.1,0.1]],
    }

        def li_calc(c):
            if c=='Bachelor of Psychology':
                return "BA psychology is an undergraduate degree offered by universities and colleges across the world. It focuses on the study of human behaviour and the mind. It introduces students to different branches of psychology like criminal psychology, social, counselling, behavioural, group etc."
            elif c=='Sound engineering':
                return "Sound Engineering is the technical study of sound, its characteristics, and nature. A sound engineer, also known as an audio engineer, are the individuals responsible for curating, mixing, reproducing and sound equalization and electronic effects. These professionals help music producers find the exact output they want. "
            elif c=='BE BT':
                return "Biotechnology is the use of biology to solve problems and make useful products. The most prominent approach used is genetic engineering, which enables scientists to tailor an organism's DNA at will."
            elif c=='BE ASE':
                return "Aerospace engineering, also called aeronautical engineering, or astronautical engineering, field of engineering concerned with the design, development, construction, testing, and operation of vehicles operating in the Earth's atmosphere or in outer space."
            elif c=='MBBS':
                return "MBBS full form stands for Bachelor of Medicine, Bachelor of Surgery. An MBBS degree is an undergraduate course for aspirants who want to fulfil their dream of becoming a doctor. It is a professional degree in medical science. After completing the MBBS course and obtaining the degree, students would be qualified as medical practitioners or doctors. "
            elif c=='B Arch':
                return "BArch (Bachelor of Architecture) is an undergraduate degree in the field of architecture. This five-year full-time programme is a blend of theoretical and practical knowledge for students to learn the art of planning, designing and constructing physical structures of various kinds. "
        
            elif c=='B Design':
                return "Bachelor of Design (BDes) or BDesign is an established degree in design field at undergraduate level. B.Des degree is a full-time four-year course offered in various specialisations such as Fashion Designing, Interior Designing, Accessory Designing, Textile Designing and much more. Over the years, the BDes degree has evolved and now offered in various design specialisations such as Graphic Designing, Multimedia Designing, VFX Design, Visual Communication, and Game Designing."
        
            elif c=='BBA, MBA':
                return "The BBA MBA dual degree programme is a five-year undergraduate plus postgraduate integrated course that a candidate can pursue right after passing his or her 10+2 exams. It combines both undergraduate BBA and postgraduate MBA degree programmes in one integrated course. "
            elif c=='Commerce':
                return "Bachelor of Commerce, also known as BCom/BCom (Hons) is an undergraduate degree that can be pursued by students who have cleared Class 12th in Science, Arts or Commerce stream. However, preference is given to students who have studied Commerce at 10+2 level. The duration of the course spans over a period of three years in Indian colleges/Universities."
        
            elif c=='Bachelor of Performing Arts':
                return "The Bachelor's degree in Performing arts (BA in Performing Arts) was started at AIMS Institutes, Bangalore in 2014. It is affiliated to Bangalore University and recognized by the Government of India. The duration of the course is three or four years comprising of six or eight semesters."
        
            elif c=='Interior Desiging':
                return "Interior design is the art and science of enhancing the interior of a building to achieve a healthier and more aesthetically pleasing environment for the people using the space. An interior designer is someone who plans, researches, coordinates, and manages such enhancement projects."
        
            elif c=='B COM, CA':
                return "Bachelor of Commerce, also known as BCom/BCom (Hons) is an undergraduate degree that can be pursued by students who have cleared Class 12th in Science, Arts or Commerce stream. However, preference is given to students who have studied Commerce at 10+2 level. The duration of the course spans over a period of three years in Indian colleges/Universities."
        
            elif c=='BE CSE, AI/ML, BE IS':
                return "BE CSE is a 4 Years undergraduate course that deeply talks about various important aspects of computers. This course includes computer programming, software, operating system, and computer hardware etc. " 
        
            else:
                return ""


        marks=request.form.get("marks")
        dream_careers1=request.form.get("dreamProfessions")
        dream_careers=dream_careers1.split(', ')
        print("Dream professions", dream_careers)
        dream_subjects1 =request.form.get("interestedSubjects")
        dream_subjects=dream_subjects1.split(', ')
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
        
        v17=""
        #to check for common careers
        for i in dream_careers:
            print("Inside loop")
            v17+=i+" "
            print(choice)
            if i in choice:
                final_percentage[i] = final_percentage[i]*2
        print(final_percentage)
        print("Here")
        print(choice,"This is choice")
        print(final_percentage)
        count=0
        for i in dream_subjects:
            print("I AM HERE")
            print(i,subjects_final[choice[count]])
            if i in subjects_final[choice[count]]:
                print("This is final career",choice[count])
                print("I AM HERE")
                final_percentage[choice[count]] = final_percentage[choice[count]]+0.05
            count+=1

       
        print(request.form.get("name"))
        print(request.form.get("date"))
        print(request.form.get("class"))
        print(request.form.get("dob"))
        print(request.form.get("address"))
        print(request.form.get("phone"))
        print(request.form.get("hobbies"))
        print(request.form.get("additionalSkills"))
        print(request.form.get("qualitiesLiked"))
        print(request.form.get("qualitiesAdmired"))
        print(final_percentage)

    
        S=0
        A=0
        C=0
        for i in list(final_percentage.keys()):
            print(i)
            if d[i][1]=='S':
                S+=1
            elif d[i][1]=='A':
                A+=1
            else:
                C+=1
            if S>C and S>A:
                greatest='Science'
                if C>A:
                    middle='Commerce'
                    low='Arts'
                else:
                    middle='Arts'
                    low='Commerce'
            elif C>S and C>A:
                greatest='Commerce'
                if S>A:
                    middle='Science'
                    low='Arts'
                else:
                    middle='Arts'
                    low='Science'
            else:
                greatest='Arts'
                if S>C:
                    middle='Science'
                    low='Commerce'
                else:
                    middle='Commerce'
                    low='Science'

        v21=""
        v21= greatest+", "+middle+", "+low

        def v21_calc(c):
            if c=='Science':
                return "Qualities of mathematical reasoning and logical thinking come into play here. There are mainly two branches in the science stream: one is the non-medical stream (PCM), and another is the Medical stream (PCB). Physics and chemistry are standard for both streams. Maths is opted by the students who kick start their career in non-medical streams like Engineering and Architecture."
            elif c=='Arts':
                return "This field is called the art field, in which a person moves towards advancing his career through different types of arts. In this you can get Bachelor of Art, Bachelor of Arts in English, Bachelor of Art in Business, Bachelor of Management, Bachelor of Physical Education, Bachelor of Business Studies, Bachelor of Business Administration, Bachelor of Fine Art and many more "
            else:
                return "Commerce stream is a group of educational courses that deals with the study of trade, business, and accounts. Business activities such as goods exchange and providing services to consumers make up the foundation of commerce stream courses."


        v3 = ""
        branch_list = [greatest, middle, low]
        print(final_percentage.keys())
        for i in range(0,4):
            if i==3:
                v3+=list(final_percentage.keys())[i]
            else:
                v3=v3+list(final_percentage.keys())[i]+", "
    
        li = list(final_percentage.keys())
        print("FINAL LIST IS ----->", li)
        st=set()
        for i in li:
            st.add(d[i][0])
            if(len(st)==5):
                break
        print(st)
        st=list(st)
        if len(st) < 5:
            while len(st) < 5:
                st.append("")
        template_path = os.path.join('./', 'Sample DF Report.docx')
        template = DocxTemplate(template_path)
        to_fill_in = {'Name' : request.form.get("name"),
                    'DOB' :  request.form.get("dob"),
                    'Gender' : 'female',
                    'Class' : request.form.get("class"),
                    'var1': dream_careers1,
                    'var2': v3,
                    'var3': dream_subjects1,
                    'var4': request.form.get("hobbies"),
                    'var5': 12,  #
                    'var6': 30,  #
                    'var7': 26,  #
                    'var8': 10,  #
                    'var44': 5,  #
                    'var45': 20, #
                    'var9': scores[4],
                    'var10': scores[5],
                    'var11': scores[6],
                    'var12' : scores[2],
                    'var13': scores[1],
                    'var14': 'Confident, Team player, Quick to adapt',
                    'var15': 'Hardworking, agile',
                    'var16': v3,
                    'var17': v17,
                    'var18': request.form.get("additionalSkills"),
                    'var19': 'Communication, Interpersonal skills',
                    'var20': 'Networking, leadership qualities',
                    'var50': branch_list[0],
                    'var21': branch_list[1],
                     'var22': v21_calc(branch_list[0]),
                      'var23': v21_calc(branch_list[1]),
                       'var24': st[0],
                         'var25': li_calc(st[0]),
                        'var26': st[1],
                         'var27': li_calc(st[1]),
                         'var28': st[2],
                          'var29': li_calc(st[2]),
                          'var30': st[3],
                           'var31': li_calc(st[3]),
                          'var32': st[4],
                           'var33': li_calc(st[4]),
                          'var34':d[li[0]][2],
                          'var35':d[li[1]][2],
                          'var36':d[li[2]][2],
                          'var37':d[li[3]][2],
                          'var38':d[li[4]][2],
                          'var39':li[0],
                          'var40':li[1],
                          'var41':li[2],
                          'var42':li[3],
                          'var43':li[4]
  
                    
                    }


        template.render(to_fill_in)
        filename = 'hack_draft.docx'
        filled_path = os.path.join('./'+filename)
        template.save(filled_path)
        doc = aw.Document("hack_draft.docx")
        # doc.save("final.pdf")
        # return render_template("final.html", check=-1)
        
# Restart application whenever changes are made
if __name__ == "__main__":
    app.run(debug = True)