
# import module - contains uunique voter id and voters_info 
from lv2_project.voter_registration import *

# import database connector 
import mysql.connector

# change the name of database 
voters_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arowosola1449",  # Replace with your MySQL password
    database="NG_voters_database",
    auth_plugin='mysql_native_password'
)

voters_cursor = voters_database.cursor()
# voters_cursor.execute("CREATE TABLE IF NOT EXISTS OY_VOTERS_2023 (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), second_name VARCHAR(30), last_name VARCHAR(30), sex VARCHAR(1), birth_day VARCHAR(2), birth_month VARCHAR(2), birth_year INT, age INT, phone_number BIGINT, email VARCHAR(65), state_of_origin VARCHAR(15), origin_local_govt VARCHAR(30), street VARCHAR(60), nearest_busstop VARCHAR(20), city VARCHAR(20), residence_local_govt VARCHAR(45), state_of_residence VARCHAR(20), residence_ward VARCHAR(20), vin VARCHAR(20))")


def edo_state():
    choice_localgovt = input("""Select your Local Government Area:
                                01. IB-North
                                02. IB-South
                                03. IB-North-west
                                04. Atisbo \n
                'ENTER NUMBER - 01/02/03.....> '                                 
                                 """).strip()
    if choice_localgovt == "01":
        choice_ward = input("""Select ward - 
                            Ward-01 (Mokola/Oremeji)
                            Ward-02 
                            Ward-03
                            Ward-04
                            Ward-05
                'ENTER your ward (e.g. ward-01)' 
                """)
        
    elif choice_localgovt == '02':
        choice_ward = input("""Select ward - 
                            Ward-01
                            Ward-02 
                            Ward-03
                            Ward-04
                            Ward-05
                'ENTER your ward (e.g. ward-01)' 
                """)
    voters_info()
    