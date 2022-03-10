import sqlite3

connection = sqlite3.connect("teachers.db")
cur = connection.cursor()

try:
    cur.execute("SELECT tid FROM teachers LIMIT 1")
except sqlite3.OperationalError:
    cur.execute('''
        CREATE TABLE teachers(
            tid INT PRIMARY KEY,
            tname VARCHAR(255),
            tdesign VARCHAR(64),
            tdept VARHCAR(50)
        )
    ''')


teachers = [{
  "tid": 1,
  "tname": "Fay Lohden",
  "tdesign": "Assistant Professor",
  "tdept": "Information Technology"
}, {
  "tid": 2,
  "tname": "Andrey Emnoney",
  "tdesign": "Assistant Professor",
  "tdept": "Biotechnology"
}, {
  "tid": 3,
  "tname": "Madelon Rounce",
  "tdesign": "Assistant Professor",
  "tdept": "Information Technology"
}, {
  "tid": 4,
  "tname": "Roxie Leist",
  "tdesign": "Head of Department",
  "tdept": "Computer Science"
}, {
  "tid": 5,
  "tname": "Calvin Filpi",
  "tdesign": "Assistant Professor",
  "tdept": "Computer Science"
}, {
  "tid": 6,
  "tname": "Courtnay Salmons",
  "tdesign": "Head of Department",
  "tdept": "Biotechnology"
}, {
  "tid": 7,
  "tname": "Bab Tinkler",
  "tdesign": "Assistant Professor",
  "tdept": "Computer Science"
}, {
  "tid": 8,
  "tname": "Theodosia Ibanez",
  "tdesign": "Head of Department",
  "tdept": "Information Technology"
}, {
  "tid": 9,
  "tname": "Rollin Di Meo",
  "tdesign": "Assistant Professor",
  "tdept": "Computer Science"
}, {
  "tid": 10,
  "tname": "Udale MacRinn",
  "tdesign": "Assistant Professor",
  "tdept": "Information Technology"
}]

for teacher in teachers:
    cur.execute("INSERT INTO teachers(tid, tname, tdesign, tdept) VALUES (?, ?, ?, ?)",
    (teacher["tid"],teacher["tname"],teacher["tdesign"], teacher["tdept"]))

for row in cur.execute("SELECT * FROM teachers"):
    print(row)


connection.commit()
connection.close()