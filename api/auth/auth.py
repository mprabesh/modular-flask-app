import datetime
from flask import Blueprint, jsonify, request, current_app
from .utils import Auth
from init_db import get_db
import jwt

auth_controller_bp = Blueprint("auth_controller_bp", __name__)


@auth_controller_bp.route("/login", methods=["POST"])
def user_login():
    try:
        username = request.json.get("username")
        password = request.json.get("password")
        if username and password:
            auth=Auth(username,password)
            login_status=auth.user_login()
            print(login_status,"apple and orange")
            if login_status:
                payload = {'user': username,'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}  # Token expires in 30 minute}
                token = jwt.encode(payload, current_app.config['SECRET_KEY'])
                return (jsonify({"status": "success", "data":{"token":token,"userid":username}}),200)
            else:
                return jsonify({"status": "fail", "message": "Incorrect Credentials"})
        else:
            return jsonify({"error": "Username and password required"}), 400
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred"}), 500