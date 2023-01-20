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
        return False
    return True

#user interface
#user search match by teams
#input team1 and team2
def user_ST(team1, team2):
    admin_ST(team1, team2)

#user search match by date
#input date
def user_SD(date):
    admin_SD(date)

def user_STD(team1, team2, date):
    admin_STD(team1, team2, date)

#user search match by teams and date
#input team1 and team2 and date
def admin_STD(team1, team2, date):
    if validate_date(date):
        cs.send(str(("STD", team1, team2, date)).encode())
        dt = cs.recv(1024).decode()
        if dt != None:
            dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
            dt = dt.split(",")
            if dt[3] == "-":
                return "{} {}{}{}{}:{}{}Ended".format(dt[0], dt[5], dt[6], dt[1], dt[3], dt[4], dt[2])
            else:
                return "{} {}{}{}{}:{}{}Not started".format(dt[0], dt[5], dt[6], dt[1], dt[3], dt[4], dt[2])
        else:
            None

#admin interface
#def admin_S(team1,team2,date):
#    if team1 == "" and team2 == "" and date != "":
#        admin_SD(date)
#    elif team1 != "" and team2 != "" and date == "":
#        admin_ST(team1, team2)
#    elif team1 != "" and team2 != "" and date != "":
#        admin_STD(team1, team2, date)

#admin search match by teams
#input team1 and team2
def admin_ST(team1, team2):
    cs.send(str(("ST", team1, team2)).encode())
    dt = cs.recv(1024).decode()
    if dt != None:
        dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
        dt = dt.split(",")
        i = len(dt)
        i = i//7
        n = 0
        lst = []
        while n < i:
            try :
                #print(n,dt[3+n*7])
                #忘记对n*7
                int(dt[3+n*7])
                lst.append("{} {}{}{}{}:{}{}Ended".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
            except ValueError:
                lst.append("{} {}{}{}{}:{}{}Not started".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
            n = n + 1
        return lst
    else:
        return None

#admin search match by date
#input date
def admin_SD(date):
    if validate_date(date):
        cs.send(str(("SD", date)).encode())
        dt = cs.recv(1024).decode()
        if dt != None:
            dt = re.sub(r'[^0-9A-Za-z-:,]+', ' ', dt)
            #^:除了 0-9 A-Z a-z - 之外的字符
            dt = dt.split(",")
            #print(dt,len(dt))
            #match > 1
            i = len(dt)
            i = i//7
            n = 0
            lst = []
            while n < i:
                try :
                    #print(n,dt[3+n*7])
                    #忘记对n*7
                    int(dt[3+n*7])
                    lst.append("{} {}{}{}{}:{}{}Ended".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                except ValueError:
                    lst.append("{} {}{}{}{}:{}{}Not started".format(dt[0+n*7], dt[5+n*7], dt[6+n*7], dt[1+n*7], dt[3+n*7], dt[4+n*7], dt[2+n*7]))
                n = n + 1
            return lst
                #遇到错误：TypeError: list indices must be integers or slices, not float
                        #意思是：list的索引必须是’integers’  or slices,
                        #要点：" / "就表示 浮点数除法，返回浮点结果;" // "表示整数除法。
        else:
            None

#admin add match
#input team1, team2, score1, score2, date, time
def admin_AM(team1, team2, score1, score2, date, times):
    #flag提交错误：将AM的flag提交到DM中
    #导致相当长一段时间存在IndexError: tuple index out of range
    if validate_date(date):
        cs.send(str(("AM", team1, team2, score1, score2, date, times)).encode())
        if cs.recv(1024).decode() == "Match added":
            return True

#admin delete match
#input match_id
def admin_DM():
    match_id = input("Match_id:")
    cs.send(str(("DM", match_id)).encode())
    if cs.recv(1024).decode() == "Match deleted":
        return True

#admin update match
#input match_id, team1, team2, score1, score2, date, time
def admin_UM(match_id, team1, team2, score1, score2, date, times):
    if validate_date(date):
        cs.send(str(("UM", team1, team2, score1, score2, date, times, match_id)).encode())
        if cs.recv(1024).decode() == "Match updated":
            return True


#change the console_version to GUI_version
#user login
#input: username, password
def clienter_U(Name, Password):
    cs.send(str(("U", Name,Password)).encode())
    #print(cs.recv(1024).decode())
    if cs.recv(1024).decode() == "True":
        return True
    elif cs.recv(1024).decode() == "None":
        return None
    else:
        return False

#admin login
#input: username, password
def clienter_A(Name, Password):
    cs.send(str(("A", Name, Password)).encode())
    if cs.recv(1024).decode() == "True":
        return True
    elif cs.recv(1024).decode() == "None":
        return None
    else:
        return False



#user register
#input: username, password, confirm password
def clienter_RU(Name, Password):
    cs.send(str(("RU", Name, Password)).encode())
    if cs.recv(1024).decode() == "True":
        return False
    elif cs.recv(1024).decode() == "None":
        return True


#admin register
#input: username, password, confirm password
#not use
def clienter_RA(Name, Password, CPassword):
    if Password == CPassword:
        cs.send(str(("RA", Name, Password)).encode())
        if cs.recv(1024).decode() == "True":
            print("You have been registered")
    else:
        print("Passwords do not match")