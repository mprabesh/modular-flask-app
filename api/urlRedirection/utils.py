from init_db import get_db

def get_user_URL(short_link_param):
    try:
        db=get_db()
        cursor=db.cursor()
        if short_link_param:
            print(short_link_param)
            cursor.execute("SELECT original_url,short_link FROM urls WHERE short_link=?",(short_link_param,))
            value=cursor.fetchone()
            print(value)
            if value is not None:
                original_url=value["original_url"]
                return original_url
    except Exception as e:
        return e
        
