from flask import Flask, g

from config import Config

from auth.auth import auth_bp
from link_handling.link_handling import link_short_bp
from api.auth.auth import auth_controller_bp
from api.user.user import user_controller_bp
from api.urlShortner.urlshortner import link_generate_bp
from api.urlRedirection.urlredirection import url_redirection_bp



def create_app():    
    app=Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(link_generate_bp,url_prefix='/api/url')

    app.register_blueprint(url_redirection_bp,url_prefix="/")
    app.register_blueprint(auth_bp,url_prefix='/auth')
    app.register_blueprint(link_short_bp,url_prefix='/urlshort')
    app.register_blueprint(user_controller_bp,url_prefix='/api/users')
    app.register_blueprint(auth_controller_bp,url_prefix='/api/auth')

    return app



app = create_app()

if __name__ == '__main__':
    app.run(debug=True)