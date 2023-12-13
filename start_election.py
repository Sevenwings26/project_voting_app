
import time  

# Upload Candidate name and party 

""" Update by election officers """
candidate_dict = {
    "Governorship":{
        "ADC":"Ajala Mololuwa Collins",
        "PSD":"Ojulari Samsom Chibuzor"
    }
}

from clear_screen import clear_screen

from voter_verification import *

# save voting in list 
save_votes = []

# vote by inputing party name 
def vote_cating():
    choice = input("Enter party name: ").upper()
    if choice in save_votes:
        print("You cannot vote more than ONCE. ")
    else:
        save_votes.append(choice)
    # pass clear screen function
    time.sleep(3)
    
    clear_screen()
     
def office():     
    print("ororo stae governorship election".upper())
    print("\nCandidate for gubernitorial office".title())
    for party, candidate in candidate_dict.items():
        print(f"{party} : {candidate}\n")


while True:    
    # To proceed to voting 
    choice = input("Enter 'Y' to vote or N, \n Done with election? Enter 'COUNT'. \n >>>>>>>>>>>>>>>>>>>>>>>>>> ").lower()
    if choice == "y":
    # Verify voters
        # verify_voter(verification_id)
        verification_id = input("Enter your voter ID for verification: ")
        verify_voter(verification_id)
        office()
        vote_cating()
        
        
    elif choice == "n":
        None
    else:
    # elif input == "count":
        time.sleep(15)
        r = "election result".upper()
        print(r)
        result_ADC = save_votes.count("ADC")
        print(f"Number of votes for ADC {result_ADC}")
        result_PSD = save_votes.count("PSD")
        print(f"\nNumber of votes for PSD {result_PSD}")
        break
    
    