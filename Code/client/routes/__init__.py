# first line

from .auth_bp import auth_bp
from .home_bp import home_bp
from .content import content_bp
from .logged.feed_bp import feed_bp
from .logged.profile_bp import profile_bp
from .logged.libraries_bp import libraries_bp
# from .logged.media_view_bp import media_view_bp as mvp
# from .logged.media_upload_bp import media_upload_bp as mub
# from .logged.comment_bp import comments_bp

def register_blueprints(app):
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(content_bp, url_prefix='/content')
    app.register_blueprint(feed_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(libraries_bp)
    # app.register_blueprint(mvp)
    # app.register_blueprint(mub)
    # app.register_blueprint(comments_bp)

# last line