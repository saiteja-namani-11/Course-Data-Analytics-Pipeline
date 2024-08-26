import random
import pandas as pd
import requests 
import logging 
import json
import os
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

seed = int(os.environ.get('SEED', 42))
random.seed(seed)
logging.info(f"Random number seed: {seed}")

grades = { "A" : 4.0, "A-" : 3.667, "B+": 3.333, "B": 3.0 , "B-" : 2.667, "C+" : 2.333 ,"C": 2.0}

grade_dists = [
    { 'code' : 'IST659', 'prereq' : [],  'program' : ['IS', 'DS'], 'values' : [60,22,8,3,3,2,2] },
    { 'code' : 'IST722', 'prereq' : ['IST659'], 'program' : ['IS'],'values' : [57,18,15,3,3,2,2] },
    { 'code' : 'IST769', 'prereq' : ['IST659'], 'program' : ['DS'], 'values' : [55,20,12,5,4,2,2] },
    { 'code' : 'IST615', 'prereq' : [], 'program' : ['IS','DS'],'values' : [60,20,10,3,3,2,2] },
    { 'code' : 'IST714', 'prereq' : ['IST615'], 'program' : ['IS'], 'values' : [55,25,10,3,3,2,2] },
    { 'code' : 'IST621', 'prereq' : [], 'program' : ['IS'],'values' : [70,10,10,3,3,2,2] },
    { 'code' : 'IST687', 'prereq' : [], 'program' : ['DS'],'values' : [60,22,8,3,3,2,2] },
    { 'code' : 'IST718', 'prereq' : ['IST687'], 'program' : ['DS'], 'values' : [58,20,12,3,3,2,2] },
    { 'code' : 'IST707', 'prereq' : ['IST687'], 'program' : ['DS'], 'values' : [55,20,12,3,3,2,2] }
]

section_dists = [
    { 'code' : 'IST659', 'Fall' : (2,2), 'Spring' : (1,2), 'Enrollment': (90,100), 'capacity' : (20, 24)},
    { 'code' : 'IST722', 'Fall' : (1,1), 'Spring' : (0,0), 'Enrollment': (90,100), 'capacity' : (24, 28)},
    { 'code' : 'IST769', 'Fall' : (0,0), 'Spring' : (1,1), 'Enrollment': (80,95), 'capacity' : (24, 28)},
    { 'code' : 'IST615', 'Fall' : (1,1), 'Spring' : (1,2), 'Enrollment': (80,95), 'capacity' : (24, 28)},
    { 'code' : 'IST714', 'Fall' : (0,0), 'Spring' : (1,1), 'Enrollment': (85,90), 'capacity' : (20, 24)},
    { 'code' : 'IST621', 'Fall' : (1,1), 'Spring' : (1,2), 'Enrollment': (90,100), 'capacity' : (24, 28)},
    { 'code' : 'IST687', 'Fall' : (2,2), 'Spring' : (1,2), 'Enrollment': (90,100), 'capacity' : (20, 24)},
    { 'code' : 'IST718', 'Fall' : (0,0), 'Spring' : (1,1), 'Enrollment': (85,100), 'capacity' : (24, 28)},
    { 'code' : 'IST707', 'Fall' : (1,1), 'Spring' : (0,0), 'Enrollment': (85,100), 'capacity' : (24, 28)}
]

program_dists = [
    { 'code' : 'IS', 'Pct' : 45},
    { 'code' : 'DS', 'Pct' : 55 }
]

terms = [
    { '_id' : '1221', 'code' : '1221', 'name' : 'Fall 2021', 'semester' : 'Fall', 'year' : 2021, 'academic_year' : '2021-2022' },
    { '_id' : '1222', 'code' : '1222', 'name' : 'Spring 2022', 'semester' : 'Spring', 'year' : 2022, 'academic_year' : '2021-2022'  },
    { '_id' : '1231', 'code' : '1231', 'name' : 'Fall 2022', 'semester' : 'Fall', 'year' : 2022, 'academic_year' : '2022-2023'  },
    { '_id' : '1232', 'code' : '1232', 'name' : 'Spring 2023', 'semester' : 'Spring', 'year' : 2023, 'academic_year' : '2022-2023'  }
]

