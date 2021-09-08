import pyttsx3
speaker = pyttsx3.init()
import sqlite3
from colorama import Fore , Back , Style
import matplotlib.pyplot as plt

conn = sqlite3.connect('ELECTION.db')

c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Student_Panel (username text,password text)''')
c.execute("""CREATE TABLE IF NOT EXISTS Admin_Panel (username text,password text)""")
conn.commit()


def student_login():
    while True:
        # global check_password1
        # global u_name1
        u_name1 = input("Enter Username : ")
        uname1 = (u_name1,)
        try:
            c = conn.cursor()
            c.execute("SELECT password FROM Student_Panel WHERE username = ? ", uname1)
            check_password1 = c.fetchone()[0]  # [()]
            conn.commit()
        except:

            print(Fore.RED + '')
            print(Back.BLACK + '')
            print(Style.BRIGHT + " \n                              There is no user found with this user name ,\n                          Please Signup Before You Login  \n")
            print(Style.RESET_ALL + " ")
            i = input("Do You To Continue y/n : ")
            if i == 'y':
                continue
            else:
                return None

        for i in range(5):
            password = input("Enter Password : ")
            if check_password1 != password and i == 4:
                print(Fore.RED + '')
                print(Back.BLACK + '')
                print(Style.BRIGHT + "                                  You Can't Vote Temporarily Please Contact The Admin\n ")
                print(Style.RESET_ALL + " ")
                return None

            elif check_password1 != password:
                print("Wrong password please enter valid password")
                _i = input("Do You To Continue y/n : ")
                if _i == 'y':
                    continue
                else:
                    return None
            else:
                print(Fore.GREEN + '')
                print(Back.BLACK + '')
                print(Style.BRIGHT + "                                 ########## Student Panel Login Successful ##########\n ")
                print(Style.RESET_ALL + " ")
                speaker.say("Student Panel Login Successful")
                speaker.runAndWait()
                break
        try:
            global check_
            c = conn.cursor()
            c.execute("SELECT * from Candidate")
            list_of_candi = c.fetchall()
            conn.commit()
            check_ = 2
        except:
            print(Fore.RED+ '')
            print(Back.BLACK + '')
            print(Style.BRIGHT + "                                 Currently There Is No Election\n ")
            print(Style.RESET_ALL + " ")
            speaker.say("Currently There is No Election")
            speaker.runAndWait()
            check_ = 0
            return None

        if check_ == 2:
            print("----------------------------------------------------------------------------------------------")
            _list = ["Candidate_No", "Candidate_name", "Department", "Year_Of_Study"]
            print('|    Candidate_No     |    Candidate_name          |    Department    |    Year_Of_Study     |')
            print("----------------------------------------------------------------------------------------------")

            for i in list_of_candi:
                print("|   ", i[0], " "(3+len(_list[0])-1), "|   ", i[1], " "(8+len(_list[1])-len(i[1])), "|   ", i[2], " "(2+len(_list[2])-len(i[2])), "|   ", i[3], " "(2+len(_list[3])-len(i[3])), " |")
                print("----------------------------------------------------------------------------------------------")
            while True:
                # global y_vote1
                print('\n')
                y_vote = input("Enter Your Vote : ")

                try:
                    if int(y_vote) <= len(list_of_candi) and (int(y_vote)) > 0:
                        y_vote1 = input("Confirm Vote : ")
                        if y_vote == y_vote1:
                            print(Fore.GREEN + '')
                            print(Back.BLACK + '')
                            print(Style.BRIGHT + "                                     Processing Your Vote\n")
                            print(Style.RESET_ALL + " ")
                            speaker.say("Processing your vote")
                            speaker.runAndWait()

                            break
                        elif int(y_vote1) <= len(list_of_candi) and y_vote != y_vote1:
                            print(Fore.RED + '')
                            print(Back.BLACK + '')
                            print(Style.BRIGHT + "                            Both password don't match each other please type again \n")
                            print(Style.RESET_ALL + " ")
                            continue
                        else:
                            print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
                            print("@@@@@@@@@@ Please Enter Valid Option @@@@@@@@@@ \n")
                            continue
                    else:
                        print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
                        print("@@@@@@@@@@ Please Enter Valid Option @@@@@@@@@@ \n")
                        i_ = input("Do You To Want Continue y/n : ")
                        if i_ == 'y':
                            continue
                        else:
                            return None

                except:
                    print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ \n")
                    i1 = input("Do You To Want Continue y/n : ")
                    if i1 == 'y':
                        continue
                    else:
                        return None
        break
    try:
        global illegal_vote
        c.execute("SELECT password FROM pseudo_Student_Panel where username = ? AND password = ?", (u_name1, password))
        illegal_vote = c.fetchone()[0]
        conn.commit()
        print(Fore.RED + '')
        print(Back.BLACK + '')
        print(Style.BRIGHT + "                              You Have Already Contributed Your Vote,\n                          Please Contact Admin For Further Details\n ")
        print(Style.RESET_ALL + " ")
        speaker.say("You Have Already Contributed Your Vote, Please Contact Admin For Further Details")
        speaker.runAndWait()

    except:
        c.execute("INSERT INTO pseudo_Student_Panel (username, password, vot) VALUES (?, ?, ?)", (u_name1, check_password1, y_vote1))
        conn.commit()
        print(Fore.GREEN + '')
        print(Back.BLACK + '')
        print(Style.BRIGHT + "                                    * Thank For Your Valuable Vote *\n  ")
        print(Style.RESET_ALL + " ")
        speaker.say(" Thank you for your valuable vote")
        speaker.runAndWait()


def student_signup():
    while True:
        u_name = input("Enter Username : ")
        if len(u_name) == 0:
            print("//////////Enter the Username again////////// ")
            i_ = input("Do You To Continue y/n : ")
            if i_ == 'y':
                continue
            else:
                return None
        else:
            while True:
                password1 = input("Enter Password : ")
                if len(password1) == 0:
                    print("//////////Enter the Password again////////// ")
                    i_0 = input("Do You To Continue y/n : ")
                    if i_0 == 'y':
                        continue
                    else:
                        return None
                else:
                    password2 = input("Confirm Password : ")
                    if password1 != password2:
                        print(Fore.RED + '')
                        print(Back.BLACK + '')
                        print(Style.BRIGHT + "                                     Both password don't match each other please type again\n ")
                        print(Style.RESET_ALL + " ")
                        speaker.say("both passwords  don't match each other please type again ")
                        speaker.runAndWait()
                        i = input("Do You To Continue y/n : ")
                        if i == 'y':
                            continue
                        else:
                            return None
                    else:
                        c.execute("INSERT INTO Student_Panel (username, password) VALUES (?, ?)", (u_name, password2))
                        conn.commit()
                        print(Fore.GREEN + '')
                        print(Back.BLACK + '')
                        print(Style.BRIGHT + "                                     ////////// Signed up Successfully ////////// \n ")
                        print(Style.RESET_ALL + " ")
                        speaker.say("Signed up Successfully")
                        speaker.runAndWait()
                        break
        break


def student():
    while True:
        print("\nStudent Panel\n")
        stu = input("1) Login \n2) Sign Up \n3) Exit \nEnter From The Option : ")
        if stu == '1':
            print("\n\nPlease Login Your With Your Credentials \n")
            student_login()
            return None
        elif stu == '2':
            print("\n\nPlease Enter Your Details And Signup \n")
            student_signup()
            return None
        elif stu == '3':
            return None
        else:
            print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
            print("@@@@@@@@@@ Please Enter Valid Option @@@@@@@@@@ \n")
            continue


def create_election():
    c.execute("drop table IF EXISTS Candidate")
    c.execute("drop table IF EXISTS pseudo_Student_Panel")
    c.execute('''CREATE TABLE IF NOT EXISTS Candidate ( Candi_no int, c_name text, department text, year_ text)''')

    c.execute('''CREATE TABLE IF NOT EXISTS pseudo_Student_Panel ( username text, password text, vot int)''')
    conn.commit()
    global name_of_poll, no_of_candidates
    global year_
    print("\n----------Creating A New Election----------\n")
    while True:
        print("\n")
        name_of_poll = input("Name Of The Election : ")
        if len(name_of_poll) < 3:
            print("\nMinimum of 3 Characters Required")
            i_0 = input("Do You To Continue y/n : ")
            if i_0 == 'y':
                continue
            else:
                c.execute("drop table IF EXISTS Candidate")
                c.execute("drop table IF EXISTS pseudo_Student_Panel")
                return None
        else:
            while True:
                year_ = input("\nEnter The Year : ")
                try:
                    if len(year_) > 0:
                        y = int(year_)
                except:
                    print("Year Should Be in Integer Format")
                    i_8 = input("Do You To Continue y/n : ")
                    if i_8 == 'y':
                        continue
                    else:
                        c.execute("drop table IF EXISTS Candidate")
                        c.execute("drop table IF EXISTS pseudo_Student_Panel")
                        return None
                if len(year_) == 4:
                    break
                else:
                    print("\nMinimum of 4 Characters Required")
                    i_1 = input("Do You To Continue y/n : ")
                    if i_1 == 'y':
                        continue
                    else:
                        c.execute("drop table IF EXISTS Candidate")
                        c.execute("drop table IF EXISTS pseudo_Student_Panel")
                        return None
        break
    print("\n")
    while True:
        no_ = input("Enter The Number Of Candidates : ")
        try:
            no_of_candidates = int(no_)
            if no_of_candidates >= 2:
                break
            elif no_of_candidates == 1:
                print("\nThere Should Be Minimum 2 Candidates")
                i_2 = input("Do You To Continue y/n : ")
                if i_2 == 'y':
                    continue
                else:
                    c.execute("drop table IF EXISTS Candidate")
                    c.execute("drop table IF EXISTS pseudo_Student_Panel")
                    return None
            elif no_of_candidates <= 0:
                print("\n**Invalid Entry**")
                i_3 = input("Do You To Continue y/n : ")
                if i_3 == 'y':
                    continue
                else:
                    c.execute("drop table IF EXISTS Candidate")
                    c.execute("drop table IF EXISTS pseudo_Student_Panel")
                    return None
        except:
            print("\n#####Invalid Input#####")
            i = input("Do You To Continue y/n : ")
            if i == 'y':
                continue
            else:
                c.execute("drop table IF EXISTS Candidate")
                c.execute("drop table IF EXISTS pseudo_Student_Panel")
                return None
        break

    for i in range(0, no_of_candidates):
        print("\nCandidate", i + 1, " Details")
        while True:
            name_c = input("\nName Of Candidate : ")
            if len(name_c) <= 0:
                print("Requires At least 1 Character")
                i_4 = input("Do You To Continue y/n : ")
                if i_4 == 'y':
                    continue
                else:
                    c.execute("drop table IF EXISTS Candidate")
                    c.execute("drop table IF EXISTS pseudo_Student_Panel")
                    return None
            else:
                while True:
                    departments_ = ['cse', 'mech', 'it', 'eee', 'ece', 'prod', 'ice', 'tex', 'auto', 'bmed', 'btec', 'civ', 'mety', 'rob','ftec', 'CSE', 'MECH', 'IT', 'EEE', 'ECE', 'PROD', 'ICE', 'TEX', 'AUTO', 'BMED', 'BTEC', 'CIV', 'METY', 'ROB', 'FTEC']
                    department_ = input("Enter The Dept : ")
                    if len(department_) < 2 or len(department_) > 4:
                        print("Requires At least 2 Character, At most 4 Character")
                        i_5 = input("Do You To Continue y/n : ")
                        if i_5 == 'y':
                            continue
                        else:
                            c.execute("drop table IF EXISTS Candidate")
                            c.execute("drop table IF EXISTS pseudo_Student_Panel")
                            return None
                    else:
                        if department_ not in departments_:
                            print("There is No Department Like This, Please Type Again")
                            i_7 = input("Do You To Continue y/n : ")
                            if i_7 == 'y':
                                continue
                            else:
                                c.execute("drop table IF EXISTS Candidate")
                                c.execute("drop table IF EXISTS pseudo_Student_Panel")
                                return None
                        while True:
                            year = input("Enter Year Of Study : ")
                            try:
                                if len(year) > 0:
                                    y_ = int(year)
                            except:
                                print("Year of Study Should Be in Integer Format")
                                i_9 = input("Do You To Continue y/n : ")
                                if i_9 == 'y':
                                    continue
                                else:
                                    c.execute("drop table IF EXISTS Candidate")
                                    c.execute("drop table IF EXISTS pseudo_Student_Panel")
                                    return None
                            if len(year) != 1:
                                print("Requires Only 1 Character")
                                i_6 = input("Do You To Continue y/n : ")
                                if i_6 == 'y':
                                    continue
                                else:
                                    c.execute("drop table IF EXISTS Candidate")
                                    c.execute("drop table IF EXISTS pseudo_Student_Panel")
                                    return None
                            else:
                                if 1 < int(year) > 5:
                                    print("The Year of Study Should Be Between 1 to 5")
                                    i_9 = input("Do You To Continue y/n : ")
                                    if i_9 == 'y':
                                        continue
                                    else:
                                        c.execute("drop table IF EXISTS Candidate")
                                        c.execute("drop table IF EXISTS pseudo_Student_Panel")
                                        print(Fore.RED + '')
                                        print(Back.BLACK + '')
                                        print(Style.BRIGHT + "                                   !!!!!!!!!! Election Not Created !!!!!!!!!!\n ")
                                        print(Style.RESET_ALL + " ")
                                        speaker.say(" Election Not Created ")
                                        speaker.runAndWait()
                                        return None
                                else:
                                    checking = '1'
                            break
                    break
            break
        if checking == '1':
            c.execute("INSERT INTO Candidate (Candi_no, c_name, department, year_) VALUES (?, ?, ?, ?)", (i + 1, name_c, department_, year))
            conn.commit()
    print(Fore.GREEN + '')
    print(Back.BLACK + '')
    print(Style.BRIGHT + "                                    !!!!!!!!!! New Election Created !!!!!!!!!!\n ")
    print(Style.RESET_ALL + " ")
    speaker.say(" New Election Created ")
    speaker.runAndWait()


def view_result():
    c.execute("drop table IF EXISTS Result")
    c.execute("CREATE TABLE IF NOT EXISTS Result (name_of_the_candidates text,no_of_votes_per_candidate in0t)")
    conn.commit()
    try:
        c.execute("SELECT * FROM Candidate")
        candidate_ = c.fetchall()
        c.execute("SELECT * FROM pseudo_Student_Panel")
        _votes = c.fetchall()
    except:
        print(Fore.RED + '')
        print(Back.BLACK + '')
        print(Style.BRIGHT + "                           !!!!!!!!!  You Have Not Created Any Election Before !!!!!!!!!! \n                           !!!!!!!!!! Previous Election May be Deleted !!!!!!!!!! \n ")
        print(Style.RESET_ALL + " ")
        speaker.say("   You Have Not Created Any Election Before     or    Previous Election May be Deleted")
        speaker.runAndWait()
        return None
    no_of_candidates = len(candidate_)
    no_of_votes = len(_votes)

    if no_of_votes <= 0:
        print(Fore.RED + '')
        print(Back.BLACK + '')
        print(Style.BRIGHT + "                            **** Till this point no one contributed ****\n ")
        print(Style.RESET_ALL + " ")
        speaker.say("  Till this point no one contributed   ")
        speaker.runAndWait()
        return None
    else:
        name_of_the_candidates = []
        no_of_votes_per_candidate = []
        print('\n----------------------------------------------------------')
        print("                        RESULTS                           ")
        print('----------------------------------------------------------')
        for i in range(1, no_of_candidates + 1):
            b = (i,)
            c.execute("SELECT username FROM pseudo_Student_Panel WHERE vot = ? ", b)
            m_ = c.fetchall()
            no_of_votes_per_candidate.append(len(m_))
            c.execute("SELECT c_name FROM Candidate WHERE Candi_no = ? ", b)
            n_ = c.fetchall()[0][0]
            name_of_the_candidates.append(n_)
            print("No of Votes For", n_, ":", len(m_), "                             ")
            print('----------------------------------------------------------')
            c.execute("INSERT INTO Result (name_of_the_candidates, no_of_votes_per_candidate) VALUES (?, ?)", (n_, len(m_)))
            conn.commit()
        # results = dict(zip(no_of_votes_per_candidate, name_of_the_candidates))

        plt.bar(name_of_the_candidates, no_of_votes_per_candidate, width=0.4, color="red")
        plt.xlabel("Candidates")
        plt.ylabel("No Of Votes")
        plt.title("Election Results")
        plt.show()

        result = max(no_of_votes_per_candidate)
        result_ = (str(result),)
        c.execute("SELECT name_of_the_candidates FROM Result WHERE no_of_votes_per_candidate = ?", result_)
        display_result= c.fetchall()
        conn.commit()
        if len(display_result) == 1:
            print("\n")
            #print('---------------------------------------------------------------------------')
            #print("                        THE WINNER IS :", display_result[0][0])
            #print('---------------------------------------------------------------------------')
            print(Fore.CYAN + '')
            print(Back.BLACK + '')
            print(Style.BRIGHT + "                                    THE WINNER IS :", display_result[0][0] ,"\n")
            print(Style.RESET_ALL + " ")
            print("\n")

            speaker.say("The winner is "+display_result[0][0])
            speaker.runAndWait()

        else:
            print("\n")
            #print('------------------------------------------------------------------------------------------------------------------------')
            #print("                        THE ELECTION RESULTS TIE BETWEEN :", display_result[0][0], "AND", display_result[1][0])
            #print('------------------------------------------------------------------------------------------------------------------------')
            print(Fore.CYAN + '')
            print(Back.BLACK + '')
            print(Style.BRIGHT + "                               THE ELECTION RESULTS TIE BETWEEN :", display_result[0][0], "AND", display_result[1][0], "\n")
            print(Style.RESET_ALL + " ")
            print("\n")
            speaker.say("The election ties between " + display_result[0][0]+" and " +display_result[1][0])
            speaker.runAndWait()

def continue_elect():
    try:
        c.execute("SELECT * FROM pseudo_Student_Panel")
        password_ = c.fetchall()
        conn.commit()
        check = 1
    except:
        print(Fore.RED + '')
        print(Back.BLACK + '')
        print(Style.BRIGHT + "                              !!!!!!!!!  You Have Not Created Any Election Before !!!!!!!!!! \n                                 !!!!!!!!!! Previous Election May be Deleted !!!!!!!!!! \n ")
        print(Style.RESET_ALL + " ")
        speaker.say("   You Have Not Created Any Election Before     or    Previous Election May be Deleted")
        speaker.runAndWait()
        check = 0
        return None
    if check == 1:
        print("\nNo Of People Contributed Up to This time : ", len(password_))
        while True:
            delete_ = input('\n1) Delete Previous Election \n2) Continue Election \n\nEnter From The Option : ')
            if delete_ == '1':
                c.execute("drop table IF EXISTS Candidate")
                c.execute("drop table IF EXISTS pseudo_Student_Panel")
                print(Fore.RED + '')
                print(Back.BLACK + '')
                print(Style.BRIGHT + "                                    ----------Deleted Previous Election----------\n")
                print(Style.RESET_ALL + " ")
                speaker.say("Deleted Previous Election")
                speaker.runAndWait()
                return None
            elif delete_ == '2':
                return None
            else:
                print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
                print("**Please Enter Valid Option** \n")
            continue
    return None


def admin_login():
    while True:
        u_name2 = input("Enter Username : ")
        uname = (u_name2,)
        try:
            c = conn.cursor()
            c.execute("SELECT password FROM Admin_Panel WHERE username = ? ", uname)
            check_password = c.fetchone()[0]  # initialise username and password from sqlite
            conn.commit()
        except:
            print(Fore.RED + '')
            print(Back.BLACK + '')
            print(Style.BRIGHT + "                                    There is no user with this username, Please Signup Before You Login\n")
            print(Style.RESET_ALL + " ")
            speaker.say(" There is no user with this username, Please Signup Before You Login")
            speaker.runAndWait()
            i = input("Do You To Continue y/n : ")
            if i == 'y':
                continue
            else:
                return None

        while True:
            password = input("Enter Password : ")
            if check_password != password:
                print(Fore.RED + '')
                print(Back.BLACK + '')
                print(Style.BRIGHT + "                                    Wrong password please enter valid password \n")
                print(Style.RESET_ALL + " ")
                i = input("Do You To Continue y/n : ")
                if i == 'y':
                    continue
                else:
                    return None
            else:
                print(Fore.GREEN + '')
                print(Back.BLACK + '')
                print(Style.BRIGHT + "                                     ########## Admin Panel Login Successful ##########\n")
                print(Style.RESET_ALL + " ")
                speaker.say("Admin Panel Login Successful")
                speaker.runAndWait()
                while True:
                    choice = input(
                        "1) New Election \n2) Continue Election \n3) View Result \n4) Logout \n\nSelect From Above Options : ")
                    if choice == '1':
                        create_election()
                        break

                    elif choice == '2':
                        continue_elect()
                        break

                    elif choice == '3':
                        view_result()
                        break

                    elif choice == '4':
                        return None
                    else:
                        print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
                        print("**Please Enter Valid Option** \n")
                        i = input("Do You To Continue y/n : ")
                        if i == 'y':
                            continue
                        else:
                            return None
                break
        break
    return None


def admin_signup():
    while True:
        u_name = input("Enter Username : ")
        if len(u_name) == 0:
            print("//////////Enter the Username again////////// ")
            i_ = input("Do You To Continue y/n : ")
            if i_ == 'y':
                continue
            else:
                return None
        else:
            while True:
                password1 = input("Enter Password : ")
                if len(password1) == 0:
                    print("//////////Enter the Password again////////// ")
                    i_0 = input("Do You To Continue y/n : ")
                    if i_0 == 'y':
                        continue
                    else:
                        return None
                else:
                    password2 = input("Confirm Password : ")
                    if password1 != password2:
                        print(Fore.RED + '')
                        print(Back.BLACK + '')
                        print(Style.BRIGHT + "                                     Both password don't match each other please type again \n ")
                        print(Style.RESET_ALL + " ")
                        speaker.say("both passwords  don't match each other please type again ")
                        speaker.runAndWait()
                        i = input("Do You To Continue y/n : ")
                        if i == 'y':
                            continue
                        else:
                            return None
                    else:
                        c.execute("INSERT INTO Admin_Panel (username, password) VALUES (?, ?)", (u_name, password2))
                        conn.commit()
                        print(Fore.GREEN + '')
                        print(Back.BLACK + '')
                        print(Style.BRIGHT + "                                    ////////// Signed up Successfully //////////\n ")
                        print(Style.RESET_ALL + " ")
                        speaker.say("Signed up Successfully")
                        speaker.runAndWait()
                        break
        break


def admin():
    while True:
        print("\nAdmin Panel\n")
        adm = input("1) Login \n2) Sign Up \n3) Exit \nEnter From The Option : ")
        if adm == '1':
            print("\n\nPlease Login Your With Your Credentials \n")
            admin_login()
            break
        elif adm == '2':
            print("\n\nPlease Enter Your Details And Signup \n")
            admin_signup()
            break
        elif adm == '3':
            return None
        else:
            print("\n$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
            print("**Please Enter Valid Option** \n")
            continue


while True:
    print(Fore.CYAN + '')
    print(Back.BLACK + '')
    print(Style.BRIGHT + "  \n                                               THE VOTING SYSTEM  \n\n ")
    print(Style.RESET_ALL + " ")
    print("""1) Student Panel 
2) Admin 
3) Exit""")
    select_panel = input("\nSelect your panel : ")
    if select_panel == '1':
        student()
    elif select_panel == '2':
        admin()
    elif select_panel == '3':
        break
    else:
        print("$$$$$$$$$$ Invalid Option $$$$$$$$$$ ")
        print("\n**Please Enter Valid Option** ")

conn.close()
