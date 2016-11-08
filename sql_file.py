import sqlite3


# function to create database
def create_table():
    conn = sqlite3.connect('podomoro.db')
    c = conn.cursor()

    conn.execute('''CREATE TABLE IF NOT EXISTS Pomodoro (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        taskname TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        cycletime TEXT,
        cycles INT)
        ''')
    conn.commit()


# function to input data to table
def input_data(task_name, time_stamp, cycle_time, cycles):
    conn = sqlite3.connect('podomoro.db')
    c = conn.cursor()
    c.execute("INSERT INTO Pomodoro (taskname , timestamp, cycletime, cycles) VALUES (?,?,?,?)",
              (task_name, time_stamp, cycle_time, cycles))
    conn.commit()


# function to delete all tasks
def delete_all_task():
    conn = sqlite3.connect('podomoro.db')
    c = conn.cursor()
    c.execute("""DELETE from Pomodoro""")
    conn.commit()


# function to select tasks of certain day
def list_day(time_stamp):
    conn = sqlite3.connect('podomoro.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM Pomodoro WHERE timestamp = ?;""", (time_stamp,))
    data = c.fetchall()
    for row in data:
        print str(row[0]) + str(row[1]) + str(row[2]) + str(row[3])

# list_day("2016-11-07")


# function to select all tasks
def list_all():
    conn = sqlite3.connect('podomoro.db')
    c = conn.cursor()
    c.execute("""SELECT * FROM Pomodoro""")
    data = c.fetchall()
    for row in data:
        print str(row[0]) + str(row[1]) + str(row[2]) + str(row[3])

list_all()
