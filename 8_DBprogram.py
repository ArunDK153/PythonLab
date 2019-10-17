import sqlite3
from sqlite3 import Error
 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn
 
def create_table(conn, create_table):
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)

def create_student(conn, student):
    sql = 'INSERT INTO student VALUES(?,?,?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, student)

def retrieve_particular_student(conn,Id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE id=?", (Id,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def retrieve_all_students(conn,Id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def update_student(conn, student):
    sql = 'UPDATE student SET name=?, age=?,branch=?, marks=? WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()

def delete_all(conn):
    sql = 'DELETE FROM student'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def delete_particular_student(conn,Id):
    sql = 'DELETE FROM tasks where id = ?'
    cur = conn.cursor()
    cur.execute(sql,(Id,))
    conn.commit()
 
def main():
    database = "student.db"
    create_student_table = ''' CREATE TABLE IF NOT EXISTS STUDENT
                                    (ID INT PRIMARY KEY NOT NULL,
                                     NAME TEXT NOT NULL, AGE INT NOT NULL,
                                    BRANCH TEXT, CGPA DECIMAL(4,2) NOT NULL); '''
    conn = create_connection(database)
    if conn is not None:
        create_table(conn, create_student_table)
    else:
        print("Error! Cannot create the database connection.")

    while True:
        choice = int(input("""\n1. Insert new student information\n2. Display student information\n
                           3. Update student information\n4. Delete student information\n"""))
        if choice==1:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            branch = input("Enter student branch: ")
            marks = float('%.2f'%float(input("Enter student CGPA: ")))
            student= (id,name,age,branch,cgpa)
            
            conn = create_connection(database)
            with conn:
                create_student(conn,student)
                print("Information updated succesfully.\n")

        if choice==2:
            All = input("\n1. Display all students info\n2. Display particular student info\n")
            if All==1:
                
                
if __name__ == '__main__':
    main()
