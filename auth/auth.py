from flask import Blueprint, render_template


auth_bp = Blueprint(
    "auth_bp", __name__, static_folder="static", template_folder="templates"
)


@auth_bp.route("/")
def login_page():
    return render_template("hello.html")


@auth_bp.route("/register")
def register_page():
    return render_template("bang.html")
