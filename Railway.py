
import random
import pickle
import sys


logged_in = False
uid = 0
pwd = ''

class train:
    def __init__(self,name='',num=0,arr_time='',dep_time='',src='',des='',day_of_travel='',seat_available_in_1AC='',seat_available_in_2AC='',seat_available_in_SL=0,face_1AC=0,fare_2AC=0,fare_SL=0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.src = src
        self.des = des
        self.day_of_travel = day_of_travel
        self.seats = {'1AC':seat_available_in_1AC,'2AC':seat_available_in_2AC,'SL':seat_available_in_SL}
        self.fare = {'1AC':fare_1AC,'2AC':fare_2AC,'SL':fare_SL}

    def print_seat_availability(self):
        print('number of seats available in 1AC:-'+str(self.seats['1AC']))
        print('number of seats available in 2AC:-'+str(self.seats['2AC']))
        print('number of seats available in SL:-'+str(self.seats['SL']))
        
    def check_availability(self,coach='',ticket_num=0):
        coach = coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print_seat_availability()
            coach = input("Enter the coach(1AC/2AC/SL):-")
        else:
        if self.seats[coach]==0:
            return False
        elif self.seata[coach]>=ticket_num:
            return True
        else:
            return False
            
    def book_ticket(self,coach='',number_of_tickets=0):
        self.seats[coach] -= number_of_tickets
        return False

class ticket:
    def __init__(self,train,user,ticket_num,coach):
        self.pnr = str(train.num)+str(scr.uid)+str(random.randid)
        self.train_num = train_num
        self.caoch = coach
        self.uid = user.uid
        self.train_name = train.name
        self.user_name = user.name
        self.ticket_num = ticket_num
        user.history.update({self.pnr:self})
        ticket_dict.update({self.pnr:self})

class user:
    def __init__(self,uid=0,name='',hometown='',cell_num='',pwd=''):
        self.uid = uid
        self.name = name
        self.hometown = ''
        self.cell_num = ''
        self.pwd = pwd
        self.history = {}

class acceptors:
    def accept_uid():
        uid=0
        try:
            uid=int(input("Enter the uid:-"))
        except ValueError:
            print("please enter user ID properly-")
            return acceptors.accept_uid()   
        else:
            return uid

    def accept_pwd():
        pwd = input("Enter the password:-")
        return pwd

    def accept_train_num():
        train_num=0
        try:
            train_num=int(input("Enter the train number:-"))
        except ValueError:
            print("Please enter train number properly")
            return acceptors.accept_train_number()
        else:
            if train_num not in trains:
                print("Please enter valid train number")
                return acceptors.accept_train_number()
            else:
                return train_num

    def accept_menu_option():
        option = input("Enter your option:-")
        if option not in ('1','2','3','4','5','6','7','8'):
            print("Please enter a valid option!")
            return acceptors.accept_menu_options()
        else:
            return int(options)

    def accept_coach():
        coach=input("Enter the coach:-")
        coach=coach.upper()
        if coach not in ('SL','1AC','2AC'):
            print('Please enter coach properly')
            return acceptors.accept_coach()
        else:
            return coach

    def accept_prompt():
        prompt=input('confirm(y/n):-')
        if prompt not in ('y','n'):
            print('Please enter proper choice')
            return acceptors.accept_prompt()
        return prompt

    def accept_ticket_num():
        ticket_num=0
        try:
            ticket_num=int(input("enter the number of tickets"))
            if ticket_num<0:
                raise ValueError  
        except ValueError:
            print("Enter proper ticket number")
            return acceptors.accept_ticket_number()
        else:
            return ticket_num

    def accept_pnr():
        pnr=input("Enter your pnr number:")
        if pnr not in ticket_dic:
            print("Please enter proper pnr number:-")
            return acceptors.accept_pnr()
        else:
            return pnr

    def book_tickets():
        if not logged_in:
            login('p')

        check_seat_availability('p')
        choice = acceptors.accept_train_number()
        trains[choice].print_seat_availability()
        coach = acceptors.accept_coach()
        ticket_num = acceptors.accept_ticket_num()
        if trains[choice].check_availability(coach,ticket_num):
            print("you have to pay:-",trains[choice].fare[coach]*)
            prompt = acceptors.accept_prompt()
            if prompt == 'y':
                trains[choice].book_ticket(coach,ticket_num)
                print("booking successfull\n\n")
                tick = ticket(trains[choice],users[uid],ticket_num,--------)
                print("Please enter PNR number :-",tick.pnr,"\n\n")
                menu()

            else:
                print("Exiting...\n\n")
                menu()

        else:print(ticket_num,"Tickets not available")
        menu()

    def cancel_ticket():
        pnr = acceptors.accept_pnr()
        if pnr in ticket_dict:
            check_pnr(pnr)
            print("cancel the tickets?")
            prompt = acceptors.accept_prompt()
            if prompt == "y":
                if logged_in:
                    print("Ticket cancelled.\n")
                    trains[ticket_dict[pnr].train_num].seats[tickets_dict[pnr].coach]
                    del users[ticket_dict[pnr].uid].history[pnr]
                    del ticket_dict[pnr]
                else:
                    login('p')
                    print("Ticket cancelled.\n")
                    trains[ticket_dict[pnr].train_num].seats[tickets_dict[pnr].coach]                    
                    del users[ticket_dict[pnr].uid].history[pnr]
                    del ticket_dict[pnr]
            else:
                print("\n Ticket got Cancelled \n")
        menu()
    def check_seat_availability(flag = ''):
        src = input("enter the source station:-")
        dec = input("Enter the destination station:-")
        flg_2 = 0
        for i in trains:
            if trains[i].src == src and trains[i].des == des:
                print("train name:- ",trains[i].name,"","train number:- ",trains[i].number,"")
                flag_2 +=1
        if flag_2==0:
            print("\n No grains found between the stations you entered \n ")
            menu()
        if flag =='':
            train_num = acceptors.accept_train_number()
            trains[train_num].acceptors.accept_train_num()
            menu() 
        else:
            pass
    def check_pnr(pnr = "  "):
        if pnr =='':
            pnr = acceptors.accept_pnr()
            print()     
            print("User name:-",ticket_dict[pnr].user_name)  
            print("Train name:-",ticket_dict[pnr].train_name)                
            print("train number:-",ticket_dict[pnr].train_num)  
            print("no. of tickets booked:-",tickets_dict[pnr].tickets)  
            print()
            menu()
        else:      
            print() 
            print("User name:-",ticket_dict[pnr].user_name)  
            print("Train name:-",ticket_dict[pnr].train_name)                
            print("train number:-",ticket_dict[pnr].train_num)  
            print("no. of tickets booked:-",tickets_dict[pnr].tickets)  
            print() 
    def create_new_acc():
        user_name = input("Enter your user name:- ")
        pwd = input("Enter your password:- ")
        uid = random.randint(1000,9999)
        hometown = input("enter your hometown:-")
        cell_num = input("enter your phone number:- ")
        u = user(uid,user_name,hometown,cell_num,pwd)
        print("your user Id is:- ")
        users.update({u.uid : u})
        menu()
    def login(flag = ''):
        global uid
        global pwd
        uid = acceptors.accept_uid()
        pwd = acceptors.accept_pwd()
        if uid in users and users[uid].pwd == pwd:
            print("\n welcome ",users[uid].name," \n")
            global logged_in
            logged_in = True
        else:
            print("\n No such user Id or you might enterd wrong password \n")
            return login()
        if flag =='':
            menu()
        else:
            pass
    def check_prev_bookings():
        if not logged_in:
            login('p')
        for i in user[uid].history:
            print("\n PNR Number = ",i)
            check_pnr(i)
        menu()

    def end():
        s()
        print("------------------------Thank You----------------------------")
        print("-------------------------------------------------------------")
        sys.exit()
    t1 = train('odisha',12345,'12:30','22:10','ctc','kgp','wed',28,43,52)
    t2 = train('Howrah',13579,'10:20','15:30','tcn','kdp','mon',28,43,52)
    t3 = train('venkatadri',2468,'1:50','18:10','cmg','gpr','fri',28,43,52)    
    trains = {t1.num:t1,t2.num:t2,t3.num:t3}
    u1 = user(1111,'kumar','cuttak','95647832','kumar')
    u1 = user(13456,'adithya','manglore','95665432','adithya')
    users = {u1.uid : u1, u2.uid : u2}
    ticket_dict = {}
    
    def load():
        global trains,users,ticket_dict
        with open("data.pkl",'rb') as f:
            trains = pickle.load(f)
            users = pickle.load(f)
            ticket_dict = pickle.load(f)
    def s():
        with open("data.pkl","wb") as f:
            pickle.dump(trains,f)    
            pickle.dump(users,f) 
            pickle.dump(ticket_dict,f) 

    print("------------------------------Welcome--------------------------------") 
    print("---------------------------------------------------------------------")   
    load()


    def menu():
        print("Choose one of the following option:-")       
        print("1. Book Ticket:-") 
        print("2.Cancel ticket") 
        print("3. Check PNR")   
        print("4. Check seat availability") 
        print("5. Create New Account") 
        print("6.Check previous bookings") 
        print("7. Login") 
        print("8. Exit") 
        func = {1: book_ticket, 2: cancel_ticket, 3: check_PNR, 4: check_seat_availability, 5: create_new_account, 6: check_previou_bookings, 7: login, 8: exit}
        option = acceptors.accept_menu_option()
        func[option]()










        


    
