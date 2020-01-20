def main2():
    print ("""
    WHAT DO YOU WANT DO?
    (1) OPEN MEDICAL RECORD
    (2) CREATE MEDICAL RECORD
    (3) EDIT MEDICAL RECORD
    (4) PRINT MEDICAL RECORD
    (5) DELETE MEDICAL RECORD
    (6) EXIT
    """)

    command = input("ENTER: ")

    if command == "1":
        patient_name = input("PATIENT NAME (UNDERSCORE = SPACE): ")

        patient_info = open(patient_name + "_MEDICAL_RECORDS.txt", "r")
        print(patient_info.read())

        patient_info.close()

        main2()

    elif command == "2":
        def main():
           try:

               patient_name = (input("PATIENT NAME(UNDERSCORE = SPACE): "))
               patient_phone = (input("PHONE NUMBER: "))
               patient_email = (input("EMAIL: "))
               surgical_history = (input("SURGICAL HISTORY: "))
               obstetric_history = (input("OBSTETRIC HISTORY: "))
               medications = (input("MEDICATIONS: "))
               medical_allergies = (input("MEDICAL ALLERGIES: "))
               family_history = (input("FAMILY HISTORY: "))
               social_history = (input("SOCIAL HISTORY: "))
               habits = (input("HABITS: "))
               immunization_history = (input("IMMUNIZATION HISTORY: "))
               chief_complaint = (input("CHIEF COMPLAINT: "))
               history_of_present_illnesses = (input("HISTORY OF PRESENT ILLNESSES: "))
               physical_examination = (input("PHYSICAL EXAMINATION: "))
               assessment_and_plan = (input("ASSESSMENT & PLAN: "))

               patient_upload = (input("Do you want to upload patient information?(YES/NO): "))

               if patient_upload == "YES":

                   patient_info = open(patient_name + "_MEDICAL_RECORDS.txt", "w")

                   patient_info.write("PATIENT MEDICAL RECORDS")
                   patient_info.write("\n")
                   patient_info.write("\nMEDICAL HISTORY")
                   patient_info.write("\n")
                   patient_info.write("\nPATIENT NAME: " + patient_name)
                   patient_info.write("\nPHONE NUMBER: " + patient_phone)
                   patient_info.write("\nEMAIL: " + patient_email)
                   patient_info.write("\nSURGICAL HISTORY: " + surgical_history)
                   patient_info.write("\nOBSTETRIC HISTORY: " + obstetric_history)
                   patient_info.write("\nMEDICATIONS: " + medications)
                   patient_info.write("\nMEDICAL ALLERGIES: " + medical_allergies)
                   patient_info.write("\nFAMILY HISTORY: " + family_history)
                   patient_info.write("\nSOCIAL HISTORY: " + social_history)
                   patient_info.write("\nHABITS: " + habits)
                   patient_info.write("\nIMMUNIZATION HISTORY: " + immunization_history)
                   patient_info.write("\n")
                   patient_info.write("\n")
                   patient_info.write("\nMEDICAL ENCOUNTERS")
                   patient_info.write("\n")
                   patient_info.write("\nCHIEF COMPLAINT: " + chief_complaint)
                   patient_info.write("\nHISTORY OF PRESENT ILLNESSES: " + history_of_present_illnesses)
                   patient_info.write("\nPHYSICAL EXAMINATION: " + physical_examination)
                   patient_info.write("\nASSESSMENT & PLAN: " + assessment_and_plan)


                   patient_info.close()

               print("""WHAT DO YOU WANT TO DO?
               (1) EXIT
               (2) RETURN TO HOME""")

               restart = (input("ENTER (1,2): "))

               if restart == "2":
                   main2()
               else:
                   exit()

           except ValueError:
                   print("ERROR: INVALID INPUT")

        main()

    elif command == "4":

        print("""WHICH FILE DO YOU WANT TO PRINT?""")

        file = input("ENTER PATIENT NAME (UNDERSCORE = SPACE): ")
        print("DO YOU WANT TO PRINT " + file + "_MEDICAL_RECORDS.txt?")
        print_function = input("ENTER(YES/NO): ")

        if print_function == "YES":

            import os

            os.system("lpr -P FUJI_XEROX_DocuPrint_M215_b " + file + "_MEDICAL_RECORDS.txt")

            main2()

        else:
            main2()

    elif command == "5":
        print("WHICH FILE DO YOU WANT TO DELETE?")
        file = input("ENTER PATIENT NAME (UNDERSCORE = SPACE): ")

        delete = input("DO YOU WANT TO DELETE " + file + "_MEDICAL_RECORDS.txt?(YES/NO)")

        if delete == "YES":
            import os

            if os.path.exists(file + "_MEDICAL_RECORDS.txt"):
              os.remove(file + "_MEDICAL_RECORDS.txt")
              main2()

            else:
                print("""
                The file does not exist""")
                main2()

    elif command == "6":
        exit()

    else:
        print("INVALID INPUT")
        main2()

main2()


