
# collection of voter's data 

# from vote_casting import registered_voters
import random
import time

# Generating voter identification number 
def voter_id():
    voters_id = "NG"
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    for num in range(10):
        rand_num = random.choice(numbers)
        voters_id += rand_num
    return voters_id

vin = voter_id()

# collect phone number, restrict to 11-digits 
def get_phone_number():
    while True:
        voters_number = input("Enter your 11-digit phone number: ")
        if voters_number.isdigit() and len(voters_number) == 11:
            return int(voters_number)
        else:
            print('Invalid phone number. Please enter your 11-digit phone number.')

# collect sex for voter 
def sex_cat():
    while True:
        voter_sex = input("Enter voter sex (M/F): ").upper()
        """Restrict input to M or F """
        if voter_sex in ['M', 'F']:
            return voter_sex
        else:
            print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

# Create an empty list to store voter information
voters_list = []

# Database for storing voter information 
# import database connector 
import mysql.connector

voters_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arowosola1449", 
    database="voters_database",
    auth_plugin='mysql_native_password'
)

voters_cursor = voters_database.cursor()
voters_cursor.execute("CREATE TABLE IF NOT EXISTS OY_VOTERS_2023 (id INT AUTO_INCREMENT PRIMARY KEY, first_name VARCHAR(30), second_name VARCHAR(30), last_name VARCHAR(30), sex VARCHAR(1), birth_day VARCHAR(2), birth_month VARCHAR(2), birth_year INT, age INT, phone_number BIGINT, email VARCHAR(65), state_of_origin VARCHAR(15), origin_local_govt VARCHAR(30), street VARCHAR(60), nearest_busstop VARCHAR(20), city VARCHAR(20), residence_local_govt VARCHAR(45), state_of_residence VARCHAR(20), residence_ward VARCHAR(20), vin VARCHAR(20))")

# function collecting voter's data 
def voters_info():
    print("Submit Personal information\n")
    # global first_name
    first_name = input("First name: ").capitalize()
    second_name = input("Second name: ").capitalize()
    last_name = input("Last name: ").capitalize()
    
    voter_gender = sex_cat()
    
    birth_day = input("Day of birth: ")
    birth_month = input("Month of birth: ")
    birth_year = int(input("Year: "))
    
    voter_age = 2023 - birth_year
    
    phone_number = get_phone_number()
    
    voter_email = input("Supply correct email: ")
    
    state_of_origin = input("State of Origin: ").title().strip()
    origin_local_govt = input("Local government - state of origin: \n").title()
    
    print("Address")
    street = input("House number and street name: ").capitalize()
    nearest_busstop = input("Nearest Bus-stop: ").capitalize()
    city = input("City or Town: ").capitalize()
    
    state_of_residence = input("State of residence: ").title().strip()
    residence_local_govt = input("Residence Local government area: ").capitalize()
    residence_ward = input("Registrar should assist in selecting ward (e.g. ward-01): ")
    
    voters_info_dict = {
        "first_name": first_name,
        "second_name": second_name,
        "last_name": last_name,
        "voter_gender": voter_gender,
        "phone_number": phone_number,
        "residence_local_govt": residence_local_govt, 
        "residence_ward": residence_ward,
        "vin": vin,
        "voter_email": voter_email
    }
    
    # Append the dictionary to the list
    voters_list.append(voters_info_dict)
    
    print(f"{first_name}, your data has been saved successfully.")
    print(f"Please wait for some seconds, as we generate your unique Voters Identification Number....... ")
    
    time.sleep(10)
    
    print(f"VIN ({vin})")
    
    voter_input = ("INSERT INTO OY_VOTERS_2023(first_name,second_name,last_name,sex,birth_day,birth_month,birth_year,age,phone_number,email,state_of_origin,origin_local_govt,street,nearest_busstop,city,residence_local_govt,state_of_residence,residence_ward,vin) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    
    inputs = (first_name,second_name,last_name,voter_gender,birth_day,birth_month,birth_year,voter_age,phone_number,voter_email,state_of_origin,origin_local_govt,street,nearest_busstop,city,residence_local_govt,state_of_residence,residence_ward,vin) 
    
    voters_cursor.execute(voter_input,inputs)
    voters_database.commit()

# voters_info()