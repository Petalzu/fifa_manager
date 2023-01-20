import socket
import sqlite3
sql = sqlite3.connect("database.db")
print('connected to the database successfully')
c = sql.cursor()
'''
c.execute("""CREATE TABLE users
        (user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(20) NOT NULL,
            password INTEGER NOT NULL);
            """)
c.execute("""CREATE TABLE admin
        (admin_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name CHAR(20) NOT NULL,
            password INTEGER NOT NULL);
            """)
#错误：最后一行“)”里边没有逗号
c.execute("""CREATE TABLE matches
        (match_id INTEGER PRIMARY KEY AUTOINCREMENT,
            team1 CHAR(20) NOT NULL,
            team2 CHAR(20) NOT NULL,
            score1 INTEGER NOT NULL,
            score2 INTEGER NOT NULL,
            date CHAR(20) NOT NULL,
            times CHAR(20) NOT NULL);
            """)
print ("Table created successfully")
'''

host = socket.gethostname()
port = 5000
sever_socket = socket.socket()
sever_socket.bind((host,port))
sever_socket.listen(2)
conn,address = sever_socket.accept()
print("Connection from: " + str(address))

#search for a match using team name or date or both
def user_tools():
    data = conn.recv(1024).decode()
    data = eval(data)
    flag = data[0]
    if flag == "STD":
        team1 = data[1]
        team2 = data[2]
        date = data[3]
        matches = c.execute("""SELECT * FROM matches WHERE (team1 = '{}' AND team2 = '{}') AND date = '{}';""".format(team1,team2,date)).fetchall()
        conn.send(str((matches)).encode())
        user_tools()
    elif flag == "q":
        main()
    else:
        user_tools()


#admin interface
#search team or date or both
#add match, delete match, update match
def admin_tools():
    data = conn.recv(1024).decode()
    data =eval(data)
    flag = data[0]
    if flag == "ST":
        team1 = data[1]
        team2 = data[2]
        #一个简单的错误：team1，2没有分开
        match1 = c.execute("""SELECT * FROM matches WHERE team1 = '{}' AND team2 = '{}';""".format(team1,team2)).fetchall()
        conn.send(str(match1).encode())
        admin_tools()
    elif flag == "SD":
        date = data[1]
        match2 = c.execute("""SELECT * FROM matches WHERE date = '{}';""".format(date)).fetchall()
        conn.send(str((match2)).encode())
        admin_tools()
    elif flag == "STD":
        team1 = data[1]
        team2 = data[2]
        date = data[3]
        match3 = c.execute("""SELECT * FROM matches WHERE (team1 = '{}' AND team2 = '{}') AND date = '{}';""".format(team1,team2,date)).fetchall()
        conn.send(str((match3)).encode())
        admin_tools()
    elif flag == "AM":
        c.execute("""INSERT INTO matches (team1, team2, score1, score2, date, times) VALUES (?,?,?,?,?,?);""",(data[1],data[2],data[3],data[4],data[5],data[6]))
        sql.commit()
        #遇到错误：无法更改db文件数据
        #需要commit（）提交到数据库
        conn.send(str(("Match added")).encode())
        admin_tools()
    elif flag == "DM":
        c.execute("""DELETE FROM matches WHERE match_id = '{}';""".format(data[1]))
        sql.commit()
        conn.send(str(("Match deleted")).encode())
        admin_tools()
    elif flag == "UM":
        c.execute("""UPDATE matches SET team1 = '{}', team2 = '{}', score1 = '{}', score2 = '{}', date = '{}', times = '{}' WHERE match_id = '{}';""".format(data[1],data[2],data[3],data[4],data[5],data[6],data[7]))
        sql.commit()
        conn.send(str(("Match updated")).encode())
        admin_tools()
    elif flag == "q":
        main()
    else:
        admin_tools()


#main loop
def main():
    data = conn.recv(1024).decode()
    data = eval(data)
    flag = data[0]
    if flag == "U":
        user = c.execute("""SELECT password FROM users WHERE name = '{}';""".format(data[1])).fetchone()
        if user == None:
            conn.send(("None").encode())
            main()
        elif str(user[0]) == str(data[2]):
            conn.send(("True").encode())
            admin_tools()
        else:
            conn.send(("False").encode())
            main()
    elif flag == "A":
        admin = c.execute("""SELECT password FROM admin WHERE name = '{}';""".format(data[1])).fetchone()
        if admin == None:
            conn.send(("None").encode())
            main()
            #change
        elif str(admin[0]) == str(data[2]):
            conn.send(("True").encode())
            admin_tools()
        else:
            conn.send(("False").encode())
            main()
    elif flag == "RU":
        user = c.execute("""SELECT * FROM users WHERE name = '{}';""".format(data[1])).fetchone()
        if user != None:
            conn.send(("True").encode())
            main()
        else:
            c.execute("""INSERT INTO users (name, password) VALUES (?,?);""",(data[1],data[2]))
            sql.commit()
            conn.send(("False").encode())
            main()
    elif flag == "RA":
        admin = c.execute("""SELECT * FROM admin WHERE name = '{}';""".format(data[1])).fetchone()
        if admin != None:
            conn.send(("True").encode())
            main()
        else:
            #change
            c.execute("""INSERT INTO admin (name, password) VALUES (?,?);""",(data[1],data[2]))
            sql.commit()
            conn.send(("False").encode())
            main()
    elif flag == "k":
        conn.close()
    else:
        main()

main()