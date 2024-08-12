from flask import Blueprint, jsonify, request, current_app
from .utils import hash_my_url
from init_db import get_db
import jwt

link_generate_bp = Blueprint("link_generate_bp", __name__)

# Decorator to check token
def token_required(f):
    def decorator(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 403
        try:
            token = token.split(" ")[1]  # Assumes Bearer token format
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 403
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 403
        return f(*args, **kwargs,decoded_data=data)
    decorator.__name__=f.__name__
    return decorator

@link_generate_bp.route("/<username>", methods=["GET"])
# @token_required
def list_user_URL(username):
    db = get_db()
    cursor = db.cursor()
    try:
        cursor.execute("SELECT * FROM urls WHERE userid=?", (username,))
        values = cursor.fetchall()
        if cursor.description:
            column_names = [description[0] for description in cursor.description]
            mydata = [dict(zip(column_names, value)) for value in values]
            return jsonify({"status": "success", "data": mydata}), 200
        return jsonify({"status": "fail", "msg": "No URLs found for user"}), 404
    except Exception as e:
        return jsonify({"status": "fail", "msg": str(e)}), 500
    finally:
        cursor.close()

@link_generate_bp.route("/", methods=["POST"])
@token_required
def create_short_url(decoded_data):
    db = get_db()
    cursor = db.cursor()
    try:
        inputurl = request.json.get("inputURL")
        username = request.json.get("username")
        if username and inputurl and decoded_data['user']:
            encoded_value = hash_my_url(inputurl+username[2:-1])
            cursor.execute("INSERT INTO urls (original_url, short_link, userid) VALUES (?, ?, ?)",
                           (inputurl, encoded_value, username))
            db.commit()
            print(encoded_value)
            return jsonify({"status": "success", "data": {"shortURL": f"http://127.0.0.1:5000/{encoded_value}"}}),200
        return jsonify({"status": "fail", "msg": "Missing URL or username"}), 400
    except Exception as e:
        db.rollback()
        return jsonify({"status": "fail", "msg": str(e)}), 500
    finally:
        cursor.close()
        
        
        
@link_generate_bp.route("/<id>",methods=["DELETE"])
@token_required    
def remove_short_url(id,decoded_data):
    db=get_db()
    cursor=db.cursor()
    try:
        if id and decoded_data['user']:
            cursor.execute("SELECT * FROM urls WHERE id=?",(id,))
            values = cursor.fetchall()
            if cursor.description:
                column_names = [description[0] for description in cursor.description]
                mydata = [dict(zip(column_names, value)) for value in values]
                # if the data with the wanted id is not foudn check for the empty array otherwise an exception error may be encountered
                if mydata:
                    if mydata[0]['userid']==decoded_data['user']:
                        print(mydata)
                        cursor.execute("DELETE FROM urls WHERE id=?",id)
                        db.commit()
                        return jsonify({"status":"success","message":"Deleted successfully"}),200   
                    else:
                        return jsonify({"status":"fail","message":"Unauthorized"}),401
                else:
                    return jsonify({"status":"success","message":"Deleted successfully"}),200   
        else:
            return jsonify({"status":"fail","message":"No valid credentials"}),401
    except Exception as e:
        return jsonify({"status":"fail","message":e}),500
    finally:
        cursor.close()
    
