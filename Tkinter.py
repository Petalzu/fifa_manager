import tkinter
from clinet import *
import tkinter.messagebox
#问题：无法通过tkinter使用messagebox
#solve:在python3.7中，tkinter.messagebox已经被弃用，使用tkinter.messagebox.showinfo()代替
#调用子模块
import threading


#A gui interface for all functions in the clinet library
class Gui:
    def __init__(self):
        self.main()

    def main(self):
        self.window = tkinter.Tk()
        self.window.title("FIFA")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(background="black")
        #在类中 __init__函数前定义好Entry组件的textvariable变量
        self.enter_N = tkinter.StringVar()
        self.enter_P = tkinter.StringVar()
        self.enter_NA = tkinter.StringVar()
        self.enter_PA = tkinter.StringVar()
        self.enter_T1 = tkinter.StringVar()
        self.enter_T2 = tkinter.StringVar()
        self.enter_D = tkinter.StringVar()
        self.enter_CP = tkinter.StringVar()
        self.enter_M = tkinter.StringVar()
        self.enter_T = tkinter.StringVar()
        self.enter_S1 = tkinter.StringVar()
        self.enter_S2 = tkinter.StringVar()
        self.enter_NR = tkinter.StringVar()
        self.enter_PR = tkinter.StringVar()
        self.enter_CPR = tkinter.StringVar()

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()
        self.button_U = tkinter.Button(self.window, text="User", fg="white", bg="black", command=self.user)
        self.button_U.pack()
        self.button_AA = tkinter.Button(self.window, text="Admin", fg="white", bg="black", command=self.admin)
        self.button_AA.pack()
        self.button_AA = tkinter.Button(self.window, text="Rigister", fg="white", bg="black", command=self.user_register)
        self.button_AA.pack()
        self.window.mainloop()


    def thread_it(func, *args):
        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)   # 守护--就算主界面关闭，线程也会留守后台运行（不对!）
        t.start()
    #if user clicks on User button ,then skip to a new window where user can enter their name
    # and password and then login
    #and the past page will be closed
    #the page have a button to turn back to the main page
    #the value of the name and password will be sent to the clinet
    #the clinet will send the value to the server
    #the server will check the value and return a value to the clinet
    #the clinet will check the value and return a value to the gui
    def user(self):

        self.window = tkinter.Toplevel()
        #窗口影响，初始化窗体时，将Entry组件所在的主体窗口，tk.Tk() 改为 tk.Toplevel()
        self.window.title("FIFA")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(background="black")

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.label = tkinter.Label(self.window, text="Name:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_N = tkinter.Entry(self.window, width=50, textvariable=self.enter_N)
        self.entry_N.pack()

        self.label = tkinter.Label(self.window, text="Password:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_P = tkinter.Entry(self.window, width=50, textvariable=self.enter_P)
        self.entry_P.pack()

        def user_button_L():
            name = self.enter_N.get()
            password = self.enter_P.get()
            re1 = clienter_U(name, password)
            print(re1,type(re1))
            if re1 == True:
                tkinter.messagebox.showinfo(title='Welcome',message='User {}'.format(self.enter_N.get()))
                self.user_search()
            elif re1 == None:
                tkinter.messagebox.showinfo(title='Warning',message='User does not exist')
            else:
                tkinter.messagebox.showinfo(title='Warning',message='Wrong password or name')
            #使用get()方法获取输入框的内容
            #使用messagebox弹出提示框
            #print('name',name)
            #print(password)

        self.button_L = tkinter.Button(self.window, text="Login", fg="white", bg="black", command=user_button_L)
        self.button_L.pack()
        #为什么传递不到呢？因为button命名冲突了导致admin能用，user不能用
        self.window.mainloop()

    #after user login in, then skip to a new window where user can serach for matches
    #in first buttion, user can enter the name of two teams they want to search for
    #in second button, user can enter time of the match they want to search for
    #after user click on search button, then skip to a new window where user can see the result
    def user_search(self):
        self.window = tkinter.Toplevel()
        self.window.title("FIFA")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(background="black")

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.label = tkinter.Label(self.window, text="Team1:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_T1 = tkinter.Entry(self.window, width=50, textvariable=self.enter_T1)
        self.entry_T1.pack()

        self.label = tkinter.Label(self.window, text="Team2:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_T2 = tkinter.Entry(self.window, width=50, textvariable=self.enter_T2)
        self.entry_T2.pack()

        self.label = tkinter.Label(self.window, text="Date:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_D = tkinter.Entry(self.window, width=50, textvariable=self.enter_D)
        self.entry_D.pack()

        def user_search_button_S():
            team1 = self.enter_T1.get()
            team2 = self.enter_T2.get()
            date = self.enter_D.get()
            if team1 == "" and team2 == "" and date != "":
                re2 = admin_SD(date)
                #print(re)
                if re2 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                elif re2 == False:
                    tkinter.messagebox.showinfo(title='Warning',message='Wrong date form')
                else:
                    self.text.insert(tkinter.INSERT, re2)
                    #在这里一直未响应，经查是因为server有问题
                    #user_tool转为admin_tool后，可以正常运行
                    #服务端不再对权限限制，因为前端已经做了限制
            elif team1 != "" and team2 != "" and date == "":
                re2 = admin_ST(team1, team2)
                #print(re)
                if re2 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                else:
                    self.text.insert(tkinter.INSERT, re2)
            elif team1 != "" and team2 != "" and date != "":
                re2 = admin_STD(team1, team2, date)
                #print(re)
                if re2 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                elif re2 == False:
                    tkinter.messagebox.showinfo(title='Warning',message='Wrong date form')
                else:
                    self.text.insert(tkinter.INSERT, re2)
            #print(team1)
            #print(team2)
            #print(date)

        self.button_S = tkinter.Button(self.window, text="Search", fg="white", bg="black", command=user_search_button_S)
        self.button_S.pack()

        self.text = tkinter.Text(self.window, width=50, height=5, undo=True, autoseparators=False)
        self.text.pack()
        #using text to show the result

    #if admin clicks on User button ,then skip to a new window where user can enter their name and password and then login
    #the page have a button to turn back to the main page
    def admin(self):
        self.window = tkinter.Toplevel()
        self.window.title("FIFA")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(background="black")

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.label = tkinter.Label(self.window, text="Name:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_NA = tkinter.Entry(self.window, width=50, textvariable=self.enter_NA)
        self.entry_NA.pack()

        self.label = tkinter.Label(self.window, text="Password:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_PA = tkinter.Entry(self.window, width=50, textvariable=self.enter_PA)
        self.entry_PA.pack()

        def admin_button_L():
            name = self.enter_NA.get()
            password = self.enter_PA.get()
            re3 = clienter_A(name, password)
            if re3 == True:
                tkinter.messagebox.showinfo(title='Welcome',message='Admin {}'.format(self.enter_NA.get()))
                self.admin_tool()
            elif re3 == None:
                tkinter.messagebox.showinfo(title='Warning',message='Admin does not exist')
            else:
                tkinter.messagebox.showinfo(title='Warning',message='Wrong password or name')

        self.button_LA = tkinter.Button(self.window, text="Login", fg="white", bg="black", command=admin_button_L)
        self.button_LA.pack()
        self.window.mainloop()

    #admin have all of the functions of user
    #admin can also add new match, delete match, update match by functions in clineter

    def admin_tool(self):
        self.window = tkinter.Toplevel()
        self.window.title("FIFA")
        self.window.geometry("1000x1000")
        self.window.resizable(False, False)
        self.window.configure(background="black")

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.label = tkinter.Label(self.window, text="Team1:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_T1 = tkinter.Entry(self.window, width=50, textvariable=self.enter_T1)
        self.entry_T1.pack()

        self.label = tkinter.Label(self.window, text="Team2:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_T2 = tkinter.Entry(self.window, width=50, textvariable=self.enter_T2)
        self.entry_T2.pack()

        self.label = tkinter.Label(self.window, text="Score1:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_S1 = tkinter.Entry(self.window, width=50, textvariable=self.enter_S1)
        self.entry_S1.pack()

        self.label = tkinter.Label(self.window, text="Score2:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_S2 = tkinter.Entry(self.window, width=50, textvariable=self.enter_S2)
        self.entry_S2.pack()

        self.label = tkinter.Label(self.window, text="Date:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_D = tkinter.Entry(self.window, width=50, textvariable=self.enter_D)
        self.entry_D.pack()

        self.label = tkinter.Label(self.window, text="Time:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_T = tkinter.Entry(self.window, width=50, textvariable=self.enter_T)
        self.entry_T.pack()

        self.label = tkinter.Label(self.window, text="Match_id:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_M = tkinter.Entry(self.window, width=50, textvariable=self.enter_M)
        self.entry_M.pack()

        def admin_search_button_S():
            team1 = self.enter_T1.get()
            team2 = self.enter_T2.get()
            date = self.enter_D.get()
            if team1 == "" and team2 == "" and date != "":
                re4 = admin_SD(date)
                #print(re4)
                if re4 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                elif re4 == False:
                    tkinter.messagebox.showinfo(title='Warning',message='Wrong date form')
                else:
                    self.text.insert(tkinter.INSERT, re4)
            elif team1 != "" and team2 != "" and date == "":
                re4 = admin_ST(team1, team2)
                #print(re4)
                if re4 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                else:
                    self.text.insert(tkinter.INSERT, re4)
            elif team1 != "" and team2 != "" and date != "":
                re4 = admin_STD(team1, team2, date)
                #print(re4)
                if re4 == None:
                    tkinter.messagebox.showinfo(title='Warning',message='No match')
                elif re4 == False:
                    tkinter.messagebox.showinfo(title='Warning',message='Wrong date form')
                else:
                    self.text.insert(tkinter.INSERT, re4)

        self.button_SA = tkinter.Button(self.window, text="Search", fg="white", bg="black", command=admin_search_button_S)
        self.button_SA.pack()

        def admin_add():
            team1 = self.enter_T1.get()
            team2 = self.enter_T2.get()
            score1 = self.enter_S1.get()
            score2 = self.enter_S2.get()
            date = self.enter_D.get()
            time = self.enter_T.get()
            admin_AM(team1, team2, score1, score2, date, time)
            tkinter.messagebox.showinfo(title='Tips',message='Match added')

        self.button_AA = tkinter.Button(self.window, text="Add", fg="white", bg="black", command=admin_add)
        self.button_AA.pack()

        def admin_delete():
            match_id = self.enter_M.get()
            admin_DM(match_id)
            tkinter.messagebox.showinfo(title='Tips',message='Match deleted')
        self.button_DA = tkinter.Button(self.window, text="Delete", fg="white", bg="black", command=admin_delete)
        self.button_DA.pack()

        def admin_update():
            team1 = self.enter_T1.get()
            team2 = self.enter_T2.get()
            score1 = self.enter_S1.get()
            score2 = self.enter_S2.get()
            date = self.enter_D.get()
            time = self.enter_T.get()
            match_id = self.enter_M.get()
            admin_UM(team1, team2, score1, score2, date, time, match_id)
            tkinter.messagebox.showinfo(title='Tips',message='Match updated')
        self.button_UA = tkinter.Button(self.window, text="Update", fg="white", bg="black", command=admin_update)
        self.button_UA.pack()

        self.text = tkinter.Text(self.window, width=70, height=40, undo=True, autoseparators=False)
        self.text.pack()

        self.window.mainloop()

        #register a new user
        #the password need to be confirmed
    def user_register(self):
        self.window = tkinter.Toplevel()
        self.window.title("FIFA")
        self.window.geometry("500x500")
        self.window.resizable(False, False)
        self.window.configure(background="black")

        self.label = tkinter.Label(self.window, text="FIFA", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.label = tkinter.Label(self.window, text="Name:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_NR = tkinter.Entry(self.window, width=50, textvariable=self.enter_NR)
        self.entry_NR.pack()

        self.label = tkinter.Label(self.window, text="Password:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_PR = tkinter.Entry(self.window, width=50, textvariable=self.enter_PR)
        self.entry_PR.pack()

        self.label = tkinter.Label(self.window, text="Confirm Password:", fg="white", bg="black", font=("Arial", 20))
        self.label.pack()

        self.entry_CPR = tkinter.Entry(self.window, width=50, textvariable=self.enter_CPR)
        self.entry_CPR.pack()

        def user_button_R():
            name = self.enter_NR.get()
            password = self.enter_PR.get()
            confirm = self.enter_CPR.get()
            if password == confirm:
                re5 = clienter_RU(name, password)
                if re5 == True:
                    tkinter.messagebox.showinfo(title='Welcome',message='User {}'.format(self.enter_NR.get()))
                    self.main()
                elif re5 == False:
                    tkinter.messagebox.showinfo(title='Warning',message='User already exist')
                    self.main()
            else:
                tkinter.messagebox.showinfo(title='Warning',message='Password not match')
                self.user_register()

        self.button_RUU = tkinter.Button(self.window, text="Register", fg="white", bg="black", command=user_button_R)
        self.button_RUU.pack()
        self.window.mainloop()


#run zhe gui
Gui().window.mainloop()