import sqlite3
from sqlite3 import Error
 
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        print("\n")
    return conn
 
def create_table(conn, create_table):
    try:
        c = conn.cursor()
        c.execute(create_table)
    except Error as e:
        print(e)
        print("\n")

def create_student(conn, student):
    sql = 'INSERT INTO student VALUES(?,?,?,?,?)'
    cur = conn.cursor()
    cur.execute(sql, student)

def retrieve_particular_student(conn,Id):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE id=?", (Id,))
    rows = cur.fetchall()
    if len(rows)>0:
        for row in rows:
            print("Student ID: ",str(row[0]),"\nStudent name: ",str(row[1]),"\nStudent age: ",str(row[2]),"\nStudent branch: ",str(row[3]),"\nStudent CGPA: ",str(row[4]),"\n")
    else:
        print("Student doesn't exist.\n")

def retrieve_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    if len(rows)>0:
        i=1
        for row in rows:
            print("Student ",str(i),"\n")
            print("Student ID: ",str(row[0]),"\nStudent name: ",str(row[1]),"\nStudent age: ",str(row[2]),"\nStudent branch: ",str(row[3]),"\nStudent CGPA: ",str(row[4]),"\n")
            i+=1
    else:
        print("No students exist.\n")

def update_student(conn, Id):
    sql = 'UPDATE student SET name=?, age=?,branch=?, cgpa=? WHERE id=?'
    cur = conn.cursor()
    cur.execute('SELECT * FROM student WHERE id=?',(Id,))
    if len(cur.fetchall())>0:
        print("Enter other details to update.\n")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        branch = input("Enter student branch: ")
        cgpa = float('%.2f'%float(input("Enter student CGPA: ")))
        student= (name,age,branch,cgpa,Id)
        cur.execute(sql, student)
        conn.commit()
        print("Information updated succesfully.\n")
    else:
        print("Student doesn't exist.\n")

def delete_all(conn):
    sql = 'DELETE FROM student'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

def delete_particular_student(conn,Id):
    sql = 'DELETE FROM student where id = ?'
    cur = conn.cursor()
    cur.execute('SELECT * FROM student WHERE id=?',(Id,))
    if len(cur.fetchall())>0:
        cur.execute(sql,(Id,))
        conn.commit()
        print("Student record deleted succesfully.\n")
    else:
        print("Student doesn't exist.\n")
 
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
        print("Error! Cannot create the database connection.\n")

    while True:
        choice = int(input("\n1. Insert new student information\n2. Display student information\n3. Update student information\n4. Delete student information\n5. Exit\n"))
        if choice==1:
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            branch = input("Enter student branch: ")
            cgpa = float('%.2f'%float(input("Enter student CGPA: ")))
            student= (id,name,age,branch,cgpa)
            
            conn = create_connection(database)
            with conn:
                create_student(conn,student)
                print("Information updated succesfully.\n")

        elif choice==2:
            All = int(input("\n1. Display all students info\n2. Display particular student info\n"))
            if All==1:
                conn = create_connection(database)
                with conn:
                    retrieve_all_students(conn)
                    print("\n")
            elif All==2:
                conn = create_connection(database)
                sid = int(input("Enter student ID: "))
                with conn:
                    retrieve_particular_student(conn,sid)
                    print("\n")
            else:
                print("Invalid option.\n")

        elif choice==3:
            conn = create_connection(database)
            sid = int(input("Enter student ID to update: "))
            with conn:
                update_student(conn,sid)

        elif choice==4:
            All = int(input("\n1. Delete all students info\n2. Delete particular student info\n"))
            if All==1:
                conn = create_connection(database)
                with conn:
                    delete_all(conn)
                    print("All records deleted successfully.\n")
            elif All==2:
                conn = create_connection(database)
                sid = int(input("Enter student ID to delete: "))
                with conn:
                    delete_particular_student(conn,sid)
            else:
                print("Invalid option.\n")

        elif choice==5:
            return

        else:
            print("Invalid option.\n")
            
if __name__ == '__main__':
    main()
