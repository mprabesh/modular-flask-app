from flask import Blueprint, render_template

link_short_bp = Blueprint(
    "link_short_bp", __name__, static_folder="static", template_folder="templates"
)


@link_short_bp.route("/")
def show_link_page():
    return render_template("boom.html")


@link_short_bp.route("/list")
def show_link_list_page():    
    return render_template("list_links.html")
