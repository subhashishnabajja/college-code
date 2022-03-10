import sqlite3

connection = sqlite3.connect("students.db")
cur = connection.cursor()

try:
    cur.execute("SELECT sid FROM students LIMIT 1")
except sqlite3.OperationalError:
    cur.execute('''
        CREATE TABLE students(
            sid INT PRIMARY KEY,
            sname VARCHAR(255),
            sdept VARHCAR(50)
        )
    ''')


students = [{
  "sid": 1,
  "sname": "Eldon Doumic",
  "sdept": "Computer Science"
}, {
  "sid": 2,
  "sname": "Ursula Vasyagin",
  "sdept": "Computer Science"
}, {
  "sid": 3,
  "sname": "Kale Doble",
  "sdept": "Computer Science"
}, {
  "sid": 4,
  "sname": "Brandy Gosse",
  "sdept": "Computer Science"
}, {
  "sid": 5,
  "sname": "Niall Gehrtz",
  "sdept": "Computer Science"
}, {
  "sid": 6,
  "sname": "Henrietta Pirozzi",
  "sdept": "Computer Science"
}, {
  "sid": 7,
  "sname": "Lyndel Russell",
  "sdept": "Information Technology"
}, {
  "sid": 8,
  "sname": "Dimitry Chantler",
  "sdept": "Computer Science"
}, {
  "sid": 9,
  "sname": "Irena Rounce",
  "sdept": "Computer Science"
}, {
  "sid": 10,
  "sname": "Frederick Dumphreys",
  "sdept": "Computer Science"
}, {
  "sid": 11,
  "sname": "Connie Thomason",
  "sdept": "Computer Science"
}, {
  "sid": 12,
  "sname": "Lorrie MacCarter",
  "sdept": "Information Technology"
}, {
  "sid": 13,
  "sname": "Pru Broadfoot",
  "sdept": "Information Technology"
}, {
  "sid": 14,
  "sname": "Lilian Snassell",
  "sdept": "Information Technology"
}, {
  "sid": 15,
  "sname": "Rosamond Le Moucheux",
  "sdept": "Information Technology"
}, {
  "sid": 16,
  "sname": "Abbie Monaghan",
  "sdept": "Biotechnology"
}, {
  "sid": 17,
  "sname": "Irvin Bestar",
  "sdept": "Information Technology"
}, {
  "sid": 18,
  "sname": "Bing Olivey",
  "sdept": "Biotechnology"
}, {
  "sid": 19,
  "sname": "Loren Radke",
  "sdept": "Biotechnology"
}, {
  "sid": 20,
  "sname": "Isabeau Laurencot",
  "sdept": "Biotechnology"
}]

for student in students:
    cur.execute("INSERT INTO students(sid, sname, sdept) VALUES (?, ?, ?)",
    (student["sid"],student["sname"], student["sdept"]))

for row in cur.execute("SELECT * FROM students"):
    print(row)


connection.commit()
connection.close()