from flask import Blueprint, jsonify, request,current_app
from .utils import User,email_verification
from init_db import get_db
import jwt

user_controller_bp = Blueprint("user_controller_bp", __name__)


@user_controller_bp.route("/", methods=["POST"])
def user_detail_validation():
    try:
        # Get data from request
        email=request.json.get("email")
        username = request.json.get("username")
        password = request.json.get("password")
        if username and password and email:
            if email_verification(email):
                user=User()
                result=user.add_user(username,password,email)
                if result:
                    return jsonify({"status":"success","data":{"msg":"added successfully"}})
                else:
                    return jsonify({"status":"fail","data":{"message":"Already a user"}})
            else:
                return jsonify({"status":"fail","data":{"message":"Use proper email"}})
        else:
            return jsonify({"error": "Username and password required","status":"fail"}), 400
    except Exception as e:
        return jsonify({"status":"success","msg":e})



@user_controller_bp.route("/login", methods=["POST"])
def user_login():
    db = get_db()
    cursor = db.cursor()
    try:
        username = request.json.get("username")
        password = request.json.get("password")
        if username and password:
            cursor.execute(
                "SELECT username, password FROM users WHERE username=? AND password=?",
                (username, password),
            )
            values = cursor.fetchall()
            if cursor.description:
                column_names = [description[0] for description in cursor.description]
                mydata = [dict(zip(column_names, value)) for value in values]
                if not bool(mydata):
                    return (
                        jsonify({"status": "fail", "message": "Incorrect Credentials"}),
                        401,
                    )
                if (
                    mydata[0]["username"] == username
                    and mydata[0]["password"] == password
                ):
                    return (
                        jsonify(
                            {"status": "success", "message": "Correct Credentials"}
                        ),
                        200,
                    )
        else:
            return jsonify({"error": "Username and password required"}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    finally:
        cursor.close()

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
        return f(*args, **kwargs)
    decorator.__name__=f.__name__
    return decorator


@user_controller_bp.route("/", methods=["GET"])
# @token_required
def get_all_users():
    db = get_db()
    cursor = db.cursor()
    try:
        user=User()
        user_list=user.list_users()
        return user_list,200
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500
    finally:
        cursor.close()
