import socket
import re
import datetime


#start
cs = socket.socket()
cs.connect((socket.gethostname(), 5000))

#Validation date format
def validate_date(text):
    try:
        datetime.datetime.strptime(text, '%Y-%m-%d')
    except ValueError:
        print("Incorrect data format, should be YYYY-MM-DD")
        return False
    return True


#user interface
#search match by team name or date or both
def user():
    inputstring1 = input("(ST)search team,(SD)search date,(STD)search team and date,(q)uit: ")
    if inputstring1 == "ST":
        team = input("Team:")
        cs.send(str(("ST", team)).encode())
        dt = cs.recv(1024).decode()
        if dt != "No match found":
                dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
                dt = dt.split(",")
                i = len(dt)
                i = i//7
                n = 0
                while n < i:
                    try :
                        int(dt[3+n*7])
                        print("{} {}{}{}{}:{}{}Ended".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    except ValueError:
                        print("{} {}{}{}{}:{}{}Not started".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    n = n + 1
                user()
        else:
            print("No match found")
            user()
    elif inputstring1 == "SD":
        date = input("Date:")
        if validate_date(date):
            cs.send(str(("SD", date)).encode())
            dt = cs.recv(1024).decode()
            if dt != "No match found":
                dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
                dt = dt.split(",")
                i = len(dt)
                i = i//7
                n = 0
                while n < i:
                    try :
                        int(dt[3+n*7])
                        print("{} {}{}{}{}:{}{}Ended".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    except ValueError:
                        print("{} {}{}{}{}:{}{}Not started".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    n = n + 1
                user()
            else:
                print("No match found")
                user()
        else:
            user()
    elif inputstring1 == "STD":
        team = input("Team:")
        date = input("Date:")
        if validate_date(date):
            cs.send(str(("STD", team, date)).encode())
            if dt[3] == "-":
                    print("{} {}{}{}{}:{}{}Ended".format(dt[0], dt[5], dt[6], dt[1], dt[3], dt[4], dt[2]))
            else:
                print("{} {}{}{}{}:{}{}Not started".format(dt[0], dt[5], dt[6], dt[1], dt[3], dt[4], dt[2]))
                admin()
            user()
        else:
            user()
    elif inputstring1 == "q":
        clienter()

#admin interface
#search team and date
#add match, delete match, update match
def admin():
    inputstring2 = input("(ST)search team,(SD)search date,(AM)add match,(DM)delete match,(UM)update match,(q)uit: ")
    if inputstring2 == "ST":
        team1 = input("Team1:")
        team2 = input("Team2:")
        cs.send(str(("ST", team1, team2)).encode())
        dt = cs.recv(1024).decode()
        if dt != "No match found":
                dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
                dt = dt.split(",")
                i = len(dt)
                i = i//7
                n = 0
                while n < i:
                    try :
                        int(dt[3+n*7])
                        print("{}{}{}{}:{}{}Ended".format(dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    except ValueError:
                        print("{}{}{}{}:{}{}Not started".format(dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    n = n + 1
                admin()
        else:
            print("No match found")
            admin()
    elif inputstring2 == "SD":
        date = input("Date:")
        if validate_date(date):
            cs.send(str(("SD", date)).encode())
            dt = cs.recv(1024).decode()
            if dt != "No match found":
                dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
                #^:除了 0-9 A-Z a-z - 之外的字符
                dt = dt.split(",")
                #print(dt,len(dt))
                #match > 1
                i = len(dt)
                i = i//7
                n = 0
                while n < i:
                    #print(n,dt[3+n*7])
                    #忘记对n*7
                    try :
                        int(dt[3+n*7])
                        print("{}{}{}{}:{}{}Ended".format(dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    except ValueError:
                        print("{}{}{}{}:{}{}Not started".format(dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                    n = n + 1
                        #遇到错误：TypeError: list indices must be integers or slices, not float
                        #意思是：list的索引必须是’integers’  or slices,
                        #要点：" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
                admin()
            else:
                print("No match found")
                admin()
        else:
            admin()
    elif inputstring2 == "AM":
        #flag提交错误：将AM的flag提交到DM中
        #导致相当长一段时间存在IndexError: tuple index out of range
        team1 = input("Team1:")
        team2 = input("Team2:")
        score1 = input("Score1(input '-' if not ended):")
        score2 = input("Score2(input '-' if not ended):")
        date = input("Date:")
        times = input("Time:")
        if validate_date(date):
            cs.send(str(("AM", team1, team2, score1, score2, date, times)).encode())
            print(cs.recv(1024).decode())
            admin()
        else:
            admin()
    elif inputstring2 == "DM":
        match_id = input("Match_id:")
        cs.send(str(("DM", match_id)).encode())
        admin()
    elif inputstring2 == "UM":
        match_id = input("Match_id:")
        team1 = input("Team1:")
        team2 = input("Team2:")
        score1 = input("Score1(input '-' if not ended):")
        score2 = input("Score2(input '-' if not ended):")
        date = input("Date:")
        times = input("Time:")
        if validate_date(date):
            cs.send(str(("UM", team1, team2, score1, score2, date, times, match_id)).encode())
            print(cs.recv(1024).decode())
            admin()
        else:
            admin()

#main program
def clienter():
    inputstring = input("(U)sers,(A)dministrators,(R)egister,(q)uit: ")
    if inputstring == "U":
        Name = input("Name:")
        Password = input("Password:")
        cs.send(str(("U", Name,Password)).encode())
        if cs.recv(1024).decode() == "True":
            print("Welcome {}".format(Name))
            user()
        elif cs.recv(1024).decode() == "None":
            print("User does not exist")
            clienter()
        else:
            print("Incorrect username or password")
            clienter()
    elif inputstring == "A":
        Name = input("Name:")
        Password = input("Password:")
        cs.send(str(("A", Name, Password)).encode())
        if cs.recv(1024).decode() == "True":
            print("Welcome {}".format(Name))
            admin()
        else:
            print("Incorrect username or password")
            clienter()
    elif inputstring == "R":
        is2 = input("Register for (U)sers or (A)dministrators: ")
        Name = input("Name:")
        Password = input("Password:")
        CPassword = input("Confirm the password:")
        if Password == CPassword:
            if is2 == "U":
                cs.send(str(("RU", Name, Password)).encode())
                if cs.recv(1024).decode() == "True":
                    print("You have been registered")
                clienter()
            elif is2 == "A":
                cs.send(str(("RA", Name, Password)).encode())
                if cs.recv(1024).decode() == "True":
                    print("You have been registered")
                clienter()
        else:
            print("Passwords do not match")
            clienter()
    elif inputstring == "q":
        return
    elif inputstring == 'u' or 'a' or 'r' or 'Q':
        print("Please enter a valid input")
        clienter()
    else:
        print("Please enter a correct input")
        clienter()


clienter()