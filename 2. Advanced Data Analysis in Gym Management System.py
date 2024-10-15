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

    start_age = 20
    end_age = 30

def get_members_in_age_range(start_age, end_age):
    conn = conn.is_connected()

if conn:
    try:
        cursor = conn.cursor(dictionary=True) 
        sql_query = """
        SELECT id, name, age
        FROM Members
        WHERE age BETWEEN %s AND %s;
        """
        cursor.execute(sql_query, (start_age, end_age))  
        results = cursor.fetchall()  

        if results:
            print(f"Members aged between {start_age} and {end_age}:")
            for member in results:
                print(f"ID: {member['id']}, Name: {member['name']}, Age: {member['age']}")
        else:
                print(f"No members found between the ages of {start_age} and {end_age}.")

    except mysql.connector.Error as e:
        print(f"Error executing query: {e}")
    finally:
        cursor.close()  
        conn.close()  

# Example usage of the function
if __name__ == "__main__":
    get_members_in_age_range(start_age, end_age)
