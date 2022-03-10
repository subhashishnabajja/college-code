import sqlite3

connection = sqlite3.connect("courses.db")
cur = connection.cursor()

try:
    cur.execute("SELECT sid FROM courses LIMIT 1")
except sqlite3.OperationalError:
    cur.execute('''
        CREATE TABLE courses(
            cid INT PRIMARY KEY,
            cname VARCHAR(255)
        )
    ''')


courses = [
    {
        "cid": 1,
        "cname": "Computer Science"
    },
    {
        "cid": 2,
        "cname": "Information Technology"
    },
    {
        "cid": 3,
        "cname": "Biotechnology"
    },
    {
        "cid": 4,
        "cname": "Mass media"
    }
]

for course in courses:
    cur.execute("INSERT INTO courses(cid, cname) VALUES (?, ?)",
    (course["cid"],course["cname"]))

for row in cur.execute("SELECT * FROM courses"):
    print(row)


connection.commit()
connection.close()