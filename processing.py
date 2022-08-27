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
mi_scores = [3,4,6,7,2,5,2,7]
#mi_subjects = ['LIN', 'I-M', 'SP', 'B-K', 'MU', 'NTER', 'NTRA', 'NAT']
mi_subjects = ['LIN', 'I-M', 'SP', 'Lin', 'MU', 'NTER', 'NTRA', 'NAT']
non_academic = ['carpenter', 'farmer', 'painter', 'pottery']
marks = 30
top5=[]
dream_careers = ['Astronomer','Politician','Writer']
riasec = [0.1,0.1,0.1,0.1,0.1]
mi_careers = {'Lin': ['Astronomer','Botanist','Conservationist', 'Ecologist','Meteorologist'],
    'I-M': ['Audiologist','Audiologist', 'Sound editor', 'Music conductor','Recording engineer','Songwriter'],
    'SP': ['Accountant','Computer analyst', 'Computer technician','Computer programmer','Database designer' ],
    }

dream_subjects =['science','math','physics']


def assign_career():

    final_percentage={}
    if marks<=30:
        top5 = non_academic

    domain = mi_subjects[mi_scores.index(max(mi_scores))]
    choice =  mi_careers[domain]   #will be a list
    print("This is choice", choice)

    value = 1/(len(dream_careers)+5)
    

    for i in choice:   #assign equal values
        print(i)
        temp=d[i][2]
        choice_subjects=temp.split(', ')
        final_percentage[i]= value
        print("choice subjects", choice_subjects)
    
    for i in dream_careers:
        final_percentage[i]=value
    print(final_percentage)
    

    #to check for common careers
    for i in dream_careers:
        if i in choice:
            final_percentage[i] = final_percentage[i]*2
    print(final_percentage)
    print(choice,"Thus is choice")
    temp='Astronomer'
    for i in dream_subjects:
        if i in choice_subjects:
            final_percentage[temp] = final_percentage[temp]+0.05

    print(final_percentage)
assign_career()










