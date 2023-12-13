# # 4. **Voting:**
# #    - `cast_vote(voter_id, firstname)`: Allows a registered voter to cast a vote for a specific candidate.

"""Verify voter - 
                Ask voter for VIN then check if VIN is in database by fetching data from database.
""" 
import mysql.connector

def verify_voter(voter_id):
    try:
        # Establish a connection to the MySQL server
        voters_database = mysql.connector.connect(
            host="localhost",
            user="root",
            password="arowosola1449", 
            database="voters_database",
            auth_plugin='mysql_native_password'
        )
        
        if voters_database.is_connected():
            # Define the SELECT query
            query = f"SELECT * FROM OY_VOTERS_2023 WHERE vin = '{voter_id}'"

            # Create a cursor object to execute the query
            voters_cursor = voters_database.cursor(dictionary=True)  # This returns the results as dictionaries

            # Execute the query
            voters_cursor.execute(query)

            # Fetch the result
            voter_data = voters_cursor.fetchone()

            if voter_data:
                # Voter found, you can proceed with the voting process or any other action
                # print("Voter ID Verified. Voter Data:", voter_data)
                print("Voter ID Verified")
                
            else:
                print("Voter ID not found. Please check your ID and try again.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        if voters_database.is_connected():
            voters_cursor.close()
            voters_database.close()

   
    


