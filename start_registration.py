
# Start Program
# Registration of voters and voting!

import time
from voter_registration import voters_info
voting_period = True

print("""Welcome To voters registration.
          To register, enter "Y". """)
while voting_period:
    response = input(">>>> ").upper()
    if response == "Y":
        time.sleep(2)
        """Select voter state based on residence or state of voting"""
        print( """ SELECT STATE: 
                        1. Abia
                        2. Boxer
                        3. Ororo
                        """)
        try:
            state_choice = int(input(">>> "))
        except:
            print("Only takes intergers, 1/2/3..........")
        if state_choice == 1:
            print("loading..........")
        elif state_choice == 2:
            print("loading..........")
        elif state_choice == 3:                       
            # Call the function for voters registration and data submission         
            voters_info()
            print("Note: You'll be notified on the election due DATE via text message and email.")
    
    elif response == "N":
        time.sleep(5)
        print("Thank you")
        break
    else:
        print("Invalid Response...")