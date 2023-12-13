
# import module - contains uunique voter id and voters_info 
from lv2_project.voter_registration import *

def oyo_state():
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
    