
# candidate registration 

import random
import time

welcome = """ Welcome to ARC voting system - 
                Strictly follow the instructions spelled out below before proceeding to fill in the candidate form.
            """
# - Have an instruction document

def get_phone_number():
    while True:
        voters_number = input("Enter your 11-digit phone number: ")
        if voters_number.isdigit() and len(voters_number) == 11:
            return int(voters_number)
        else:
            print('Invalid phone number. Please enter your 11-digit phone number.')

def sex_cat():
    while True:
        voter_sex = input("Enter voter sex (M/F): ").upper()
        if voter_sex in ['M', 'F']:
            return voter_sex
        else:
            print("Invalid input. Please enter 'M' for Male or 'F' for Female.")

# Create an empty list to store voter information
candidate_list = []

election_view = {}

# candidates table
# import database connector 
import mysql.connector

voters_database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="arowosola1449", 
    database="voters_database",
    auth_plugin='mysql_native_password'
)

# voters_cursor = voters_database.cursor()
# voters_cursor.execute("CREATE TABLE IF NOT EXIST CANDIDATES ()")


# Candidate registration 
def candidate_info():
    print("Submit Personal information\n")
    first_name = input("First name: ")
    second_name = input("Second name: ")
    last_name = input("Last name: ")
    
    global full_name
    full_name = first_name + " " + second_name + " " + last_name
    
    # voter_gender = sex_cat()
    
    # birth_day = input("Day of birth: ")
    # birth_month = input("Month of birth: ")
    # birth_year = int(input("Year: "))
    
    # phone_number = get_phone_number()
    
    # voter_email = input("Supply correct email: ")
    
    # state_of_origin = input("State of Origin: ").title().strip()
    # origin_local_govt = input("Local government - state of origin: \n").title()
    
    # print("Address")
    # street = input("House number and street name: ")
    # nearest_busstop = input("Nearest Bus-stop: ")
    # city = input("City or Town: ")
    
    # state_of_residence = input("State of residence: ").title().strip()
    # residence_local_govt = input("Residence Local government area: ")
    # residence_ward = input("Registrar should assist in selecting ward (e.g. ward-01): ")
    
    # office_vying = input("Fill-in the office you are contesting for: ")
    # print("Confirm in our memo if your party is registered - if not, you shall be disqualified! ")

    global party_name
    party_name = input("Party name: ")
    
    # print(f"{first_name.upper()} {second_name.upper()} {last_name.upper()}, from {residence_local_govt}, {state_of_residence.title()} is contesting for the office of {office_vying} under the party name - {party_name}. ")
    
    candidate_info_dict = {
        "first_name": first_name,
        "second_name": second_name,
        "last_name": last_name,
        # "voter_gender": voter_gender,
        # "phone_number": phone_number,
        # "residence_local_govt": residence_local_govt, 
        # "residence_ward": residence_ward,
        # "voter_email": voter_email,
        # "office":office_vying,
        "party_name":party_name
    }
    
    # upload up the candidate details in back end and add undecided:undecided
    election_view[party_name] = full_name
    
    # Append the dictionary to the list
    candidate_list.append(candidate_info_dict)
    
    
# candidate_info()
# print(election_view)