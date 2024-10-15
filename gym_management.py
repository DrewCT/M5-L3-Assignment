import mysql.connector
from mysql.connector import Error

host='localhost'
user='root'
password='ur_pw'
db_name='M5_l2_Assignment'

try: 
    conn = mysql.connector.connect(
        database = db_name,
        user = user,
        password = password,
        host = host
    )

    if conn.is_connected():
        print("Connected to MySQL database successfully")

except Error as e:
    print(f"Error connecting to the database: {e}")
      
finally:
    if conn and conn.is_connected():
        conn.close()
        print("MySQL conn is closed.")  


# Task 1: Add a Member
def add_member(id, name, age):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            sql_query = "INSERT INTO Members (id, name, age) VALUES (%s, %s, %s)"
            cursor.execute(sql_query, (id, name, age))
            conn.commit()
            print("Member added successfully.")
    except Error as e:
        print(f"Error adding member: {e}")
    finally:
        if conn:
            conn.close()

# Task 2: Add a Workout Session
def add_workout_session(member_id, date, session_time, activity):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            sql_query = """
            INSERT INTO WorkoutSessions (member_id, session_date, session_time, activity) 
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(sql_query, (member_id, date, session_time, activity))
            conn.commit()
            print("Workout session added successfully.")
    except Error as e:
        print(f"Error adding workout session: {e}")
    finally:
        if conn:
            conn.close()

# Task 3: Updating Member Information
def update_member_age(member_id, new_age):
    try:
       if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Members WHERE id = %s", (member_id,))
        if cursor.fetchone():
                sql_query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(sql_query, (new_age, member_id))
                conn.commit()
                print("Member age updated successfully.")
        else:
                print("Member not found.")
    except Error as e:
        print(f"Error updating member age: {e}")
    finally:
        if conn:
            conn.close()

# Task 4: Delete a Workout Session
def delete_workout_session(session_id):
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM WorkoutSessions WHERE session_id = %s", (session_id,))
            if cursor.fetchone():
                sql_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(sql_query, (session_id,))
                conn.commit()
                print("Workout session deleted successfully.")
            else:
                print("Session not found.")
    except Error as e:
        print(f"Error deleting workout session: {e}")
    finally:
        if conn:
            conn.close()


add_member(1, 'Johnny Doe', 28)
add_workout_session(1, '2024-01-19', '10:00 AM', 'Hoop Session')
update_member_age(1, 29)
delete_workout_session(1)