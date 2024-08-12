from init_db import get_db


class User:
    def __init__(self,db_instance=get_db):
        self.db_instance=db_instance()
        
    def list_users(self):
        try:
            cursor = self.db_instance.cursor()
            cursor.execute("SELECT username, password,email FROM users")
            values = cursor.fetchall()
            if cursor.description:
                column_names = [description[0] for description in cursor.description]
                allusers = [dict(zip(column_names, value)) for value in values]
                return allusers
        except:
                return []
        finally:
            cursor.close()
    
    def add_user(self,username,password,email):
        try:
            cursor = self.db_instance.cursor()
            cursor.execute("SELECT username FROM users WHERE username=?",(username,))
            values=cursor.fetchall()
            if cursor.description:
                column_names = [description[0] for description in cursor.description]
                mydata = [dict(zip(column_names, value)) for value in values]
            if mydata:
                return 0
            cursor.execute(
                "INSERT INTO users (username, password,email) VALUES (?, ?,?)",
                (username,password,email),
            )
            self.db_instance.commit()
            return 1            
        except Exception as e:
            self.db_instance.rollback()
            print(e)
        finally:
            cursor.close()  

    def get_user(self,username,password):
        try:
            cursor = self.db_instance.cursor()
            cursor.execute(
                "SELECT username, password FROM users WHERE username=? AND password=?",
                (username, password),
            )
            values = cursor.fetchall()
            if cursor.description:
                column_names = [description[0] for description in cursor.description]
                mydata = [dict(zip(column_names, value)) for value in values]
                return mydata 
        except Exception as e:
            print(e)
        finally:
            cursor.close()
    def remove_user():
        pass
    

def email_verification(receiver_email):
    email_check1 = ["gmail","hotmail","yahoo","outlook","mylambton"]
    email_check2 = [".com",".in",".org",".edu",".co.in",".ca"]
    count = 0

    for domain in email_check1:
        if domain in receiver_email:
            count+=1
    for site in email_check2:
        if site in receiver_email:
            count+=1

    if "@" not in receiver_email or count!=2:
        return 0
    return 1

