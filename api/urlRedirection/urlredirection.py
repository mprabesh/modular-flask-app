from flask import Blueprint, request,redirect
from .utils import get_user_URL
from init_db import get_db

url_redirection_bp=Blueprint("url_redirection_bp",__name__)


# @url_redirection_bp.route("/<short_link_param>",methods=["GET"])
# def redirect_url(short_link_param):
#     try:
#         if short_link_param:
#             print(short_link_param)
#             original_url=get_user_URL(short_link_param)
#             return redirect(original_url, 302)
#     except Exception as e:
#         print(e)