programs = [
    { 
        '_id' : 'IS',
        'code' : 'IS', 
        'name' : 'Information Systems',
        'type' : 'Masters',
        'credits' : 36,
        'required_courses' : ['IST659', 'IST615', 'IST621'],
        'elective_courses' : ['IST722', 'IST714', 'IST687', 'IST707']
    },
    { 
        '_id' : 'DS',
        'code' : 'DS', 
        'name' : 'Data Science',
        'type' : 'Masters',
        'credits' : 34,
        'required_courses' : ['IST659', 'IST615', 'IST687','IST718', 'IST707'],
        'elective_courses' : ['IST769', 'IST714', ]
    },
    {
        '_id' : 'BDC',
        'code' : 'BDC',
        'name' : 'Data Engineering Certificate',
        'type' : 'Certificate',
        'credits' : 9,
        'required_courses' : ['IST659', 'IST722', 'IST769'],
    },
    {
        '_id' : 'CCC',
        'code' : 'CCC',
        'name' : 'Cloud Computing Certificate',
        'type' : 'Certificate',
        'credits' : 9,
        'required_courses' : ['IST621', 'IST615', 'IST714']
    },
    {
        '_id' : 'MLC',
        'code' : 'MLC',
        'name' : 'Machine Learning Certificate',
        'type' : 'Certificate',
        'credits' : 9,
        'required_courses' : ['IST687', 'IST707', 'IST718']
    }
]

courses = [
        {   '_id': 'IST659', 'code' : 'IST659', 
            'name' : 'Data Administration Concepts and Database Management', 
            'description' : 'Definition, development, and management of databases for information systems. Data analysis techniques, data modeling, and schema design. Query languages and search specifications. Overview of file organization for databases. Data administration concepts and skills.' ,
            'credits' : 3,
            'prerequisites' : [],
            'required_in_programs': [ 'IS', 'DS'],
            'elective_in_programs' : [],
            'key_assignments': [ 'project']
        },
        {
            '_id': 'IST722', 'code' : 'IST722', 
            'name' : 'Data Warehousing', 
            'description' : 'Introduction to concepts of business intelligence (BI) and the practice/techniques in building a BI solution. Focuses are on how to use data warehouses as a BI solution to make better organizational decisions.',
            'credits' : 3,
            'prerequisites' : ['IST659'],
            'required_in_programs': [],
            'elective_in_programs' : ['IS'],
            'key_assignments': [ 'project', 'exam']
        },
        {
            '_id': 'IST769','code' : 'IST769', 
            'name' : 'Advanced Big Data Management', 
            'description': 'Analyze relational and non-relational databases and corresponding database management system architectures. Learn to build complex database objects to support a variety of needs from big data and traditional perspectives. Data systems performance, scalability, security.',
            'credits' : 3,
            'prerequisites' : ['IST659'],
            'required_in_programs': [],
            'elective_in_programs' : ['DS'],
            'key_assignments': [ 'project', 'exam' ]
        },
        {
            '_id': 'IST615', 'code' : 'IST615',
            'name' : 'Cloud Management',
            'description' : 'Cloud services creation and management. Practical experience in using, creating and managing digital services across data centers and hybrid clouds. Strategic choices for cloud digital service solutions across open data centers and software defined networks.',
            'credits' : 3,
            'prerequisites' : [],
            'required_in_programs': [ 'IS', 'DS'],
            'elective_in_programs' : [],
            'key_assignments': [ 'project', 'paper' ]
        },
        {
            '_id': 'IST714', 'code' : 'IST714',
            'name' : 'Cloud Architecture',
            'description' : 'Advanced, lab-based exploration of enterprise cloud migration/adoption costs, planning and economics; cloud application/service design, network and data center resource orchestration. Topics also include cloud elastic sizing, risk management, governance, compliance and monitoring.',
            'credits' : 3,
            'prerequisites' : ['IST615'],
            'required_in_programs': [],
            'elective_in_programs' : ['IS', 'DS'],
            'key_assignments': [ 'project' ]
        },
        {
            '_id': 'IST621', 'code' : 'IST621',
            'name' : 'Information Management and Technology',
            'description' : 'Information and technology management overview with a focus on digital transformation. How information and technology managers create organizational, technological, and personal capabilities to succeed in a rapidly changing digital world.',
            'credits' : 3,
            'prerequisites' : [],
            'required_in_programs': [ 'IS'],
            'elective_in_programs' : [],
            'key_assignments': [ 'paper' ]
        },
        {
            '_id': 'IST687', 'code' : 'IST687',
            'name' : 'Introduction to Data Science',
            'description' : 'Introduces information professionals to fundamentals about data and the standards, technologies, and methods for organizing, managing, curating, preserving, and using data. Discusses broader issues relating to data management, quality control and publication of data.',
            'credits' : 3,
            'prerequisites' : [],
            'required_in_programs': [ 'DS'],
            'elective_in_programs' : [ 'IS' ],
            'key_assignments': [ 'project', 'exam' ]
        },
        {
            '_id': 'IST707', 'code' : 'IST707',
            'name' : 'Applied Machine Learning',
            'description' : 'General overview of industry standard machine learning techniques and algorithms. Focus on machine learning model building and optimization, real-world applications, and future directions in the field. Hands-on experience with modern data science packages.',
            'credits' : 3,
            'prerequisites' : ['IST687'],
            'required_in_programs': [ 'DS'],
            'elective_in_programs' : [ 'IS' ],
            'key_assignments': [ 'exam' ]
        },
        {
            '_id': 'IST718', 'code' : 'IST718',
            'name' : 'Big Data Analytics',
            'description' : 'A broad introduction to big data analytical and processing tools for information professionals. Students will develop a portfolio of theoretical and practical resources for several real-world case studies.',
            'credits' : 3,
            'prerequisites' : ['IST687'],
            'required_in_programs': [ 'DS'],
            'elective_in_programs' : [],
            'key_assignments': [ 'project' ]
        }
]

