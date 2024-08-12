from init_db import get_db


class Auth:
    def __init__(self,username,password,db_instance=get_db):
        self.db_instance=db_instance()
        self.username=username
        self.password=password
        
    def user_login(self):
        try:
            cursor=self.db_instance.cursor()
            cursor.execute(
                "SELECT username, password FROM users WHERE username=? AND password=?",
                (self.username, self.password),
            )
            value=cursor.fetchone()
            if value is not None:
                if value["username"]==self.username and value["password"]==self.password:
                    return True
                else:
                    return False
        except Exception as e:
            return {"msg":e,"status":"fail"}
        finally:
            cursor.close()
    
    def user_token():
        pass
    
