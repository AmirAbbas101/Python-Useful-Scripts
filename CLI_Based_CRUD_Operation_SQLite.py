import mysql.connector

# Connect to MySQL
def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="558822",
        database="student"
    )

# Create a new student record
def create_student(conn, regNo, name):
    cursor = conn.cursor()
    sql = "INSERT INTO bscs21 (regNo, name) VALUES (%s, %s)"
    cursor.execute(sql, (regNo, name))
    conn.commit()
    print("Student added successfully")

# Read all students
def read_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bscs21")
    students = cursor.fetchall()
    for student in students:
        print(student)

# Update student record by regNo
def update_student(conn, regNo, new_name):
    cursor = conn.cursor()
    sql = "UPDATE bscs21 SET name = %s WHERE regNo = %s"
    cursor.execute(sql, (new_name, regNo))
    conn.commit()
    print("Student updated successfully")

# Delete student record by regNo
def delete_student(conn, regNo):
    cursor = conn.cursor()
    sql = "DELETE FROM bscs21 WHERE regNo = %s"
    cursor.execute(sql, (regNo,))
    conn.commit()
    print("Student deleted successfully")

# Main function to run the CLI
def main():
    conn = connect()
    while True:
        print("\n1. Create student\n2. Read all students\n3. Update student\n4. Delete student\n5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            regNo = int(input("Enter registration number: "))
            name = input("Enter name: ")
            create_student(conn, regNo, name)
        elif choice == "2":
            read_students(conn)
        elif choice == "3":
            regNo = int(input("Enter registration number of the student to update: "))
            new_name = input("Enter new name: ")
            update_student(conn, regNo, new_name)
        elif choice == "4":
            regNo = int(input("Enter registration number of the student to delete: "))
            delete_student(conn, regNo)
        elif choice == "5":
            break
        else:
            print("Invalid choice")

    conn.close()

if __name__ == "__main__":
    main()
