from flask_google_fonts import GoogleFonts
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


csrf = CSRFProtect()
fonts = GoogleFonts()
login_manager = LoginManager()


def init_extensions(app):
    """Load app extensions."""
    csrf.init_app(app)
    fonts.init_app(app)
    # login_manager.init_app(app)