def generate_sections(terms, section_dists):
    sections = []
    for term in terms:
        # logging.info(term)
        for section_dist in section_dists:
            if term['code'].endswith("1"): # Fall
                section_count = random.randint(section_dist['Fall'][0], section_dist['Fall'][1])
            else: # Spring
                section_count = random.randint(section_dist['Spring'][0], section_dist['Spring'][1])
            for i in range(section_count):
                capacity = random.choice(section_dist['capacity'])
                enrollment_pct = random.choice(section_dist['Enrollment'])
                enrollment = capacity if enrollment_pct == 100 else int(enrollment_pct * capacity / 100) + random.randint(-2,2)
                section = {
                    'term' : term['code'],
                    'course' : section_dist['code'],
                    'section' : f"M{i+1:03}",
                    'enrollment': enrollment,
                    'capacity' : capacity
                }
                # logging.info(section)
                sections.append(section)
                # random.randint(section_dist['Enrollment'][0], section_dist['Enrollment'][1])

    return sections

def generate_students(program_dists):
    response = requests.get("https://raw.githubusercontent.com/mafudge/datasets/master/funny-names/funny-names.tsv")
    names = response.text.split("\n")
    names = [ f"{n.split()[0].strip()} {n.split()[1].strip()}" for n in names ]
    students = []
    for name in names:
        program = random.choices(program_dists, weights=[p['Pct'] for p in program_dists])[0]
        student = {
            '_id': name.lower().replace(" ", "").strip(),
            'name' : name,
            'program' : program['code']
        }
        students.append(student)
    return students


def generate_enrollments(sections, students, grade_dists):
    enrollments = []
    for section in sections[:]:
        # logging.info(section)
        grade_dist = [ gd for gd in grade_dists if gd['code']==section['course']][0]
        # logging.info(grade_dist)
        n = 0 
        while n < section['enrollment']:
            student = random.choice(students)
            student_courses = [ e['course'] for e in enrollments if e['student_id'] == student['_id']]
            # logging.info(student_courses)
            if True: #student['program'] in grade_dist['program']: # student is in program
                if section['course'] not in student_courses: # student has not taken course
                    if grade_dist['prereq'] == [] or grade_dist['prereq'][0] in student_courses: # took prereq
                        n += 1
                        letter = random.choices(["A","A-","B+","B", "B-", "C+","C"], grade_dist['values'],k=1)[0]
                        enrollment = {
                            'term' : section['term'],
                            'course_enrollment' : n,
                            'course' : section['course'],
                            'section' : section['section'],
                            'student_id' : student['_id'],
                            'grade' : letter,
                            'grade_points' : grades[letter]
                        }
                        # logging.info(enrollment)
                        enrollments.append(enrollment)
     
    return enrollments

def save_json(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

def save_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == '__main__':
    from pymongo import MongoClient
    logging.info("Generating data...")
    DATAPATH = "data/"
    students = generate_students(program_dists)
    sections =   generate_sections(terms, section_dists)
    enrollments = generate_enrollments(sections, students, grade_dists)
    logging.info("Saving data...")
    save_json(students, DATAPATH + "students.json")
    save_json(courses,DATAPATH + "courses.json")
    save_json(programs, DATAPATH + "programs.json")
    save_json(terms, DATAPATH + "terms.json")
    save_csv(sections, DATAPATH + "sections.csv")
    save_csv(enrollments, DATAPATH + "enrollments.csv")

    CONNECTION_STRING = "mongodb://admin:mongopw@mongo:27017"

    logging.info("Writing data to MongoDB...")
    client = MongoClient(CONNECTION_STRING)
    client.drop_database('ischooldb')
    db = client.ischooldb
    db.courses.insert_many(courses)
    db.programs.insert_many(programs)
    db.terms.insert_many(terms)
    db.students.insert_many(students)

